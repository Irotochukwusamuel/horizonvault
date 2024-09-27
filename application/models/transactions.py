from application import db
from application.Mixins.GenericMixins import GenericMixin
import enum
from sqlalchemy import Enum


class TransactionStatus(enum.Enum):
    PROCESSING = 'processing'
    APPROVED = 'approved'
    FAILED = 'failed'


class TransactionType(enum.Enum):
    TRANSACT_B2C = 'transact_b2c'
    TRANSACT_C2C = 'transact_c2c'
    TRANSACT_C2B = 'transact_c2b'


# Define the Transactions model
class Transactions(db.Model, GenericMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True, index=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True, index=True)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True, index=True)
    coin_id = db.Column(db.Integer, db.ForeignKey('coins.id'))
    amount = db.Column(db.Float, default=0.0)
    receiver_address = db.Column(db.Text, nullable=True)
    receiver_fee = db.Column(db.Float, default=0.0)
    sender_fee = db.Column(db.Float, default=0.0)
    status = db.Column(Enum(TransactionStatus), default=TransactionStatus.PROCESSING, nullable=False)
    network = db.Column(db.Text, nullable=True)
    transaction_type = db.Column(Enum(TransactionType), nullable=False)
    sender_user = db.relationship("User", back_populates='sent_transactions', foreign_keys=[sender_id])
    receiver_user = db.relationship("User", back_populates='received_transactions', foreign_keys=[receiver_id])
    coins = db.relationship("Coins", back_populates='transactions')
    user = db.relationship("User", back_populates="transactions", foreign_keys=[user_id])
