from flask import Blueprint, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from application.module.authentication import Authentication
from application.utils.output import return_json, OutputObj

auth_blueprint = Blueprint('auth', __name__)
authenticationModel = Authentication()


@auth_blueprint.route('/refresh-token', methods=['GET'])
@jwt_required(refresh=True)
def refresh_token():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return return_json(OutputObj(message="Token has been refreshed", data={"access_token": access_token}, code=200))


@auth_blueprint.route('/login', methods=['POST'])
def login():
    req = request.json
    email = req.get('email')
    password = req.get('password')
    return authenticationModel.Login(email, password)


@auth_blueprint.route('/update-password', methods=['POST'])
def update_password():
    req = request.json
    code = req.get('otp')
    password = req.get('password')
    email = req.get('email')
    return authenticationModel.update_password(email, code, password)


@auth_blueprint.route('/set-password', methods=['POST'])
def admin_set_password():
    req = request.json
    email = req.get('email')
    password = req.get('password')
    return authenticationModel.admin_set_up_password(email, password)


@auth_blueprint.route('/set-user-password', methods=['POST'])
def set_user_password():
    req = request.json
    email = req.get('email')
    password = req.get('password')
    token = req.get('token')
    return authenticationModel.set_up_password(email, password, token)


@auth_blueprint.route('/reset-password', methods=['POST'])
def reset_password():
    req = request.json
    email = req.get('email')
    return authenticationModel.reset_password(email)


@auth_blueprint.route('/invite-link', methods=['POST'])
@jwt_required()
def invite_user():
    req = request.json
    email = req.get('email')
    type = req.get('type')
    return authenticationModel.invite_link(email, type)


@auth_blueprint.route('/ping', methods=['GET'])
def ping():
    return return_json(OutputObj(message="pong!!"))
