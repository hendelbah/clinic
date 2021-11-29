"""
This module implements instance of patient in database
"""
from datetime import date
from clinic_app.models.basemodel import BaseModel, db


class Patient(BaseModel):
    """
    Patient object stands for representation of data row in `patient` table.
    There is information about this clinic's patients
    """
    __tablename__ = 'patient'

    phone_number = db.Column(db.String(20), nullable=False, unique=True, index=True)
    email = db.Column(db.String(80), unique=True, index=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False, index=True)
    third_name = db.Column(db.String(40), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    time_registered = db.Column(db.DateTime, server_default=db.func.now())

    booked_appointments = db.relationship('BookedAppointment', back_populates='patient')
    fulfilled_appointments = db.relationship('FulfilledAppointment', back_populates='patient')

    def __init__(self, phone_number, first_name, last_name, third_name, birthday, email=None):
        """
        :param str phone_number: patient's unique phone number
        :param str first_name: patient's given name
        :param str last_name: patient's surname
        :param str third_name: patient's third name
        :param date birthday: patient's date of birth
        :param str email: patient's email
        """
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.third_name = third_name
        self.birthday = birthday
        self.email = email
