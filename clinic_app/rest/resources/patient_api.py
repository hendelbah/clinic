"""
Patients REST API, this module defines the following classes:

- `PatientMixIn`: patient API mixin class
- `PatientsApi`: patients collection API resource class
- `PatientApi`: patient API resource class
"""
from flask_restful.reqparse import RequestParser

from clinic_app.rest.resources.base_api import BaseResource, BaseListResource
from clinic_app.rest.schemas import PatientSchema
from clinic_app.service import PatientService


class PatientMixIn:
    """Mixin that provides class attribute values for patient API's"""
    service = PatientService
    schema = PatientSchema
    filters_parser = RequestParser()
    filters_parser.add_argument('phone')
    filters_parser.add_argument('name')
    filters_parser.add_argument('surname')
    filters_parser.add_argument('patronymic')


class PatientApi(BaseResource, PatientMixIn):
    """Patient API class"""


class PatientsApi(BaseListResource, PatientMixIn):
    """Patient list API class"""
