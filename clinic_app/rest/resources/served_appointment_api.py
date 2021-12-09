"""
Served appointments REST API, this module defines the following classes:

- `ServedAppointmentMixIn`: served appointment API mixin class
- `ServedAppointmentsApi`: served appointments collection API resource class
- `ServedAppointmentApi`: served appointment API resource class
"""
from datetime import date

from flask_restful.reqparse import RequestParser

from clinic_app.rest.resources.base_api import BaseItemResource, BaseCollectionResource
from clinic_app.rest.schemas import ServedAppointmentSchema
from clinic_app.service import ServedAppointmentService


class ServedAppointmentMixIn:
    """Mixin that provides class attribute values for served appointment API's"""
    service = ServedAppointmentService
    schema = ServedAppointmentSchema
    parser = RequestParser()
    parser.add_argument('doctor_id', type=int)
    parser.add_argument('patient_id', type=int)
    parser.add_argument('date_from', type=lambda x: date.fromordinal(int(x)))
    parser.add_argument('date_to', type=lambda x: date.fromordinal(int(x)))


class ServedAppointmentApi(BaseItemResource, ServedAppointmentMixIn):
    """Served appointment API class"""


class ServedAppointmentsApi(BaseCollectionResource, ServedAppointmentMixIn):
    """Served appointment list API class"""
