from clinic_app.rest.doctors_resource import DoctorsResource

from flask_restful import Api
from flask import Blueprint

api_blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(api_blueprint)


api.add_resource(DoctorsResource, '/doctors', '/doctors/<int:doctor_id>')