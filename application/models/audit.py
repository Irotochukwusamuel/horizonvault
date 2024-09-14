from application import db
from application.Mixins.GenericMixins import GenericMixin


class Audit(db.Model, GenericMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    action = db.Column(db.String(350), nullable=True)
    data = db.Column(db.JSON(none_as_null=True), nullable=True)
    user = db.relationship("User", back_populates='audits')

    @classmethod
    def add_audit(cls, action: str, user, Additional_data: dict):
        try:
            add_audit = Audit(user=user, action=action, data=Additional_data)
            add_audit.save(refresh=True)
        except Exception as e:
            raise e

