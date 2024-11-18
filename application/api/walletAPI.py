from flask import Blueprint, request
from application.module.wallet import Wallets
from application.utils.output import return_json, OutputObj
from application.api import authenticate

wallet_blueprint = Blueprint('wallet', __name__)
walletModel = Wallets()


@wallet_blueprint.route('/balance', methods=['GET'])
@authenticate()
def balance():
    return return_json(OutputObj(message="User balance", data=walletModel.list_wallet(), code=200))


@wallet_blueprint.route('/wallets', methods=['GET'])
@authenticate()
def wallets():
    return return_json(OutputObj(message="User balance", data=walletModel.list_all_wallets(), code=200))


@wallet_blueprint.route('/get-user', methods=['GET'])
@authenticate()
def get_user():
    return return_json(OutputObj(message="User", data=walletModel.get_user(), code=200))


@wallet_blueprint.route('/deposit', methods=['POST'])
@authenticate()
def deposit():
    req = request.get_json()
    wallet_name = req.get('wallet_name')
    return return_json(OutputObj(message="Deposit Successful", data=walletModel.deposit(wallet_name), code=200))


@wallet_blueprint.route('/withdraw', methods=['POST'])
@authenticate()
def withdraw():
    req = request.get_json()
    destination_address = req.get('destination_address')
    amount = req.get('amount')
    network = req.get('network')
    source = req.get('source')
    return return_json(OutputObj(message="Withdrawal Successful", data=walletModel.withdraw(destination_address, amount, network, source), code=200))


@wallet_blueprint.route('/transfer', methods=['POST'])
@authenticate()
def transfer():
    req = request.get_json()
    amount = req.get('amount')
    receiver = req.get('receiver')
    source = req.get('source')
    return return_json(OutputObj(message="Transfer Successful", data=walletModel.transfer(source, receiver, amount), code=200))


@wallet_blueprint.route('/swap', methods=['POST'])
@authenticate()
def swap():
    req = request.get_json()
    amount = req.get('amount')
    from_wallet = req.get('from_wallet')
    to_wallet = req.get('to_wallet')
    return return_json(OutputObj(message="Swap Successful", data=walletModel.swap(from_wallet, to_wallet, amount), code=200))


@wallet_blueprint.route('/history', methods=['GET'])
@authenticate()
def history():
    return return_json(OutputObj(message="Transaction History", data=walletModel.history(), code=200))
