"""
Patients REST API, this module defines the following classes:

- `PatientMixIn`: patient API mixin class
- `PatientListApi`: patient list API class
- `PatientApi`: patient API class
"""
from flask_restful.reqparse import RequestParser

from clinic_app.rest.resources.resource_routines import ResourceRoutine, ListResourceRoutine
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


class PatientApi(ResourceRoutine, PatientMixIn):
    """Patient API class"""


class PatientListApi(ListResourceRoutine, PatientMixIn):
    """Patient list API class"""
