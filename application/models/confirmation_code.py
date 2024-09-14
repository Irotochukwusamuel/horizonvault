from application import db
from application.Mixins.GenericMixins import GenericMixin
import datetime
import random
import string
from exceptions.custom_exception import CustomException


class ConfirmationCode(db.Model, GenericMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=True)
    code = db.Column(db.String(150), nullable=True)
    msisdn = db.Column(db.String(150), nullable=True)
    counter = db.Column(db.Integer, nullable=True, default=0)
    expiration = db.Column(db.DateTime, nullable=True)
    user = db.relationship("User", back_populates='confirmation_codes')

    @classmethod
    def generate_token(cls, length=4):
        return ''.join(random.choices(string.digits, k=length))

    @classmethod
    def create_confirmation_code(cls, user, contact_info, contact_type):
        otp_code = cls.generate_token()
        expiration_time = datetime.datetime.now() + datetime.timedelta(minutes=2)

        confirmation_code = ConfirmationCode(
            user_id=user.id,
            code=otp_code,
            expiration=expiration_time,
            **{contact_type: contact_info}
        )

        confirmation_code.save(refresh=True)

        return f"OTP code has been sent to {contact_info}"

    @classmethod
    def send_email_confirmation_code(cls, user):
        return cls.create_confirmation_code(user, user.email, 'email')

    @classmethod
    def send_msisdn_confirmation_code(cls, user):
        return cls.create_confirmation_code(user, user.msisdn, 'msisdn')

    @classmethod
    def is_otp_valid(cls, user, code):
        confirm_code: ConfirmationCode = cls.query.filter_by(code=code, user_id=user.id).first()
        current_time = datetime.datetime.now()

        if confirm_code.counter >= 1:
            raise CustomException(message="Invalid confirmation code", status_code=400)

        if not confirm_code:
            raise CustomException(message="Invalid confirmation code", status_code=400)

        if current_time > confirm_code.expiration:
            raise CustomException(message="OTP code has already expired", status_code=400)

        confirm_code.counter += 1
        confirm_code.save()

        return True
