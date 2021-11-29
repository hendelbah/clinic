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
    surname = db.Column(db.String(40), nullable=False, index=True)
    name = db.Column(db.String(40), nullable=False)
    patronymic = db.Column(db.String(40), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    time_registered = db.Column(db.DateTime, server_default=db.func.now())

    booked_appointments = db.relationship('BookedAppointment', back_populates='patient')
    fulfilled_appointments = db.relationship('FulfilledAppointment', back_populates='patient')

    def __init__(self, phone_number, surname, name, patronymic, birthday):
        """
        :param str phone_number: patient's unique phone number
        :param str surname: patient's surname
        :param str name: patient's given name
        :param str patronymic: patient's patronymic
        :param date birthday: patient's date of birth
        """
        self.phone_number = phone_number
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.birthday = birthday
