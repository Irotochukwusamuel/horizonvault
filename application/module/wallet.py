from sqlalchemy import or_
from sqlalchemy.orm import joinedload

from . import *
from application.models.transactions import TransactionType, TransactionStatus


class Wallets:

    @classmethod
    def fetch_wallet(cls, wallet_id):
        if not wallet_id:
            raise CustomException(ExceptionCode.INVALID_INPUT)

        res: Wallet = Wallet.query.filter_by(wallet_id=wallet_id, user=current_user).first()
        if not res:
            raise CustomException(message="Wallet not found", status_code=404)
        return res.to_dict()

    @classmethod
    def get_user(cls):
        user: User = User.GetUser(current_user.id)
        if not user:
            raise CustomException(ExceptionCode.ACCOUNT_NOT_FOUND)
        return user.to_dict()

    @classmethod
    def list_wallet(cls):
        wallets: List[Wallet] = (
            Wallet.query
            .options(joinedload(Wallet.coins))
            .filter(Wallet.user_id == current_user.id)
            .all()
        )

        wallet_list = [{
            **w.to_dict(),
            "wallet_name": w.coins.name,
            "wallet_symbol": w.coins.symbol,
            "total": int(w.balance) * (w.coins.rate if w.coins.rate not in [0, None, ''] else 1) if w.coins.symbol != "USDC" else w.balance
        } for w in wallets]

        return wallet_list

    @classmethod
    def list_all_wallets(cls):
        coins: List[Coins] = Coins.query.all()
        return [x.to_dict(add_filter=False) for x in coins]

    @classmethod
    def deposit(cls, wallet_name):
        if not wallet_name:
            raise CustomException(ExceptionCode.INVALID_INPUT)

        coin: Coins = Coins.query.filter(Coins.name == wallet_name).first()
        if not coin:
            raise CustomException(ExceptionCode.WALLET_NOT_FOUND)
        return random.choice(coin.admin_wallets).wallet_id if coin.admin_wallets else "no wallet found"

    @classmethod
    def withdraw(cls, destination_address, amount, network, source):

        if not destination_address or not amount or not network or not source:
            raise CustomException(ExceptionCode.INVALID_INPUT)

        coin: Coins = Coins.query.filter(Coins.name == source).first()

        if not coin:
            raise CustomException(ExceptionCode.WALLET_NOT_FOUND)

        account: Wallet = Wallet.query.filter(Wallet.user == current_user, Wallet.coin_id == coin.id).first()

        if amount > account.balance:
            raise CustomException(ExceptionCode.INSUFFICIENT_FUNDS)

        account.balance -= amount
        db.session.commit()

        trans = Transactions(
            amount=amount,
            network=network,
            transaction_type=TransactionType.TRANSACT_C2B,
            coins=account.coins,
            sender_user=current_user,
            receiver_address=destination_address
        )
        trans.save(refresh=True)

        return "Transaction is been processed."

    @classmethod
    def transfer(cls, source, receiver, amount):

        if not source or not receiver or not amount:
            raise CustomException(ExceptionCode.INVALID_INPUT)

        if receiver == current_user.email or receiver == current_user.id:
            raise CustomException(ExceptionCode.SELF_TRANSFER_NOT_PROCESSED)

        coin: Coins = Coins.query.filter(Coins.name == source).first()

        if not coin:
            raise CustomException(ExceptionCode.WALLET_NOT_FOUND)

        sender_account: Wallet = Wallet.query.filter(Wallet.user == current_user, Wallet.coin_id == coin.id).first()

        if not sender_account:
            raise CustomException(ExceptionCode.WALLET_NOT_FOUND)

        receiver: User = User.query.filter(or_(User.email == receiver, User.id == receiver)).first()

        receiver_account: Wallet = Wallet.query.filter(Wallet.user == receiver, Wallet.coin_id == coin.id).first()

        if not receiver_account:
            raise CustomException(ExceptionCode.WALLET_NOT_FOUND)

        if not receiver:
            raise CustomException(ExceptionCode.INVALID_RECEIVER_ACCOUNT)

        if amount > sender_account.balance:
            raise CustomException(ExceptionCode.INSUFFICIENT_FUNDS)

        sender_account.balance -= amount
        receiver_account.balance += amount
        db.session.commit()

        trans = Transactions(
            amount=amount,
            transaction_type=TransactionType.TRANSACT_C2C,
            coins=sender_account.coins,
            receiver_user=receiver,
            sender_user=current_user,
            status=TransactionStatus.APPROVED
        )
        trans.save(refresh=True)

        return "Transaction successful."

    @classmethod
    def history(cls):
        trans: List[Transactions] = Transactions.query.filter(or_(Transactions.sender_user == current_user, Transactions.receiver_user == current_user)).order_by(Transactions.id).all()
        return [
            {
                **x.to_dict(),
                "transaction_type": x.transaction_type.value,
                "status": x.status.value,
                "coin": x.coins.to_dict(),
                "receiver": x.receiver_user.to_dict() if x.receiver_user else None,
                "sender": x.sender_user.to_dict() if x.sender_user else None
            }
            for x in trans
        ]

    @classmethod
    def swap(cls, from_wallet, to_wallet, amount):
        if amount <= 0:
            raise CustomException(message="Amount must be greater than zero.", status_code=400)

        convert_from: Wallet = Wallet.query.join(Coins).filter(Coins.name == from_wallet, Wallet.user == current_user).first()
        convert_to: Wallet = Wallet.query.join(Coins).filter(Coins.name == to_wallet, Wallet.user == current_user).first()

        if not convert_from or not convert_to:
            raise CustomException(message="One or both wallets not found.", status_code=404)

        if amount > convert_from.balance:
            raise CustomException(ExceptionCode.INSUFFICIENT_FUNDS)

        amount_topUp = (amount * convert_from.coins.rate) / convert_to.coins.rate
        print("amount_topUp", amount_topUp)
        convert_from.balance -= amount
        convert_to.balance += amount_topUp
        db.session.commit()
        return "Swap successful."
