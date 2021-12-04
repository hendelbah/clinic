from flask_restful import Api
from flask import Blueprint
from clinic_app.rest.resources import Doctors, DoctorsList, Patients, PatientsList, \
    BookedAppointments, BookedAppointmentsList, FulfilledAppointments, FulfilledAppointmentsList

api_blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(api_blueprint)

api.add_resource(Doctors, '/doctors/<int:id>')
api.add_resource(DoctorsList, '/doctors')
api.add_resource(Patients, '/patients/<int:id>')
api.add_resource(PatientsList, '/patients')
api.add_resource(BookedAppointments, '/booked_appointments/<int:id>')
api.add_resource(BookedAppointmentsList, '/booked_appointments')
api.add_resource(FulfilledAppointments, '/fulfilled_appointments/<int:id>')
api.add_resource(FulfilledAppointmentsList, '/fulfilled_appointments')
