"""
This module implements instance of booked appointment in database
"""
from datetime import date as date_, time as time_

from clinic_app import db


# pylint: disable=redefined-builtin
class BookedAppointment(db.Model):
    """
    BookedAppointment object stands for representation of data row in `booked_appointment` table.
    There is data on doctors appointments booked for patients
    """
    __tablename__ = 'booked_appointment'
    __table_args__ = (
        db.UniqueConstraint('doctor_id', 'date', 'time'),
        db.UniqueConstraint('patient_id', 'date', 'time'),
    )

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id', ondelete='CASCADE'),
                          nullable=False, index=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id', ondelete='CASCADE'),
                           nullable=False, index=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)

    patient = db.relationship('Patient', back_populates='booked_appointments')
    doctor = db.relationship('Doctor', back_populates='booked_appointments')

    def __init__(self, patient_id: int, doctor_id: int, date: date_, time: time_, id: int = None):
        """
        :param patient_id: id of patient from `patient` table
        :param doctor_id: id of doctor from `doctor` table
        :param date: planned date of appointment
        :param time: planned time of appointment
        :param id: id of booked appointment
        """
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time
        self.id = id

    def __repr__(self):
        keys = ('id', 'patient_id', 'doctor_id', 'date', 'time')
        values = (f"{key}={getattr(self, key)!r}" for key in keys)
        return f'<BookedAppointment({", ".join(values)})>'
