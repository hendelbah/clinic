"""
This module implements instance of fulfilled appointment in database
"""
from .basemodel import db, BaseModel
from datetime import date, time


class FulfilledAppointment(BaseModel):
    """
    FulfilledAppointment object stands for representation of data row in fulfilled_appointment table.
    It is for appointment archiving.
    """
    __tablename__ = 'fulfilled_appointment'
    __table_args__ = (
        db.UniqueConstraint('appointed_date', 'appointed_time'),
    )

    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id', ondelete='SET NULL'), index=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id', ondelete='SET NULL'), index=True)
    appointed_date = db.Column(db.Date, nullable=False)
    appointed_time = db.Column(db.Time, nullable=False)
    cancelled = db.Column(db.Boolean, nullable=False)
    conclusion = db.Column(db.String(511), nullable=False)
    prescription = db.Column(db.String(511), nullable=False)
    actual_cost = db.Column(db.Integer, nullable=False)

    patient = db.relationship('Patient', back_populates='fulfilled_appointments')
    doctor = db.relationship('Doctor', back_populates='fulfilled_appointments')

    def __init__(self, patient_id, doctor_id, appointed_date,
                 appointed_time, cancelled, cost, conclusion, prescription):
        """
        :param int patient_id: id of patient from patient table
        :param int doctor_id: id of doctor from doctor table
        :param date appointed_date: planned date of appointment
        :param time appointed_time: planned time of appointment
        :param bool cancelled: True if appointment didn't happen
        :param cost: overall cost for the appointment
        :param conclusion: doctor's conclusion
        :param prescription: prescription for the patient
        """
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointed_date = appointed_date
        self.appointed_time = appointed_time
        self.cancelled = cancelled
        if cancelled:
            self.actual_cost = 0
            self.conclusion = ''
            self.prescription = ''
        else:
            self.actual_cost = cost
            self.conclusion = conclusion
            self.prescription = prescription
