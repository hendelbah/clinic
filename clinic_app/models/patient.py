"""
This module implements instance of patient in database
"""
from .basemodel import BaseModel, db


class Patient(BaseModel):
    __tablename__ = 'patient'

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, unique=True)
    phone_number = db.Column(db.String(20), nullable=False, unique=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    third_name = db.Column(db.String(40), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    time_registered = db.Column(db.DateTime, server_default=db.func.now())

    user = db.relationship('User', back_populates='patient_account')
    booked_appointments = db.relationship('BookedAppointment', back_populates='patient')
    fulfilled_appointments = db.relationship('FulfilledAppointment', back_populates='patient')

    def __init__(self, user_id, phone_number, first_name, last_name, third_name, birthday):
        """
        :param user_id: corresponding user id from user table
        :param phone_number: patient's unique phone number
        :param first_name: patient's first name
        :param last_name: patient's last name
        :param third_name: patient's third name
        :param birthday: patient's appointed_date of birth
        """
        self.user_id = user_id
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.third_name = third_name
        self.birthday = birthday
