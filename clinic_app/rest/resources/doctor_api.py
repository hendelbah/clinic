"""
Doctors REST API, this module defines the following classes:

- `DoctorMixIn`: doctor API mixin class
- `DoctorsApi`: doctors collection API resource class
- `DoctorApi`: doctor API resource class
"""
from flask_restful.reqparse import RequestParser

from clinic_app.rest.resources.base_api import BaseItemResource, BaseCollectionResource
from clinic_app.rest.schemas import DoctorSchema
from clinic_app.service import DoctorService


class DoctorMixIn:
    """Mixin that provides class attribute values for doctor API's"""
    service = DoctorService
    schema = DoctorSchema
    parser = RequestParser()
    parser.add_argument('search_name', type=str)
    parser.add_argument('no_user', type=bool, default=False)


class DoctorApi(BaseItemResource, DoctorMixIn):
    """Doctor API class"""


class DoctorsApi(BaseCollectionResource, DoctorMixIn):
    """Doctor list API class"""
