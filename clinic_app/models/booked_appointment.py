"""
This module implements instance of booked appointment in database
"""
from datetime import date, time
from clinic_app.models.basemodel import BaseModel, db


class BookedAppointment(BaseModel):
    """
    BookedAppointment object stands for representation of data row in `booked_appointment` table.
    There is data on doctors appointments booked for patients
    """
    __tablename__ = 'booked_appointment'
    __table_args__ = (
        db.UniqueConstraint('doctor_id', 'date', 'time'),
        db.UniqueConstraint('patient_id', 'date', 'time'),
    )

    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id', ondelete='CASCADE'), nullable=False, index=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id', ondelete='CASCADE'), nullable=False, index=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)

    patient = db.relationship('Patient', back_populates='booked_appointments')
    doctor = db.relationship('Doctor', back_populates='booked_appointments')

    def __init__(self, patient_id, doctor_id, date_, time_):
        """
        :param int patient_id: id of patient from `patient` table
        :param int doctor_id: id of doctor from `doctor` table
        :param date date_: planned date of appointment
        :param time time_: planned time of appointment
        """
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date_
        self.time = time_
