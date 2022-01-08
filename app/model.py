from app import db
from sqlalchemy_utils.types.choice import ChoiceType
from flask_restful_swagger import swagger

# Profile Model

class ProfileModel(db.Model):

    TYPES = [
        (u'ACTIVE', u'ACTIVE'),
        (u'PAUSED', u'PAUSED')
    ]
    __tablename__ = "profile"

    id = db.Column(db.Integer, primary_key = True, nullable=False,  autoincrement=True)
    name = db.Column(db.String(25), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    status = db.Column(ChoiceType(TYPES), server_default="ACTIVE")

    def __repr__(self):
        return self.name

swagger.add_model(ProfileModel)