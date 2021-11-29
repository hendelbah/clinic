"""
Package contains all sqlalchemy database models
"""
from clinic_app.models.basemodel import BaseModel, db
from clinic_app.models.medical_area import MedicalArea
from clinic_app.models.doctor import Doctor
from clinic_app.models.patient import Patient
from clinic_app.models.user import User
from clinic_app.models.booked_appointment import BookedAppointment
from clinic_app.models.fulfilled_appointment import FulfilledAppointment

__all__ = ['BaseModel', 'BookedAppointment', 'Doctor', 'FulfilledAppointment', 'MedicalArea', 'Patient', 'User', 'db']
