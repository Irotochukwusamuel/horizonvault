import uuid
from datetime import timedelta
import datetime
import random
import string
import jwt
from flask_jwt_extended import create_access_token, create_refresh_token

from . import *
from application import SECRET_KEY


class Authentication:

    @staticmethod
    def send_otp(user):
        otp_code = ''.join(random.choices(string.digits, k=4))
        expiration_time = datetime.datetime.now() + datetime.timedelta(minutes=2)
        add_to_confirmation = ConfirmationCode(email=user.email, user_id=user.id, code=otp_code, expiration=expiration_time)
        add_to_confirmation.save(refresh=True)
        EmailHandler.email(user.email, "Email verification", f"Your one-time-password is {otp_code}")
        return True

    def resent_otp(self, email):
        user = User.query.filter_by(email=email).first()
        if not user:
            raise CustomException(message="User does not exist", status_code=404)
        self.send_otp(user)
        return return_json(OutputObj(
            message=f"An OTP has been sent to {email} for verification",
            code=200
        ))

    def signUp(self, email: str, password: str, username: str):

        if not email or not password or not username:
            raise CustomException(message="invalid data passed", status_code=401)

        try:
            User.is_email_exists(email)
            User.is_username_exists(username)
            password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            user = User.CreateUser(email, username, password.decode())
            user.referral_id = Referral.generate_referral_id(user.id)
            user.save(refresh=True)
            self.send_otp(user)
            return return_json(OutputObj(
                message=f"An OTP has been sent to {email} for verification",
                code=200
            ))
        except Exception as e:
            raise e

    @staticmethod
    def setup_account():
        Wallet.generate_wallets(current_user)
        return "Account setup is completed."

    @staticmethod
    def login(email, password):

        if not email or not password:
            raise CustomException(message="invalid data passed", status_code=401)

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

        if not email or not password:
            raise CustomException(message="invalid data passed", status_code=401)

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

        return return_json(OutputObj(message="Password has been updated successfully. Please login again.", code=200))

    @staticmethod
    def reset_password(email):
        if not email:
            raise CustomException(message="Invalid data passed", status_code=401)

        user: User = User.query.filter_by(email=email).first()

        if not user:
            raise CustomException(message="user does not exist", status_code=404)

        res = Helper.send_otp(user)
        return return_json(OutputObj(message=res, code=200))

    @staticmethod
    def emailVerification(email: str, code: str):
        user = User.query.filter_by(email=email).first()
        if not user:
            raise CustomException(message="User does not exist", status_code=404)
        ConfirmationCode.is_otp_valid(user, code)

        user.isEmailVerified = True
        user.save(refresh=True)
        access_token, refresh_token = User.generate_access_token(user)
        return return_json(
            OutputObj(
                message="Email verified successfully",
                data={"access_token": access_token, "refresh_token": refresh_token, 'expiration_in_seconds': 120, **user.to_dict()},
                code=200
            )
        )

    @staticmethod
    def msisdnVerification(msisdn: str, code: str):
        user = User.query.filter_by(msisdn=msisdn).first()
        if not user:
            raise CustomException(message="User does not exist", status_code=404)
        ConfirmationCode.is_otp_valid(user, code)

        user.isMsisdnVerified = True
        user.save(refresh=True)
        return "Phone number verified successfully"

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
