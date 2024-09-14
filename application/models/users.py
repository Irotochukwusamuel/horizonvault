from typing import Callable

import bcrypt

from application import db
from application.Mixins.GenericMixins import GenericMixin
from exceptions.codes import ExceptionCode
from exceptions.custom_exception import CustomException
from flask_jwt_extended import create_access_token, create_refresh_token
import datetime


class User(db.Model, GenericMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), nullable=True, unique=True)
    msisdn = db.Column(db.String(250), nullable=True, unique=True)
    password = db.Column(db.String(350), nullable=True)
    referral_id = db.Column(db.String(250), nullable=True, unique=True)
    first_name = db.Column(db.String(350), nullable=True)
    last_name = db.Column(db.String(350), nullable=True)
    country = db.Column(db.String(350), nullable=True)
    language = db.Column(db.String(350), default='en')
    isDeactivated = db.Column(db.Boolean, default=False)
    isEmailVerified = db.Column(db.Boolean, default=False)
    isMsisdnVerified = db.Column(db.Boolean, default=False)
    has_email_notification_enabled = db.Column(db.Boolean, default=False)
    deactivate_reason = db.Column(db.String(450), nullable=True)

    wallets = db.relationship('Wallet', back_populates='user', cascade="all, delete-orphan")
    confirmation_codes = db.relationship('ConfirmationCode', back_populates='user', cascade="all, delete-orphan")
    notifications = db.relationship("Notification", back_populates='user', cascade="all, delete-orphan")
    referrals_made = db.relationship("Referral", back_populates="referrer", lazy='dynamic', foreign_keys='Referral.referrer_id')
    referrals_received = db.relationship("Referral", back_populates="referred", lazy='dynamic', foreign_keys='Referral.referred_id')

    def as_dict(self, include_sensitive_info=False):
        """
        Convert the User object to a dictionary representation,
        excluding sensitive information like password and id.
        """
        return {
            key: getattr(self, key)
            for key in ['email', 'msisdn', 'isDeactivated', 'deactivate_reason']
            if include_sensitive_info or key not in {'password', 'id'}
        }

    @classmethod
    def generate_access_token(cls, user) -> tuple:
        access_token = create_access_token(identity=user.id, expires_delta=datetime.timedelta(minutes=120))
        refresh_token = create_refresh_token(identity=user.id)
        return access_token, refresh_token

    @classmethod
    def is_email_exists(cls, email):
        if cls.query.filter_by(email=email).first():
            raise CustomException(message="Email already exists", status_code=401)
        return False

    @classmethod
    def is_msisdn_exists(cls, msisdn):
        if cls.query.filter_by(msisdn=msisdn).first():
            raise CustomException(message="Phone number already exists", status_code=401)
        return False

    @classmethod
    def GetUser(cls, user_id):
        user = User.query.filter_by(id=user_id).first()
        if not user:
            raise CustomException(message="User does not exist", status_code=404)
        return user

    @classmethod
    def CreateUser(cls, email, msisdn, role, password=None):
        try:
            user = User(email=email, msisdn=msisdn, password=password)
            user.roles = role
            db.session.add(user)
            db.session.commit()
            db.session.refresh(user)
            return user
        except Exception as e:
            db.session.rollback()
            raise e

    def UpdatePassword(self, password):
        try:
            hash_value = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            self.password = hash_value.decode()
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            raise CustomException(ExceptionCode.DATABASE_ERROR)

    def UpdateMsisdn(self, msisdn):
        try:
            self.msisdn = msisdn
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            raise CustomException(ExceptionCode.DATABASE_ERROR)
