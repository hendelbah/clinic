"""
Booked appointments REST API, this module defines the following classes:

- `BookedAppointmentMixIn`: booked appointment API mixin class
- `BookedAppointmentsApi`: booked appointments collection resource API class
- `BookedAppointmentApi`: booked appointment resource API class
"""
from datetime import date

from flask_restful.reqparse import RequestParser

from clinic_app.rest.resources.base_api import BaseItemResource, BaseCollectionResource
from clinic_app.rest.schemas import BookedAppointmentSchema
from clinic_app.service import BookedAppointmentService


class BookedAppointmentMixIn:
    """Mixin that provides class attribute values for booked appointment API's"""
    service = BookedAppointmentService
    schema = BookedAppointmentSchema
    parser = RequestParser()
    parser.add_argument('doctor_id', type=int)
    parser.add_argument('patient_id', type=int)
    parser.add_argument('date', type=lambda x: date.fromordinal(int(x)))
    parser.add_argument('past_only', type=bool, default=False)


class BookedAppointmentApi(BaseItemResource, BookedAppointmentMixIn):
    """Booked appointment API class"""


class BookedAppointmentsApi(BaseCollectionResource, BookedAppointmentMixIn):
    """Booked appointment list API class"""
