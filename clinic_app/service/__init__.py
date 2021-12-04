"""
Package contain service classes and functions to work with database
"""
from clinic_app.service.base_service import BaseService, handle_db_errors
from clinic_app.service.doctor_service import DoctorService
from clinic_app.service.patient_service import PatientService
from clinic_app.service.appointment_service import \
    BookedAppointmentService, FulfilledAppointmentService
