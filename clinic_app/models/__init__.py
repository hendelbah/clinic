"""
Package contains all sqlalchemy database models
"""
from clinic_app.models.basemodel import BaseModel
from clinic_app.models.booked_appointment import BookedAppointment
from clinic_app.models.doctor import Doctor
from clinic_app.models.patient import Patient
from clinic_app.models.served_appointment import ServedAppointment
from clinic_app.models.user import User

__all__ = ['BaseModel', 'BookedAppointment', 'Doctor', 'ServedAppointment', 'Patient', 'User']
