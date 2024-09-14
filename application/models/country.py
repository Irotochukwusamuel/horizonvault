from application import db
from application.Mixins.GenericMixins import GenericMixin


class Country(db.Model, GenericMixin):
    id = db.Column(db.Integer, primary_key=True)
    country_code = db.Column(db.String(250), nullable=True)
    country_name = db.Column(db.String(250), nullable=True, unique=True)
    country_currency = db.Column(db.String(250), nullable=True)
    country_capital = db.Column(db.String(250), nullable=True)
    states = db.relationship("State", back_populates='country')



