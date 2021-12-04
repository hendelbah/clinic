from datetime import date

from flask_restful.reqparse import RequestParser

from clinic_app.service import ServedAppointmentService, handle_db_errors
from clinic_app.rest.schemas import ServedAppointmentSchema
from clinic_app.rest.resources.base_resource import \
    BaseResource, BaseListResource, ResourceTemplate


class ServedAppointmentMixin:
    service = ServedAppointmentService
    schema = ServedAppointmentSchema
    parser = RequestParser()
    parser.add_argument('doctor_id', type=int)
    parser.add_argument('patient_id', type=int)
    parser.add_argument('date_from', type=lambda x: date.fromordinal(int(x)))
    parser.add_argument('date_to', type=lambda x: date.fromordinal(int(x)))


class ServedAppointments(BaseResource, ServedAppointmentMixin):
    pass


class ServedAppointmentsList(BaseListResource, ServedAppointmentMixin):
    pass


class Statistics(ServedAppointmentMixin, ResourceTemplate):
    @classmethod
    @handle_db_errors
    def get(cls):
        args = cls.parser.parse_args()
        count = cls.service.get_filtered_count(**args)
        income = cls.service.get_filtered_income(**args)
        return {'appointments_count': count, 'total_income': income}, 200
