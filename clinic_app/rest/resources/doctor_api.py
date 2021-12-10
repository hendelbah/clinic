"""
Doctors REST API, this module defines the following classes:

- `DoctorMixIn`: doctor API mixin class
- `DoctorsApi`: doctors collection API resource class
- `DoctorApi`: doctor API resource class
"""
from flask_restful.reqparse import RequestParser

from clinic_app.rest.resources.base_api import BaseResource, BaseListResource
from clinic_app.rest.schemas import DoctorSchema
from clinic_app.service import DoctorService


class DoctorMixIn:
    """Mixin that provides class attribute values for doctor API's"""
    service = DoctorService
    schema = DoctorSchema
    filters_parser = RequestParser()
    filters_parser.add_argument('search_name')
    filters_parser.add_argument('no_user', type=bool, default=False)


class DoctorApi(BaseResource, DoctorMixIn):
    """Doctor API class"""


class DoctorsApi(BaseListResource, DoctorMixIn):
    """Doctor list API class"""
