import uuid
from datetime import timedelta

import jwt
from flask_jwt_extended import create_access_token, create_refresh_token

from . import *
from application import SECRET_KEY


class Authentication:
    @staticmethod
    def Login(email, password):
        user: User = User.query.filter_by(email=email).first()

        if user and user.isDeactivated:
            raise CustomException(ExceptionCode.ACCOUNT_ALREADY_DEACTIVATED)

        if user and user.password and bcrypt.checkpw(str(password).encode(), user.password.encode()):
            access_token, refresh_token = User.generate_access_token(user)

            return return_json(
                OutputObj(message="Login successful", data={"access_token": access_token, "refresh_token": refresh_token, 'expiration_in_seconds': 120, **user.to_dict()}, code=200)
            )

        else:
            raise CustomException(ExceptionCode.INVALID_CREDENTIALS)

    @staticmethod
    def update_password(email: str, code: str, password):
        _user: User = User.query.filter_by(email=email).first()

        if not _user:
            raise CustomException(message="User does not exist", status_code=404)

        confirm_code: ConfirmationCode = ConfirmationCode.query.filter(ConfirmationCode.code == code, ConfirmationCode.user_id == _user.id).first()
        current_time = datetime.datetime.now()

        if not confirm_code:
            raise CustomException(message="Invalid confirmation code", status_code=400)

        if current_time > confirm_code.expiration:
            raise CustomException(message="OTP code has already expired", status_code=400)

        _user.UpdatePassword(password)

        return return_json(OutputObj(message="Password has been set successfully. Please login again.", code=200))

    @staticmethod
    def admin_set_up_password(email, password):

        _user: User = User.query.filter_by(email=email).first()

        if not _user:
            raise CustomException(ExceptionCode.ACCOUNT_NOT_FOUND)

        _user.UpdatePassword(password)

        return return_json(OutputObj(message="Password has been set successfully.", code=200))

    def set_up_password(self, email, password, token):

        if not email or not password or not token:
            raise CustomException(message="email or password or token is empty", status_code=400)

        self.is_valid_token(token)
        _user: User = User.query.filter_by(email=email).first()

        if not _user:
            raise CustomException(ExceptionCode.ACCOUNT_NOT_FOUND)

        _user.UpdatePassword(password)

        return return_json(OutputObj(message="Password has been set successfully.", code=200))

    @staticmethod
    def reset_password(email):
        user: User = User.query.filter_by(email=email).first()

        if not user:
            raise CustomException(message="user does not exist", status_code=404)

        res = Helper.send_otp(user)
        return return_json(OutputObj(message=res, code=200))

    @staticmethod
    def invite_link(email, type):

        if not email or not type:
            raise CustomException(message="Email and type are required", status_code=400)

        user: User = User.query.filter_by(id=current_user.id).first()
        if not user:
            raise CustomException(message="user does not exist", status_code=404)

        if type not in ['teacher', 'parent']:
            raise CustomException(message="Type must be teacher|parent", status_code=400)

        school = User.GetSchool(user.id)
        school_id = school[0].id if isinstance(school, list) else school.id
        school_name = school[0].name if isinstance(school, list) else school.name

        if type == 'teacher':
            role = "colearner"
            link = f"https://keyhub-frontend.vercel.app/school/{school_id}/teacher/sign-up"
        else:
            role = "parent"
            link = f"https://keyhub-frontend.vercel.app/school/{school_id}/parent/sign-up"

        EmailHandler.send_invite_email(email, school_name, role, link)
        return return_json(OutputObj(message=f"Invite link has been successfully sent to {email}", code=200))

    @staticmethod
    def is_valid_token(token):
        try:
            jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            return True
        except jwt.ExpiredSignatureError:
            raise CustomException(message="Password expired", status_code=401)
        except jwt.InvalidTokenError:
            # If the token is invalid or tampered with, return False
            raise CustomException(message="Invalid token", status_code=401)
