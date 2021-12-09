"""
Patients REST API, this module defines the following classes:

- `PatientMixIn`: patient API mixin class
- `PatientsApi`: patients collection API resource class
- `PatientApi`: patient API resource class
"""
from flask_restful.reqparse import RequestParser

from clinic_app.rest.resources.base_api import BaseItemResource, BaseCollectionResource
from clinic_app.rest.schemas import PatientSchema
from clinic_app.service import PatientService


class PatientMixIn:
    """Mixin that provides class attribute values for patient API's"""
    service = PatientService
    schema = PatientSchema
    parser = RequestParser()
    parser.add_argument('phone', dest='phone_number')
    parser.add_argument('name')
    parser.add_argument('surname')


class PatientApi(BaseItemResource, PatientMixIn):
    """Patient API class"""


class PatientsApi(BaseCollectionResource, PatientMixIn):
    """Patient list API class"""
