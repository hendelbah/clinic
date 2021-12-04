from flask import Blueprint
from flask_restful import Api

from clinic_app.rest.resources import (ServedAppointments, ServedAppointmentsList,
                                       BookedAppointments, BookedAppointmentsList, Doctors,
                                       DoctorsList, Patients, PatientsList, Statistics)

api_blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(api_blueprint)

api.add_resource(Doctors, '/doctors/<int:id>')
api.add_resource(DoctorsList, '/doctors')
api.add_resource(Patients, '/patients/<int:id>')
api.add_resource(PatientsList, '/patients')
api.add_resource(BookedAppointments, '/booked_appointments/<int:id>')
api.add_resource(BookedAppointmentsList, '/booked_appointments')
api.add_resource(ServedAppointments, '/served_appointments/<int:id>')
api.add_resource(ServedAppointmentsList, '/served_appointments')
api.add_resource(Statistics, '/statistics')
