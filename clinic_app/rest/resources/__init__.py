"""
This package contains modules defining all API resources.

Modules:

- `base_api.py`: defines base resource classes with common routines
- `doctor_api.py`: defines resources for managing doctors
- `patient_api.py`: defines resources for managing patients
- `booked_appointment_api.py`: defines resources for managing booked appointments
- `served_appointment_api.py`: defines resources for managing served appointments
- `user_api.py`: defines resources for managing users
"""

from clinic_app.rest.resources.booked_appointment_api import \
    BookedAppointmentApi, BookedAppointmentsApi
from clinic_app.rest.resources.doctor_api import DoctorApi, DoctorsApi
from clinic_app.rest.resources.patient_api import PatientApi, PatientsApi
from clinic_app.rest.resources.served_appointment_api import \
    ServedAppointmentApi, ServedAppointmentsApi
from clinic_app.rest.resources.user_api import UserApi, UsersApi

__all__ = ['DoctorApi', 'DoctorsApi', 'BookedAppointmentApi', 'BookedAppointmentsApi', 'UsersApi',
           'PatientApi', 'PatientsApi', 'ServedAppointmentApi', 'ServedAppointmentsApi', 'UserApi']
