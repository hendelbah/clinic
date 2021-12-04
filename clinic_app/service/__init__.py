"""
Package contain service classes and functions to work with database
"""
from clinic_app.service.base_service import BaseService, handle_db_errors
from clinic_app.service.doctor import DoctorService
from clinic_app.service.patient import PatientService
from clinic_app.service.booked_appointment import BookedAppointmentService
from clinic_app.service.served_appointment import ServedAppointmentService

__all__ = ['BaseService', 'handle_db_errors', 'DoctorService', 'PatientService',
           'BookedAppointmentService', 'ServedAppointmentService']
