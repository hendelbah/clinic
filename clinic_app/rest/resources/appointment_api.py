"""
Served appointments REST API, this module defines the following classes:

- `AppointmentMixIn`: appointment API mixin class
- `AppointmentsApi`: appointments collection API resource class
- `AppointmentApi`: appointment API resource class
- `StatisticsApi`: API resource class for statistics on appointments
"""
from datetime import date

from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from clinic_app.rest.resources.base_api import BaseResource, BaseListResource, validate_auth
from clinic_app.rest.schemas import AppointmentSchema
from clinic_app.service import AppointmentService


class AppointmentMixIn:
    """Mixin that provides class attribute values for served appointment API's"""
    service = AppointmentService
    schema = AppointmentSchema
    filters_parser = RequestParser()
    filters_parser.add_argument('doctor_uuid', type=int)
    filters_parser.add_argument('patient_uuid', type=int)
    filters_parser.add_argument('date_from', type=lambda x: date.fromordinal(int(x)))
    filters_parser.add_argument('date_to', type=lambda x: date.fromordinal(int(x)))
    filters_parser.add_argument('unfilled', type=bool, default=False)


class AppointmentApi(BaseResource, AppointmentMixIn):
    """Appointment API class"""


class AppointmentsApi(BaseListResource, AppointmentMixIn):
    """Appointment list API class"""


class StatisticsApi(Resource, AppointmentMixIn):
    """Appointment's statistics list API class"""

    @classmethod
    @validate_auth
    def get(cls):
        """Retrieve"""
        filters = cls.filters_parser.parse_args()
        count = cls.service.get_count(**filters)
        income = cls.service.get_income(**filters)
        return {'count': count, 'income': income}, 200
