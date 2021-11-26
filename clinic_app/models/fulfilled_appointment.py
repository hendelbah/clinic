from .basemodel import db, BaseModel


class FulfilledAppointment(BaseModel):
    __tablename__ = 'fulfilled_appointment'
    __table_args__ = (
        db.UniqueConstraint('date', 'time'),
    )
    patient_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='SET NULL'))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id', ondelete='SET NULL'))
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    cancelled = db.Column(db.Boolean, default=True)
    conclusion = db.Column(db.String(255), default=None)
    prescription = db.Column(db.String(511), default=None)

    patient = db.relationship('Patient', back_populates='fulfilled_appointments')
    doctor = db.relationship('Doctor', back_populates='fulfilled_appointments')
