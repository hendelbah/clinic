"""
Package contains all sqlalchemy database models
"""
from clinic_app.models.basemodel import BaseModel
from clinic_app.models.doctor import Doctor
from clinic_app.models.patient import Patient
from clinic_app.models.user import User
from clinic_app.models.booked_appointment import BookedAppointment
from clinic_app.models.fulfilled_appointment import FulfilledAppointment

__all__ = [BaseModel, BookedAppointment, Doctor, FulfilledAppointment, Patient, User]
