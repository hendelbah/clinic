from datetime import date
from flask_restful.reqparse import RequestParser
from clinic_app.rest.schemas import FulfilledAppointmentSchema
from clinic_app.rest.resources.base_resource import BaseResource, BaseListResource
from clinic_app.service import FulfilledAppointmentService


class AbstractFulfilledAppointment:
    service = FulfilledAppointmentService
    schema = FulfilledAppointmentSchema
    parser = RequestParser()
    parser.add_argument('doctor_id', type=int)
    parser.add_argument('patient_id', type=int)
    parser.add_argument('date', type=lambda x: date.fromordinal(int(x)))


class FulfilledAppointments(BaseResource, AbstractFulfilledAppointment):
    pass


class FulfilledAppointmentsList(BaseListResource, AbstractFulfilledAppointment):
    pass
