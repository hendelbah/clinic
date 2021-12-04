"""
This module implements instance of served appointment in database
"""
from datetime import date as date_, time as time_

from clinic_app.models.basemodel import db, BaseModel


# pylint: disable=redefined-builtin
class ServedAppointment(BaseModel):
    """
    ServedAppointment object stands for representation of data row in
    `served_appointment` table. Table stores appointments that took place.
    """
    __tablename__ = 'served_appointment'
    __table_args__ = (
        db.UniqueConstraint('doctor_id', 'date', 'time'),
        db.UniqueConstraint('patient_id', 'date', 'time'),
    )

    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id', ondelete='SET NULL'),
                           index=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id', ondelete='SET NULL'),
                          index=True)
    date = db.Column(db.Date, nullable=False, index=True)
    time = db.Column(db.Time, nullable=False)
    conclusion = db.Column(db.String(511), nullable=False)
    prescription = db.Column(db.String(511), nullable=False)
    bill = db.Column(db.Integer, nullable=False)

    patient = db.relationship('Patient', back_populates='served_appointments')
    doctor = db.relationship('Doctor', back_populates='served_appointments')

    def __init__(self, patient_id: int, doctor_id: int, date: date_, time: time_,
                 conclusion: str, prescription: str, bill: str, id: int = None):
        """
        :param patient_id: id of patient from patient table
        :param doctor_id: id of doctor from doctor table
        :param date: date of appointment
        :param time: time of appointment
        :param conclusion: doctor's conclusion
        :param prescription: prescription for the patient
        :param bill: overall cost of doctor's services
        :param id: id of booked appointment
        """
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time
        self.conclusion = conclusion
        self.prescription = prescription
        self.bill = bill
        self.id = id
