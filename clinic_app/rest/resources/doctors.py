from flask_restful.reqparse import RequestParser
from clinic_app.rest.schemas import DoctorSchema
from clinic_app.service import DoctorService
from clinic_app.rest.resources.base_resource import BaseResource, BaseListResource


class AbstractDoctors:
    service = DoctorService
    schema = DoctorSchema
    parser = RequestParser()
    parser.add_argument('full_name', type=str)


class Doctors(BaseResource, AbstractDoctors):
    pass


class DoctorsList(BaseListResource, AbstractDoctors):
    pass
