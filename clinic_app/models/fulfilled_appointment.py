"""
This module implements instance of fulfilled appointment in database
"""
from .basemodel import db, BaseModel
from .booked_appointment import BookedAppointment


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
    appointed_date = db.Column(db.Date, nullable=False, index=True)
    appointed_time = db.Column(db.Time, nullable=False)
    cancelled = db.Column(db.Boolean, nullable=False)
    conclusion = db.Column(db.String(511), nullable=False)
    prescription = db.Column(db.String(511), nullable=False)
    actual_cost = db.Column(db.Integer, nullable=False)

    patient = db.relationship('Patient', back_populates='fulfilled_appointments')
    doctor = db.relationship('Doctor', back_populates='fulfilled_appointments')

    def __init__(self, booked_appointment, cancelled, cost, conclusion, prescription):
        """
        :param BookedAppointment booked_appointment: BookedAppointment instance as a source
        :param bool cancelled: True if appointment didn't happen
        :param str cost: overall cost for the appointment
        :param str conclusion: doctor's conclusion
        :param str prescription: prescription for the patient
        """
        self.patient_id = booked_appointment.patient_id
        self.doctor_id = booked_appointment.doctor_id
        self.appointed_date = booked_appointment.appointed_date
        self.appointed_time = booked_appointment.appointed_time
        self.cancelled = cancelled
        self.actual_cost = cost
        self.conclusion = conclusion
        self.prescription = prescription
