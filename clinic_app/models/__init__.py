from .basemodel import BaseModel, db
from .medical_area import MedicalArea
from .doctor import Doctor
from .patient import Patient
from .user import User
from .booked_appointment import BookedAppointment
from .fulfilled_appointment import FulfilledAppointment

__all__ = ['BaseModel', 'BookedAppointment', 'Doctor', 'FulfilledAppointment', 'MedicalArea', 'Patient', 'User', 'db']
