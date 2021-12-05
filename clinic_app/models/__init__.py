"""
Package contains modules defining SQLAlchemy models

Modules:

- `doctor.py`: defines model representing doctors
- `patient.py`: defines model representing doctors
- `user.py`: defines model representing users
- `booked_appointment.py`: defines model representing appointments booked
- `served_appointment.py`: defines model representing appointments that took place
"""
from clinic_app.models.booked_appointment import BookedAppointment
from clinic_app.models.doctor import Doctor
from clinic_app.models.patient import Patient
from clinic_app.models.served_appointment import ServedAppointment
from clinic_app.models.user import User

__all__ = ['BookedAppointment', 'Doctor', 'ServedAppointment', 'Patient', 'User']
