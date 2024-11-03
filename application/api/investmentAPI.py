from flask import Blueprint, request
from application.module.investments import InvestmentModule, InvestmentCreation
from application.module.authentication import Authentication
from application.api import authenticate
from application.utils.authenticator import response_decorator

investment_blueprint = Blueprint('investment', __name__)
authenticationModel = Authentication()
investmentModel = InvestmentModule()


@investment_blueprint.route('/create-investment', methods=['POST'])
@authenticate()
@response_decorator
def create_investment():
    req = request.get_json()
    data = InvestmentCreation(
        scheme_id=req.get('scheme_id'),
        amount=req.get('amount'),
        deposit_type=req.get('deposit_type')
    )
    return investmentModel.create_investment(data)


@investment_blueprint.route('/payment-wallet', methods=['GET'])
@authenticate()
@response_decorator
def get_payment_wallet():
    return investmentModel.payment_wallet()


@investment_blueprint.route('/confirm-payment', methods=['POST'])
@authenticate()
@response_decorator
def confirm_payment():
    req = request.get_json()
    return investmentModel.confirm_payment(req.get('investment_id'))


@investment_blueprint.route('/<int:id>', methods=['GET'])
@authenticate()
@response_decorator
def get_investment(id):
    return investmentModel.get_investment(id)


@investment_blueprint.route(rule='/all', methods=['GET'])
@authenticate()
@response_decorator
def get_all_investments():
    return investmentModel.get_user_investments()


@investment_blueprint.route('/schemes', methods=['GET'])
@authenticate()
@response_decorator
def get_all_investment_schemes():
    return investmentModel.get_investment_schemes()
