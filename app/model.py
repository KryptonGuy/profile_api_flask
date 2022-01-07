from app import db
from sqlalchemy_utils.types.choice import ChoiceType

# Profile Model

class ProfileModel(db.Model):
    TYPES = [
        (u'Active', u'Active'),
        (u'Paused', u'Paused')
    ]
    __tablename__ = "profile"

    id = db.Column(db.Integer, primary_key = True, nullable=False,  autoincrement=True)
    name = db.Column(db.String(25), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    status = db.Column(ChoiceType(TYPES), server_default="Active")

    def __repr__(self):
        return self.name