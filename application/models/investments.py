from typing import Optional

from application import db
from application.Mixins.GenericMixins import GenericMixin
import enum
from sqlalchemy import Enum

from exceptions.custom_exception import CustomException


class DepositType(enum.Enum):
    CASH = "cash"
    WALLET = "wallet"


class InvestmentStatus(enum.Enum):
    PENDING = 'pending'
    PROCESSING = 'processing'
    APPROVED = 'approved'
    FAILED = 'failed'
    COMPLETED = 'completed'


class InvestmentInterval(enum.Enum):
    DAILY = 'daily'
    MONTHLY = 'monthly'
    BIWEEKLY = 'bi-weekly'
    WEEKLY = 'weekly'
    YEARLY = 'yearly'
    TRIDAYS = 'tri-days'
    BIDAYS = 'bi-days'


class InvestmentScheme(db.Model, GenericMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    rate = db.Column(db.Float, nullable=False)
    minimum = db.Column(db.Float, nullable=False)
    maximum = db.Column(db.Float, nullable=False)
    interval = db.Column(Enum(InvestmentInterval), default=InvestmentInterval.DAILY, nullable=False)
    investments = db.relationship("Investment", back_populates="scheme")


class Investment(db.Model, GenericMixin):
    id = db.Column(db.Integer, primary_key=True)
    scheme_id = db.Column(db.Integer, db.ForeignKey("investment_scheme.id"), nullable=False, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, index=True)
    wallet_id = db.Column(db.Integer, db.ForeignKey("wallet.id"), nullable=True, index=True)
    amount = db.Column(db.Float, default=0.0)
    status = db.Column(Enum(InvestmentStatus), default=InvestmentStatus.PROCESSING, nullable=False)
    deposit_type = db.Column(Enum(DepositType), default=DepositType.CASH, nullable=False)
    scheme = db.relationship("InvestmentScheme", back_populates="investments")
    user = db.relationship("User", back_populates="investments")
    wallets = db.relationship("Wallet", back_populates="investments")

    @classmethod
    def get_investment(cls, investment_id) -> 'Investment':
        invest: cls = cls.query.filter(cls.id == investment_id).first()
        if not invest:
            raise CustomException(message="No Investment found with the ID", status_code=404)
        return invest
