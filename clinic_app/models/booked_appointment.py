"""
This module implements instance of booked appointment in database
"""
from .basemodel import BaseModel, db
from datetime import date, time


class BookedAppointment(BaseModel):
    """
    BookedAppointment object stands for representation of data row in booked_appointment table.
    """
    __tablename__ = 'booked_appointment'
    __table_args__ = (
        db.UniqueConstraint('appointed_date', 'appointed_time'),
    )

    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id', ondelete='CASCADE'), index=True, nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id', ondelete='CASCADE'), index=True, nullable=False)
    appointed_date = db.Column(db.Date, nullable=False)
    appointed_time = db.Column(db.Time, nullable=False)

    patient = db.relationship('Patient', back_populates='booked_appointments')
    doctor = db.relationship('Doctor', back_populates='booked_appointments')

    def __init__(self, patient_id, doctor_id, appointed_date, appointed_time):
        """
        :param int patient_id: id of patient from patient table
        :param int doctor_id: id of doctor from doctor table
        :param date appointed_date: planned date of appointment
        :param time appointed_time: planned time of appointment
        """
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointed_date = appointed_date
        self.appointed_time = appointed_time
