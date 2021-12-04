from clinic_app.rest.resources.booked_appointments import \
    BookedAppointments, BookedAppointmentsList
from clinic_app.rest.resources.doctors import Doctors, DoctorsList
from clinic_app.rest.resources.patients import Patients, PatientsList
from clinic_app.rest.resources.served_appointments import \
    ServedAppointments, ServedAppointmentsList, Statistics

__all__ = ['Doctors', 'DoctorsList', 'Patients', 'PatientsList', 'BookedAppointments',
           'BookedAppointmentsList', 'ServedAppointments', 'ServedAppointmentsList', 'Statistics']
