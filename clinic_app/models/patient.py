from basemodel import BaseModel, db


class Patient(BaseModel):
    __tablename__ = 'patient'
    phone_number = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    birth_date = db.Column(db.Date, nullable=False)

