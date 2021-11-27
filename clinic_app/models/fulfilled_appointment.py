from .basemodel import db, BaseModel


class FulfilledAppointment(BaseModel):
    __tablename__ = 'fulfilled_appointment'
    __table_args__ = (
        db.UniqueConstraint('date', 'time'),
    )
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id', ondelete='SET NULL'), index=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id', ondelete='SET NULL'), index=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    cancelled = db.Column(db.Boolean, nullable=False)
    conclusion = db.Column(db.String(255))
    prescription = db.Column(db.String(511))
    actual_cost = db.Column(db.Integer, nullable=False)

    patient = db.relationship('Patient', back_populates='fulfilled_appointments')
    doctor = db.relationship('Doctor', back_populates='fulfilled_appointments')
