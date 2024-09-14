from application import db
from application.Mixins.GenericMixins import GenericMixin


class State(db.Model, GenericMixin):
    id = db.Column(db.Integer, primary_key=True)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    state_name = db.Column(db.String(250), nullable=True, unique=True)
    country = db.relationship("Country", back_populates='states')
