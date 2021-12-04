from flask_restful.reqparse import RequestParser

from clinic_app.rest.resources.base_resource import BaseResource, BaseListResource
from clinic_app.rest.schemas import DoctorSchema
from clinic_app.service import DoctorService


class DoctorsMixIn:
    service = DoctorService
    schema = DoctorSchema
    parser = RequestParser()
    parser.add_argument('search_name', type=str)


class Doctors(BaseResource, DoctorsMixIn):
    pass


class DoctorsList(BaseListResource, DoctorsMixIn):
    pass
