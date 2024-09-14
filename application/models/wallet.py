from application import db
from application.Mixins.GenericMixins import GenericMixin
import os
import hashlib


class Wallet(db.Model, GenericMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    wallet_type = db.Column(db.String(350), nullable=True)
    wallet_name = db.Column(db.String(350), nullable=True)
    wallet_id = db.Column(db.Text, nullable=True, unique=True)
    user = db.relationship("User", back_populates='wallets')
    is_active = db.Column(db.Boolean, default=True)

    @classmethod
    def generate_wallet_id(cls) -> str:
        private_key = os.urandom(32)

        public_key = hashlib.sha256(private_key).hexdigest()

        wallet_id = hashlib.new('ripemd160', public_key.encode()).hexdigest()

        return wallet_id

    @classmethod
    def create_wallet(cls, wallet_type, wallet_name, user) -> bool:
        create = Wallet(wallet_type=wallet_type, wallet_name=wallet_name, wallet_id=cls.generate_wallet_id(), user=user)
        create.save(refresh=True)
        return True

