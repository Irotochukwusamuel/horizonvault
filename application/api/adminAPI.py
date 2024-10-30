from flask import Blueprint, request
from application.module.admin import Admin
from application.module.authentication import Authentication
from application.api import authenticate, is_admin

admin_blueprint = Blueprint('admin', __name__)
authenticationModel = Authentication()
adminModel = Admin()


@admin_blueprint.route('/add-admin', methods=['POST'])
@authenticate()
@is_admin()
def add_as_admin():
    req = request.get_json()
    email = req.get('email')
    return adminModel.add_as_admin(email)


@admin_blueprint.route('/remove-admin', methods=['POST'])
@authenticate()
@is_admin()
def remove_as_admin():
    req = request.get_json()
    email = req.get('email')
    return adminModel.remove_as_admin(email)


@admin_blueprint.route('/users', methods=['GET'])
@authenticate()
@is_admin()
def view_all_users():
    page = request.args.get('page', 1)
    per_page = request.args.get('per_page', 10)
    return adminModel.view_all_users(page, per_page)


@admin_blueprint.route('/users/<int:user_id>', methods=['GET'])
@authenticate()
@is_admin()
def view_user_details(user_id):
    return adminModel.view_user_details(user_id)


@admin_blueprint.route('/transactions', methods=['GET'])
@authenticate()
@is_admin()
def view_all_transactions():
    page = request.args.get('page', 1)
    per_page = request.args.get('per_page', 10)
    return adminModel.view_all_transactions(page, per_page)


@admin_blueprint.route('/approve-transaction', methods=['POST'])
@authenticate()
@is_admin()
def approve_transaction():
    req = request.get_json()
    transaction_id = req.get('transaction_id')
    return adminModel.approve_transaction(transaction_id)


@admin_blueprint.route('/cancel-transaction', methods=['POST'])
@authenticate()
@is_admin()
def cancel_transaction():
    req = request.get_json()
    transaction_id = req.get('transaction_id')
    return adminModel.cancel_transaction(transaction_id)


@admin_blueprint.route('/deactivate-user', methods=['POST'])
@authenticate()
@is_admin()
def deactivate_user():
    req = request.get_json()
    email = req.get('email')
    return adminModel.deactivate_user(email)


@admin_blueprint.route('/activate-user', methods=['POST'])
@authenticate()
@is_admin()
def activate_user():
    req = request.get_json()
    email = req.get('email')
    return adminModel.activate_user(email)



@admin_blueprint.route('/admin-wallets', methods=['GET'])
@authenticate()
@is_admin()
def view_admin_wallets():
    return adminModel.view_admin_wallets()

@admin_blueprint.route('/add-wallet', methods=['POST'])
@authenticate()
@is_admin()
def add_wallet_address():
    req = request.get_json()
    wallet_address = req.get('wallet_address')
    coin_id = req.get('coin_id')
    return adminModel.add_wallet_address(wallet_address, coin_id)


@admin_blueprint.route('/remove-wallet', methods=['POST'])
@authenticate()
@is_admin()
def remove_wallet_address():
    req = request.get_json()
    wallet_address = req.get('wallet_address')
    coin_id = req.get('coin_id')
    return adminModel.remove_wallet_address(wallet_address, coin_id)


@admin_blueprint.route('/credit-user', methods=['POST'])
@authenticate()
@is_admin()
def credit_user():
    req = request.get_json()
    wallet_address = req.get('wallet_address')
    amount = req.get('amount')
    return adminModel.credit_user(wallet_address, amount)


@admin_blueprint.route('/debit-user', methods=['POST'])
@authenticate()
@is_admin()
def debit_user():
    req = request.get_json()
    wallet_address = req.get('wallet_address')
    amount = req.get('amount')
    return adminModel.debit_user(wallet_address, amount)
