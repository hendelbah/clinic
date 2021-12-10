"""
This package contains modules defining all API resources.

Modules:

- `base_api.py`: defines base resource classes with common routines
- `doctor_api.py`: defines resources for managing doctors
- `patient_api.py`: defines resources for managing patients
- `appointment_api.py`: defines resources for managing appointments
- `user_api.py`: defines resources for managing users
"""

from clinic_app.rest.resources.appointment_api import AppointmentApi, AppointmentsApi, StatisticsApi
from clinic_app.rest.resources.doctor_api import DoctorApi, DoctorsApi
from clinic_app.rest.resources.patient_api import PatientApi, PatientsApi
from clinic_app.rest.resources.user_api import UserApi, UsersApi

__all__ = ['DoctorApi', 'DoctorsApi', 'UsersApi', 'PatientApi', 'PatientsApi',
           'AppointmentApi', 'AppointmentsApi', 'UserApi', 'StatisticsApi']
