"""
Doctors REST API, this module defines the following classes:

- `DoctorMixIn`: doctor API mixin class
- `DoctorListApi`: doctor list API class
- `DoctorApi`: doctor API class
"""
from flask_restful.reqparse import RequestParser

from clinic_app.rest.resources.base_api import BaseResource, BaseResourceList
from clinic_app.rest.schemas import DoctorSchema
from clinic_app.service import DoctorService


class DoctorMixIn:
    """Mixin that provides class attribute values for doctor API's"""
    service = DoctorService
    schema = DoctorSchema
    parser = RequestParser()
    parser.add_argument('search_name', type=str)
    parser.add_argument('no_user', type=bool, default=False)


class DoctorApi(BaseResource, DoctorMixIn):
    """Doctor API class"""


class DoctorListApi(BaseResourceList, DoctorMixIn):
    """Doctor list API class"""
