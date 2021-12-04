from flask_restful.reqparse import RequestParser
from clinic_app.rest.schemas import PatientSchema
from clinic_app.service import PatientService
from clinic_app.rest.resources.base_resource import BaseResource, BaseListResource


class AbstractPatients:
    service = PatientService
    schema = PatientSchema
    parser = RequestParser()
    parser.add_argument('phone')
    parser.add_argument('name')
    parser.add_argument('surname')


class Patients(BaseResource, AbstractPatients):
    pass


class PatientsList(BaseListResource, AbstractPatients):
    pass
