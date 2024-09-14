from application import db
from application.Mixins.GenericMixins import GenericMixin
import random
import string
import hashlib


class Referral(db.Model, GenericMixin):
    id = db.Column(db.Integer, primary_key=True)
    referrer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    referred_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    referrer = db.relationship("User", foreign_keys=[referrer_id], back_populates="referrals_made")
    referred = db.relationship("User", foreign_keys=[referred_id], back_populates="referrals_received")

    @classmethod
    def generate_referral_id(cls, user_id: int) -> str:
        # Use user_id as a base for the referral ID
        base_id = str(user_id)

        # Generate a random string
        random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        # Combine base_id and random_part
        raw_referral = f"{base_id}{random_part}"

        # Optional: Hash the combined string for additional uniqueness and to limit length
        referral_hash = hashlib.sha256(raw_referral.encode()).hexdigest()[:10]

        return referral_hash
