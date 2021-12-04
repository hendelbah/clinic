from datetime import date
from flask_restful.reqparse import RequestParser
from clinic_app.rest.schemas import BookedAppointmentSchema
from clinic_app.rest.resources.base_resource import BaseResource, BaseListResource
from clinic_app.service import BookedAppointmentService


class AbstractBookedAppointment:
    service = BookedAppointmentService
    schema = BookedAppointmentSchema
    parser = RequestParser()
    parser.add_argument('doctor_id', type=int)
    parser.add_argument('patient_id', type=int)
    parser.add_argument('date', type=lambda x: date.fromordinal(int(x)))
    parser.add_argument('past', type=bool)


class BookedAppointments(BaseResource, AbstractBookedAppointment):
    pass


class BookedAppointmentsList(BaseListResource, AbstractBookedAppointment):
    pass
