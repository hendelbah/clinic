"""
This module implements instance of fulfilled appointment in database
"""
from datetime import date, time
from clinic_app.models.basemodel import db, BaseModel


class FulfilledAppointment(BaseModel):
    """
    FulfilledAppointment object stands for representation of data row in `fulfilled_appointment` table.
    There is archived appointments that took place(or were cancelled).
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
    cancelled = db.Column(db.Boolean, nullable=False)
    conclusion = db.Column(db.String(511), nullable=False)
    prescription = db.Column(db.String(511), nullable=False)
    bill = db.Column(db.Integer, nullable=False)

    patient = db.relationship('Patient', back_populates='fulfilled_appointments')
    doctor = db.relationship('Doctor', back_populates='fulfilled_appointments')

    def __init__(self, patient_id, doctor_id, date_, time_, cancelled, conclusion='', prescription='', bill=0):
        """
        :param int patient_id: id of patient from patient table
        :param int doctor_id: id of doctor from doctor table
        :param date date_: date of appointment
        :param time time_: time of appointment
        :param bool cancelled: True if appointment didn't happen
        :param str conclusion: doctor's conclusion
        :param str prescription: prescription for the patient
        :param str bill: overall cost for doctor's services
        """
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date_
        self.time = time_
        self.cancelled = cancelled
        self.conclusion = conclusion
        self.prescription = prescription
        self.bill = bill
