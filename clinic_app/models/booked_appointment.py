from .basemodel import BaseModel, db


class BookedAppointment(BaseModel):
    __tablename__ = 'booked_appointment'
    __table_args__ = (
        db.UniqueConstraint('date', 'time'),
    )
    patient_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), index=True, nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id', ondelete='CASCADE'), index=True, nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)

    patient = db.relationship('Patient', back_populates='booked_appointments')
    doctor = db.relationship('Doctor', back_populates='booked_appointments')
