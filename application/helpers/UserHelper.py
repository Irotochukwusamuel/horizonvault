import datetime
import random
import string

from flask import request

from application import db
from application.models import ConfirmationCode
from application.module import current_user
from application.utils.emailHandler import EmailHandler
from exceptions.custom_exception import CustomException, ExceptionCode


class Helper:

    @classmethod
    def generate_token(cls):
        return ''.join(random.choices(string.digits, k=4))

    @classmethod
    def send_otp(cls, user):
        otp_code = cls.generate_token()
        expiration_time = datetime.datetime.now() + datetime.timedelta(minutes=2)
        add_to_confirmation = ConfirmationCode(email=user.email, user_id=user.id, code=otp_code, expiration=expiration_time)
        add_to_confirmation.save(refresh=True)
        EmailHandler.send_otp(user.email, otp_code)
        return f"OTP code has been sent to {user.email}"

    @classmethod
    def disable_account(cls, user, reason):
        try:
            user.isDeactivated = not user.isDeactivated
            user.deactivate_reason = reason
            db.session.commit()
            return f"{user.email} account has been deactivated" if user.isDeactivated else f"{user.email} account has been activated"

        except Exception:
            db.session.rollback()
            raise CustomException(ExceptionCode.DATABASE_ERROR)
