"""
This module implements instance of fulfilled appointment in database
"""
from clinic_app.models.booked_appointment import db, BaseModel, BookedAppointment


class FulfilledAppointment(BaseModel):
    """
    FulfilledAppointment object stands for representation of data row in `fulfilled_appointment` table.
    There are appointments that took place.
    """
    __tablename__ = 'fulfilled_appointment'
    __table_args__ = (
        db.UniqueConstraint('doctor_id', 'date', 'time'),
        db.UniqueConstraint('patient_id', 'date', 'time'),
    )

    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id', ondelete='SET NULL'), index=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id', ondelete='SET NULL'), index=True)
    date = db.Column(db.Date, nullable=False, index=True)
    time = db.Column(db.Time, nullable=False)
    conclusion = db.Column(db.String(511), nullable=False)
    prescription = db.Column(db.String(511), nullable=False)
    bill = db.Column(db.Integer, nullable=False)

    patient = db.relationship('Patient', back_populates='fulfilled_appointments')
    doctor = db.relationship('Doctor', back_populates='fulfilled_appointments')

    def __init__(self, patient_id, doctor_id, date_, time_, conclusion, prescription, bill):
        """
        :param int patient_id: id of patient from patient table
        :param int doctor_id: id of doctor from doctor table
        :param date date_: date of appointment
        :param time time_: time of appointment
        :param str conclusion: doctor's conclusion
        :param str prescription: prescription for the patient
        :param str bill: overall cost of doctor's services
        """
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date_
        self.time = time_
        self.conclusion = conclusion
        self.prescription = prescription
        self.bill = bill
