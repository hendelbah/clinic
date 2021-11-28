"""
This module implements instance of doctor in database
"""
from .basemodel import BaseModel, db


class Doctor(BaseModel):
    """
    Doctor object stands for representation of data row in doctor table.
    It represents a doctor's account for registered user
    """
    __tablename__ = 'doctor'

    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'),
                        nullable=False, unique=True, index=True)
    medical_area_id = db.Column(db.Integer, db.ForeignKey('medical_area.id'), nullable=False, index=True)
    phone_number = db.Column(db.String(20), nullable=False, unique=True)
    full_name = db.Column(db.String(127), nullable=False)
    speciality = db.Column(db.String(127), nullable=False)
    about_self = db.Column(db.String(1023), nullable=False)
    appointment_basic_price = db.Column(db.Integer, nullable=False)
    time_hired = db.Column(db.DateTime, server_default=db.func.now())
    time_quit = db.Column(db.DateTime, default=None)

    user = db.relationship('User', back_populates='doctor_account')
    medical_area = db.relationship('MedicalArea', back_populates='doctors')
    booked_appointments = db.relationship('BookedAppointment', back_populates='doctor')
    fulfilled_appointments = db.relationship('FulfilledAppointment', back_populates='doctor')

    def __init__(self, user_id, area_id, phone_number, full_name, speciality, about_self='', appointment_price=300):
        """
        :param user_id: corresponding user id from user table
        :param area_id: area id from medical_area table
        :param phone_number: doctor's own unique phone number
        :param full_name: doctor's full name
        :param speciality: doctor's speciality
        :param about_self: some information about doctor to display on site
        :param appointment_price: basic appointment price for the doctor
        """
        self.user_id = user_id
        self.area_id = area_id
        self.phone_number = phone_number
        self.full_name = full_name
        self.speciality = speciality
        self.about_self = about_self
        self.appointment_basic_price = appointment_price
