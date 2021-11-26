from .basemodel import BaseModel, db
from .area import Area
from .doctor import Doctor
from .patient import Patient
from .user import User
from .booked_appointment import BookedAppointment
from .fulfilled_appointment import FulfilledAppointment

__all__ = ['Area', 'BaseModel', 'BookedAppointment', 'Doctor', 'FulfilledAppointment', 'Patient', 'User', 'db']
