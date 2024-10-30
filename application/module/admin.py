from . import *
from application.models.transactions import TransactionStatus


class Admin:

    @staticmethod
    def add_as_admin(email):
        user: User = User.GetUserFromEmail(email)
        if user.is_admin:
            raise CustomException(message="User is already an admin", status_code=400)
        user.is_admin = True
        user.save()
        return return_json(OutputObj(message=f"{email} has been successfully added as admin"))

    @staticmethod
    def remove_as_admin(email):
        user: User = User.GetUserFromEmail(email)
        if not user.is_admin:
            raise CustomException(message="User is already not an admin", status_code=400)
        user.is_admin = False
        user.save()
        return return_json(OutputObj(message=f"{email} has been successfully removed as admin"))

    @staticmethod
    def view_all_users(page, per_page):
        page = int(page)
        per_page = int(per_page)
        _users: User = User.query.order_by(User.id).paginate(page=page, per_page=per_page, error_out=False)
        total_items = _users.total
        results = [item for item in _users.items]
        total_pages = (total_items - 1) // per_page + 1
        pagination_data = {
            "page": page,
            "size": per_page,
            "total_pages": total_pages,
            "total_items": total_items,
            "results": {
                "total_users": len(results),
                "total_active_users": len([x for x in results if not x.isDeactivated]),
                "total_deactivated_users": len([x for x in results if x.isDeactivated]),
                "users": [{**users.to_dict(add_filter=False)} for users in results],
            }
        }
        return return_json(OutputObj(data=pagination_data, message="View all users", status=200))

    @staticmethod
    def view_user_details(user_id):
        user: User = User.GetUser(user_id)
        user_transactions = user.sent_transactions + user.received_transactions
        return return_json(OutputObj(data={
            "user": user.to_dict(),
            "wallets": [x.to_dict() for x in user.wallets],
            "transactions": [{**trans.to_dict(add_filter=False), 'status': trans.status.value, 'transaction_type': trans.transaction_type.value} for trans in user_transactions]},
            message="User details", status=200))

    @staticmethod
    def view_all_transactions(page, per_page):
        page = int(page)
        per_page = int(per_page)
        _transactions: Transactions = Transactions.query.order_by(Transactions.id).paginate(page=page, per_page=per_page, error_out=False)
        total_items = _transactions.total
        results: List[Transactions] = [item for item in _transactions.items]
        total_pages = (total_items - 1) // per_page + 1
        pagination_data = {
            "page": page,
            "size": per_page,
            "total_pages": total_pages,
            "total_items": total_items,
            "results": {
                "total_transactions": len(results),
                "total_approved_transactions": len([x for x in results if x.status.value == TransactionStatus.APPROVED.value]),
                "total_failed_transactions": len([x for x in results if x.status.value == TransactionStatus.FAILED.value]),
                "total_processing_transactions": len([x for x in results if x.status.value == TransactionStatus.PROCESSING.value]),
                "transactions": [{**trans.to_dict(add_filter=False), 'status': trans.status.value, 'transaction_type': trans.transaction_type.value} for trans in results],
            }
        }
        return return_json(OutputObj(data=pagination_data, message="View all transactions", status=200))

    @staticmethod
    def approve_transaction(transaction_id):
        transaction: Transactions = Transactions.query.filter_by(id=transaction_id).first()

        if not transaction:
            raise CustomException(ExceptionCode.TRANSACTION_NOT_FOUND)

        if transaction.status.value == TransactionStatus.APPROVED.value:
            raise CustomException(message="Transaction is already approved", status_code=400)

        transaction.status = TransactionStatus.APPROVED
        transaction.save()
        return return_json(OutputObj(
            message=f"Transaction ID : {transaction} has been successfully approved.",
            code=200
        ))

    @staticmethod
    def cancel_transaction(transaction_id):
        transaction: Transactions = Transactions.query.filter_by(id=transaction_id).first()

        if not transaction:
            raise CustomException(ExceptionCode.TRANSACTION_NOT_FOUND)

        if transaction.status.value == TransactionStatus.FAILED.value:
            raise CustomException(message="Transaction is already failed", status_code=400)

        transaction.status = TransactionStatus.FAILED
        transaction.save()
        return return_json(OutputObj(
            message=f"Transaction ID : {transaction} has been successfully cancelled.",
            code=200
        ))

    @staticmethod
    def deactivate_user(email):
        user = User.GetUserFromEmail(email)

        if user.isDeactivated:
            raise CustomException(ExceptionCode.ACCOUNT_ALREADY_DEACTIVATED)
        user.isDeactivated = True
        user.save()
        return return_json(OutputObj(
            message=f"{email} has been successfully deactivated.",
            code=200
        ))

    @staticmethod
    def activate_user(email):
        user = User.GetUserFromEmail(email)
        if not user.isDeactivated:
            raise CustomException(ExceptionCode.ACCOUNT_ALREADY_ACTIVATED)
        user.isDeactivated = False
        user.save()
        return return_json(OutputObj(
            message=f"{email} has been successfully activated.",
            code=200
        ))

    @staticmethod
    def add_wallet_address(wallet_address, coin_id):
        coins = Coins.query.filter(Coins.id == coin_id).first()
        if not coins:
            raise CustomException(message="Coin does not exist.", status_code=404)
        create_address = AdminWallets(coin_id=coin_id, wallet_id=wallet_address)
        create_address.save()
        return return_json(OutputObj(message=f"{wallet_address} has been successfully added.", code=200))

    @staticmethod
    def remove_wallet_address(wallet_address, coin_id):
        coins = Coins.query.filter(Coins.id == coin_id).first()
        if not coins:
            raise CustomException(message="Coin does not exist.", status_code=404)
        wallet_address: AdminWallets = AdminWallets.query.filter_by(wallet_id=wallet_address).first()
        if not wallet_address:
            raise CustomException(message="Wallet does not exist.", status_code=404)
        wallet_address.delete()
        return return_json(OutputObj(message="Wallet has been successfully removed.", code=200))

    @staticmethod
    def credit_user(wallet_address, amount):
        address: Wallet = Wallet.query.filter_by(wallet_id=wallet_address).first()
        if not wallet_address:
            raise CustomException(message="Wallet does not exist.", status_code=404)
        if amount < 1:
            raise CustomException(message="Amount must be greater than 0.", status_code=400)

        if not address:
            raise CustomException(message="Wallet does not exist.", status_code=404)
        address.balance += amount
        address.save()
        return return_json(OutputObj(message=f"{wallet_address} has been successfully credited with {amount}", code=200))

    @staticmethod
    def debit_user(wallet_address, amount):
        address: Wallet = Wallet.query.filter_by(wallet_id=wallet_address).first()
        if not wallet_address:
            raise CustomException(message="Wallet does not exist.", status_code=404)
        if amount < 1:
            raise CustomException(message="Amount must be greater than 0.", status_code=400)

        if not address:
            raise CustomException(message="Wallet does not exist.", status_code=404)

        if amount > address.balance:
            raise CustomException(message="Amount cannot be greater than balance.", status_code=400)

        address.balance -= amount
        address.save()
        return return_json(OutputObj(message=f"{wallet_address} has been successfully debited with {amount}", code=200))
