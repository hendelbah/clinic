from .basemodel import BaseModel, db


class Doctor(BaseModel):
    __tablename__ = 'doctor'

    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='SET NULL'), unique=True)
    area_id = db.Column(db.Integer, db.ForeignKey('area.id'), nullable=False)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    speciality = db.Column(db.String(100), nullable=False)
    experience = db.Column(db.Integer, nullable=False)
    appointment_price = db.Column(db.Integer, nullable=False)

    user = db.relationship('User', back_populates='doctor_account')
    area = db.relationship('Area', back_populates='doctors')
    booked_appointments = db.relationship('BookedAppointment', back_populates='doctor')
    fulfilled_appointments = db.relationship('FulfilledAppointment', back_populates='doctor')
