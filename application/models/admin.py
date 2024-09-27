from application import db
from application.Mixins.GenericMixins import GenericMixin


class AdminWallets(db.Model, GenericMixin):
    id = db.Column(db.Integer, primary_key=True)
    coin_id = db.Column(db.Integer, db.ForeignKey('coins.id'))
    wallet_id = db.Column(db.Text, nullable=True)
    coins = db.relationship("Coins", back_populates='admin_wallets')
