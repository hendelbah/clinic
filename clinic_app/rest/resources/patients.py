from flask_restful.reqparse import RequestParser

from clinic_app.rest.resources.base_resource import BaseResource, BaseListResource
from clinic_app.rest.schemas import PatientSchema
from clinic_app.service import PatientService


class PatientsMixin:
    service = PatientService
    schema = PatientSchema
    parser = RequestParser()
    parser.add_argument('phone', dest='phone_number')
    parser.add_argument('name')
    parser.add_argument('surname')


class Patients(BaseResource, PatientsMixin):
    pass


class PatientsList(BaseListResource, PatientsMixin):
    pass
