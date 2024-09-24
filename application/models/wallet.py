from application import db
from application.Mixins.GenericMixins import GenericMixin
import os
import hashlib


class Coins(db.Model, GenericMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=True, unique=True)
    symbol = db.Column(db.Text, nullable=True, unique=True)
    logo = db.Column(db.Text, nullable=True, unique=True)
    wallets = db.relationship("Wallet", back_populates='coins')


class Wallet(db.Model, GenericMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    coin_id = db.Column(db.Integer, db.ForeignKey('coins.id'))
    wallet_id = db.Column(db.Text, nullable=True, unique=True)
    user = db.relationship("User", back_populates='wallets')
    is_active = db.Column(db.Boolean, default=True)
    coins = db.relationship("Coins", back_populates='wallets')

    @classmethod
    def generate_wallet_id(cls) -> str:
        private_key = os.urandom(32)

        public_key = hashlib.sha256(private_key).hexdigest()

        wallet_id = hashlib.new('ripemd160', public_key.encode()).hexdigest()

        return wallet_id
