"""
This module contains base resource classes with common routines.

Classes:

- `BaseResource`: declares common class attributes
- `ResourceRoutine` defines routines for resources with urls with `id` parameter
- `ListResourceRoutine` defines routines for resources without url parameters
"""
from flask import request
from flask_restful import Resource, reqparse, abort

from clinic_app import ma
from clinic_app.rest.schemas import pagination_schema, validate_data
from clinic_app.service import ServiceRoutine, handle_db_errors


class BaseResource(Resource):
    """Base resource class"""
    service: ServiceRoutine
    schema: ma.Schema
    parser: reqparse.RequestParser

    @staticmethod
    def json_validated():
        """Get dict from request's json or get 400 error"""
        data = request.json
        if not isinstance(data, dict):
            abort(400)
        return data


# pylint: disable=redefined-builtin
class ResourceRoutine(BaseResource):
    """Resource class with common routines for inheritance"""

    @classmethod
    def get(cls, id):
        """Retrieve"""
        schema = cls.schema()
        instance = cls.service.get_or_404(id)
        return schema.dump(instance), 200

    @classmethod
    @handle_db_errors
    def put(cls, id):
        """Update"""
        data = cls.json_validated()
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
        """Delete"""
        if not cls.service.exists(id):
            return {'message': 'Resource not found'}, 404
        cls.service.delete(id)
        return '', 204


class ListResourceRoutine(BaseResource):
    """ListResource class with common routines for inheritance"""

    @classmethod
    @handle_db_errors
    def post(cls):
        """Create"""
        data = cls.json_validated()
        schema = cls.schema(transient=True, exclude=('id',))
        instance, errors = validate_data(schema, data)
        if not instance:
            return errors, 422
        cls.service.save(instance)
        return {'id': instance.id}, 201

    @classmethod
    @handle_db_errors
    def get(cls):
        """Retrieve"""
        schema = cls.schema()
        args = cls.parser.parse_args()
        pagination = cls.service.get_filtered_pagination(**args)
        p_schema = pagination_schema(schema)()
        return p_schema.dump(pagination), 200
