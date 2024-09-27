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
    transactions = db.relationship("Transactions", back_populates='coins')
    admin_wallets = db.relationship("AdminWallets", back_populates='coins')


class Wallet(db.Model, GenericMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    coin_id = db.Column(db.Integer, db.ForeignKey('coins.id'))
    wallet_id = db.Column(db.Text, nullable=True, unique=True)
    balance = db.Column(db.Float, default=0.0)
    user = db.relationship("User", back_populates='wallets')
    is_active = db.Column(db.Boolean, default=True)
    coins = db.relationship("Coins", back_populates='wallets')

    @classmethod
    def generate_wallets(cls, user) -> bool:
        coins = Coins.query.all()
        for coin in coins:
            try:
                private_key = os.urandom(32)

                public_key = hashlib.sha256(private_key).hexdigest()
                wallet_id = hashlib.new('ripemd160', public_key.encode()).hexdigest()
                w = Wallet(user=user, coins=coin, wallet_id=wallet_id)
                w.save(refresh=True)
            except Exception:
                continue
        return True
