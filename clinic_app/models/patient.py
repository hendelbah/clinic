from .basemodel import BaseModel, db


class Patient(BaseModel):
    __tablename__ = 'patient'

    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='SET NULL'), unique=True)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    birthday = db.Column(db.Date, nullable=False)

    user = db.relationship('User', back_populates='patient_account')
    booked_appointments = db.relationship('BookedAppointment', back_populates='patient')
    fulfilled_appointments = db.relationship('FulfilledAppointment', back_populates='patient')
