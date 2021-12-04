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

    booked_appointments = db.relationship('BookedAppointment', back_populates='patient')
    served_appointments = db.relationship('ServedAppointment', back_populates='patient')

    def __init__(self, phone_number: str, surname: str, name: str,
                 patronymic: str, birthday: date, id: int = None):
        """
        :param phone_number: patient's unique phone number
        :param surname: patient's surname
        :param name: patient's given name
        :param patronymic: patient's patronymic
        :param birthday: patient's date of birth
        :param id: patient's id
        """
        self.phone_number = phone_number
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.birthday = birthday
        self.id = id
