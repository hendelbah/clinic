"""
Package contain helper service classes and functions to work with database.

Subpackages:

- `population`: contains tools for populating database with test data

Modules:

- `base_service.py`: defines base service classes with common routines
- `doctor_service.py`: defines service class for querying Doctor model
- `patient_service.py`: defines service class for querying Patient model
- `booked_app_service.py`: defines service class for querying BookedAppointments model
- `served_app_service.py`: defines service class for querying ServedAppointments model
- `user_service.py`: defines service class for querying User model
"""
from clinic_app.service.base_service import BaseService
from clinic_app.service.booked_app_service import BookedAppointmentService
from clinic_app.service.doctor_service import DoctorService
from clinic_app.service.patient_service import PatientService
from clinic_app.service.served_app_service import ServedAppointmentService
from clinic_app.service.user_service import UserService

__all__ = ['BaseService', 'DoctorService', 'PatientService',
           'BookedAppointmentService', 'ServedAppointmentService', 'UserService']
