from flask import request
from flask_restful import Resource, reqparse

from clinic_app import ma
from clinic_app.rest.schemas import paginate_schema, validate_data
from clinic_app.service import BaseService, handle_db_errors


class ResourceTemplate(Resource):
    service: BaseService
    schema: ma.Schema
    parser: reqparse.RequestParser


class BaseResource(ResourceTemplate):
    @classmethod
    def get(cls, id):
        schema = cls.schema()
        instance = cls.service.get_or_404(id)
        return schema.dump(instance), 200

    @classmethod
    @handle_db_errors
    def put(cls, id):
        data = request.json
        data['id'] = id
        is_new = not cls.service.exists(id)
        opts = {'transient': True} if is_new else {'partial': True}
        schema = cls.schema(session=cls.service.db.session, **opts)
        instance, errors = validate_data(schema, data)
        if not instance:
            return errors, 422
        cls.service.save(instance)
        return '', 204

    @classmethod
    def delete(cls, id):
        if not cls.service.exists(id):
            return {'message': 'Resource not found'}, 404
        cls.service.delete(id)
        return '', 204


class BaseListResource(ResourceTemplate):
    @classmethod
    @handle_db_errors
    def post(cls):
        data = request.json
        schema = cls.schema(transient=True, exclude=('id',))
        instance, errors = validate_data(schema, data)
        if not instance:
            return errors, 422
        cls.service.save(instance)
        return {'id': instance.id}, 201

    @classmethod
    @handle_db_errors
    def get(cls):
        schema = cls.schema()
        args = cls.parser.parse_args()
        print(args)
        pagination = cls.service.get_filtered_pagination(**args)
        p_schema = paginate_schema(schema)()
        return p_schema.dump(pagination), 200
