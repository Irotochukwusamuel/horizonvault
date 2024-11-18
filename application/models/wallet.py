from typing import List

from application import db
from application.Mixins.GenericMixins import GenericMixin
import os
import hashlib
from exceptions.codes import ExceptionCode
from exceptions.custom_exception import CustomException


class Coins(db.Model, GenericMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=True, unique=True)
    symbol = db.Column(db.Text, nullable=True, unique=True)
    logo = db.Column(db.Text, nullable=True, unique=True)
    rate = db.Column(db.Float, nullable=True, default=1)
    wallets = db.relationship("Wallet", back_populates='coins')
    transactions = db.relationship("Transactions", back_populates='coins')
    admin_wallets = db.relationship("AdminWallets", back_populates='coins')

    @classmethod
    def get_coin_by_name(cls, name) -> 'Coins':
        coin = cls.query.filter_by(name=name).first()
        if not coin:
            raise CustomException(message="Coin not found", status_code=404)
        return coin


class Wallet(db.Model, GenericMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    coin_id = db.Column(db.Integer, db.ForeignKey('coins.id'))
    wallet_id = db.Column(db.Text, nullable=True, unique=True)
    balance = db.Column(db.Float, default=0.0)
    user = db.relationship("User", back_populates='wallets')
    is_active = db.Column(db.Boolean, default=True)
    coins = db.relationship("Coins", back_populates='wallets')
    investments = db.relationship("Investment", back_populates='wallets')

    @classmethod
    def generate_wallets(cls, user) -> bool:
        coins: List[Coins] = Coins.query.all()
        for coin in coins:
            try:
                private_key = os.urandom(32)
                w_exists = cls.query.filter(cls.coin_id == coin.id, cls.user == user).first()
                if not w_exists:
                    public_key = hashlib.sha256(private_key).hexdigest()
                    wallet_id = hashlib.new('ripemd160', public_key.encode()).hexdigest()
                    w = cls(user=user, coins=coin, wallet_id=wallet_id)
                    w.save(refresh=True)
            except Exception:
                continue
        return True
