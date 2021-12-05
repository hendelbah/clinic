"""
Served appointments REST API, this module defines the following classes:

- `ServedAppointmentMixIn`: served appointment API mixin class
- `ServedAppointmentListApi`: served appointment list API class
- `ServedAppointmentApi`: served appointment API class
- `StatisticsApi`: served appointment statistics API class
"""
from datetime import date

from flask_restful.reqparse import RequestParser

from clinic_app.rest.resources.resource_routines import \
    ResourceRoutine, ListResourceRoutine, BaseResource
from clinic_app.rest.schemas import ServedAppointmentSchema
from clinic_app.service import ServedAppointmentService, handle_constraint_violation


class ServedAppointmentMixIn:
    """Mixin that provides class attribute values for served appointment API's"""
    service = ServedAppointmentService
    schema = ServedAppointmentSchema
    parser = RequestParser()
    parser.add_argument('doctor_id', type=int)
    parser.add_argument('patient_id', type=int)
    parser.add_argument('date_from', type=lambda x: date.fromordinal(int(x)))
    parser.add_argument('date_to', type=lambda x: date.fromordinal(int(x)))


class ServedAppointmentApi(ResourceRoutine, ServedAppointmentMixIn):
    """Served appointment API class"""


class ServedAppointmentListApi(ListResourceRoutine, ServedAppointmentMixIn):
    """Served appointment list API class"""


class StatisticsApi(ServedAppointmentMixIn, BaseResource):
    """Served appointment statistics API class"""

    @classmethod
    @handle_constraint_violation
    def get(cls):
        """Get rows amount and bill sum for filtered with parsed args rows"""
        args = cls.parser.parse_args()
        count = cls.service.get_filtered_count(**args)
        income = cls.service.get_filtered_income(**args)
        return {'appointments_count': count, 'total_income': income}, 200
