"""
This package contains modules defining REST APIs for Doctor, Patient, BookedAppointment,
ServedAppointment and User models. Respective API endpoints are initialized here and
everything is linked to `api_blueprint`:

Subpackages:

- `resources`: defines all REST API resources

Modules:

- `schemas.py`: contains Marshmallow schemas for serialization/deserialization of db models
"""
from flask import Blueprint
from flask_restful import Api

from clinic_app.rest.resources import (
    ServedAppointmentApi, ServedAppointmentsApi, BookedAppointmentApi, BookedAppointmentsApi,
    DoctorApi, DoctorsApi, PatientApi, PatientsApi, UserApi, UsersApi)

api_blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(api_blueprint)

api.add_resource(UserApi, '/users/<int:id>', endpoint='user')
api.add_resource(UsersApi, '/users', endpoint='users')
api.add_resource(DoctorApi, '/doctors/<int:id>', endpoint='doctor')
api.add_resource(DoctorsApi, '/doctors', endpoint='doctors')
api.add_resource(PatientApi, '/patients/<int:id>', endpoint='patient')
api.add_resource(PatientsApi, '/patients', endpoint='patients')
api.add_resource(BookedAppointmentApi, '/booked_appointments/<int:id>',
                 endpoint='booked_appointment')
api.add_resource(BookedAppointmentsApi, '/booked_appointments', endpoint='booked_appointments')
api.add_resource(ServedAppointmentApi, '/served_appointments/<int:id>',
                 endpoint='served_appointment')
api.add_resource(ServedAppointmentsApi, '/served_appointments', endpoint='served_appointments')
