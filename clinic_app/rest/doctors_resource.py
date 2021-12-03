from flask import request
from flask_restful import Resource
from clinic_app.models import Doctor
from clinic_app.schemas import DoctorSchema, paginate_schema
from clinic_app.service import BasicQueryHelper
from clinic_app.rest.utils import validate_data


class DoctorsResource(Resource):
    queries = BasicQueryHelper(Doctor)
    db = queries.db

    def get(self, doctor_id=None):
        doctor_schema = DoctorSchema()
        if doctor_id is not None:
            doctor = self.queries.get_or_404(doctor_id)
            return doctor_schema.dump(doctor), 200
        doctors_pagination = self.queries.get_paginated()
        p_schema = paginate_schema(doctor_schema)()
        return p_schema.dump(doctors_pagination), 200

    def put(self, doctor_id=None):
        if doctor_id is None:
            return {'message': 'Resource not found'}, 404
        data = request.json
        data['id'] = doctor_id
        is_new = not self.queries.exists(doctor_id)
        opts = {'transient': True} if is_new else {'session': self.db.session, 'partial': True}
        doctor_schema = DoctorSchema(**opts)
        doctor, errors = validate_data(doctor_schema, data)
        if not doctor:
            return errors, 422
        self.queries.save(doctor)
        return doctor_schema.dump(doctor), 201 if is_new else 200

    def delete(self, doctor_id=None):
        if not self.queries.exists(doctor_id):
            return {'message': 'Resource not found'}, 404
        self.queries.delete(doctor_id)
        return None, 204
