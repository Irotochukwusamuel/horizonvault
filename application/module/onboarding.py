from . import *


class Onboarding:

    @staticmethod
    def signUp(email: str, password: str):
        User.is_email_exists(email)
        password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        user = User(email=email, password=password.decode())
        user.referral_id = Referral.generate_referral_id(user.id)
        user.save(refresh=True)
        ConfirmationCode.send_email_confirmation_code(user)
        access_token, refresh_token = User.generate_access_token(user)
        return return_json(
            OutputObj(
                message="Registration successful, Kindly verify your email.",
                data={"access_token": access_token, "refresh_token": refresh_token, 'expiration_in_seconds': 120, **user.to_dict()},
                code=200
            )
        )

    @staticmethod
    def emailVerification(email: str, code: str):
        user = User.query.filter_by(email=email).first()
        if not user:
            raise CustomException(message="User does not exist", status_code=404)
        ConfirmationCode.is_otp_valid(user, code)

        user.isEmailVerified = True
        user.save(refresh=True)
        return "Email verified successfully"

    @staticmethod
    def msisdnVerification(msisdn: str, code: str):
        user = User.query.filter_by(msisdn=msisdn).first()
        if not user:
            raise CustomException(message="User does not exist", status_code=404)
        ConfirmationCode.is_otp_valid(user, code)

        user.isMsisdnVerified = True
        user.save(refresh=True)
        return "Phone number verified successfully"
