from . import *


class Wallets:

    @classmethod
    def create_wallet(cls, wallet_name, wallet_type):
        Wallet.create_wallet(wallet_type, wallet_name, current_user)
        return "Wallet created successfully"

    @classmethod
    def fetch_wallet(cls, wallet_id):
        res: Wallet = Wallet.query.filter_by(wallet_id=wallet_id, user=current_user).first()
        if not res:
            raise CustomException(message="Wallet not found", status_code=404)
        return res.to_dict()

    @classmethod
    def list_wallet(cls):
        wallets = current_user.wallets.all()
        return wallets
