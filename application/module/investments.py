import random
from typing import Literal, Union
from . import *
from application.models.investments import InvestmentStatus, DepositType, InvestmentInterval
from dataclasses import dataclass

from ..utils.authenticator import required_arguments_exist


@dataclass
class InvestmentCreation:
    scheme_id: int
    amount: float
    deposit_type: Literal['cash', 'wallet']

    def __post_init__(self):
        if not self.scheme_id or not self.amount or not self.deposit_type:
            raise CustomException(message="scheme_id and amount or deposit_type is required", status_code=400)

        if self.deposit_type not in ('cash', 'wallet'):
            raise CustomException(message="Deposit type must be 'cash' or 'wallet'", status_code=400)


class InvestmentModule:

    def __init__(self):
        self.coin_symbol: str = "USDC"

    def create_investment(self, data: InvestmentCreation):

        deposit_type = data.deposit_type.lower()

        scheme: InvestmentScheme = InvestmentScheme.query.filter_by(id=data.scheme_id).first()

        if not scheme:
            raise CustomException(message="No Investment scheme found with the ID", status_code=400)

        usdt_wallet = None

        if deposit_type == "cash":
            status = InvestmentStatus.PROCESSING
            message = "Investment has been initiated, Please make payment and click on confirm payment to continue."

        else:
            status = InvestmentStatus.APPROVED
            usdt_coin: Coins = Coins.query.filter(Coins.symbol == self.coin_symbol).first()
            usdt_wallet: Wallet = Wallet.query.filter(Wallet.coin_id == usdt_coin.id, Wallet.user_id == current_user.id).first()
            if data.amount > usdt_wallet:
                raise CustomException(ExceptionCode.INSUFFICIENT_FUNDS, status_code=400)
            usdt_wallet.balance -= data.amount
            usdt_wallet.save(refresh=True)
            message = "Investment has been approved."

        invest = Investment(
            scheme_id=scheme.id,
            user_id=current_user.id,
            wallet_id=usdt_wallet.id if usdt_wallet else None,
            amount=data.amount,
            status=status,
            deposit_type=deposit_type
        )
        invest.save()
        EmailHandler.email(current_user.email, "Investment", message)
        return message

    @classmethod
    def payment_wallet(cls):
        wallet_list = AdminWallets.query.all()
        return random.choice(wallet_list) if wallet_list else "No wallet address available at the moment"

    @classmethod
    @required_arguments_exist
    def confirm_payment(cls, investment_id: int):
        cls.update_investment_status(investment_id, InvestmentStatus.PENDING.value)

    @classmethod
    @required_arguments_exist
    def update_investment_status(cls, investment_id: int, status: str) -> bool:
        invest = Investment.get_investment(investment_id)
        invest.status = status
        invest.save()
        EmailHandler.email(invest.user_id, "Investment", f"Your Investment has been updated to {status}")
        return return_json(OutputObj(message=f"Investment status has been successfully updated."))

    @classmethod
    @required_arguments_exist
    def delete_investment(cls, investment_id: int) -> bool:
        invest = Investment.get_investment(investment_id)
        invest.delete()
        return return_json(OutputObj(message=f"Investment  has been successfully deleted."))

    @staticmethod
    def investment_response(invest: Investment):
        res = {
            **invest.to_dict(add_filter=False),
            "status": invest.status.value,
            "deposit_type": invest.deposit_type.value,
            "investment_name": invest.scheme.name,
            "investment_rate": invest.scheme.rate,
            "investment_interval": invest.scheme.interval.value,

        }

        if invest.wallet_id:
            res.update({
                "wallet_id": invest.wallet_id,
                "wallet_name": invest.wallets.name
            })

        return res

    @classmethod
    @required_arguments_exist
    def get_investment(cls, investment_id: int):
        invest = Investment.get_investment(investment_id)
        return cls.investment_response(invest)

    @classmethod
    def get_user_investments(cls):
        invest = current_user.investments
        return [cls.investment_response(x) for x in invest]

    @classmethod
    def get_all_investments(cls):
        invest = Investment.query.all()
        return return_json(OutputObj(data=[cls.investment_response(x) for x in invest]))

    @classmethod
    def get_investment_schemes(cls):
        schemes: List[InvestmentScheme] = InvestmentScheme.query.all()
        return [{**x.to_dict(), "interval": x.interval.value} for x in schemes]

    @classmethod
    @required_arguments_exist
    def delete_investment_scheme(cls, scheme_id: int):
        scheme: InvestmentScheme = InvestmentScheme.query.filter(InvestmentScheme.id == scheme_id).first()
        scheme.delete()
        return return_json(OutputObj(message=f"Investment scheme has been successfully deleted."))

    @classmethod
    @required_arguments_exist
    def add_investment_scheme(cls, name: str, rate: Union[float, int], minimum: Union[float, int], maximum: Union[float, int], interval: str):

        if not name or not rate or not minimum or not maximum or not interval:
            raise CustomException(message=" name, rate, minimum, maximum, interval are required", status_code=400)

        expected_intervals = [x.value for x in InvestmentInterval]
        if interval not in expected_intervals:
            raise CustomException(message=f"Interval must be one of {expected_intervals}", status_code=400)

        scheme_exist = InvestmentScheme.query.filter(InvestmentScheme.name == name).first()

        if scheme_exist:
            raise CustomException(message="Scheme name already exists", status_code=401)

        scheme_add = InvestmentScheme(name=name, rate=rate, minimum=minimum, maximum=maximum, interval=interval)
        scheme_add.save(refresh=True)
        return return_json(OutputObj(message=f"Investment scheme has been successfully added."))
