"""
This module implements instance of patient in database
"""
from datetime import date, datetime
from uuid import uuid4

from clinic_app import db


class Patient(db.Model):
    """
    Patient object stands for representation of data row in `patient` table.
    There is information about this clinic's patients
    """
    __tablename__ = 'patient'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uuid = db.Column(db.String(36), nullable=False, unique=True, index=True)
    phone_number = db.Column(db.String(20), nullable=False, unique=True, index=True)
    surname = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), nullable=False, index=True)
    name = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), nullable=False)
    patronymic = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    last_modified = db.Column(db.TIMESTAMP(timezone=True), default=datetime.utcnow,
                              onupdate=datetime.utcnow)

    def __init__(self, phone_number: str, surname: str, name: str, patronymic: str, birthday: date):
        """
        :param phone_number: patient's unique phone number
        :param surname: patient's surname
        :param name: patient's given name
        :param patronymic: patient's patronymic
        :param birthday: patient's date of birth
        """
        self.phone_number = phone_number
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.birthday = birthday
        self.uuid = str(uuid4())

    def __repr__(self):
        keys = ('id', 'surname', 'name', 'patronymic')
        values = (f"{key}={getattr(self, key)!r}" for key in keys)
        return f'<Patient({", ".join(values)})>'
