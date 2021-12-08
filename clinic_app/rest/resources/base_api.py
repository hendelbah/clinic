"""
This module contains base resource classes with common routines.

Classes:

- `BaseResource` base resource class, defines routines for resources with urls with `id` parameter
- `BaseResourceList` base resource class, defines routines for resources with no url parameters
"""
from flask import request
from flask_restful import Resource, reqparse

from clinic_app import ma
from clinic_app.rest.schemas import pagination_schema
from clinic_app.service import BaseService


# pylint: disable=redefined-builtin
class BaseResource(Resource):
    """Base Resource class with common routines for inheritance"""

    service: BaseService
    schema: ma.Schema
    parser: reqparse.RequestParser

    @classmethod
    def get(cls, id):
        """Retrieve"""
        schema = cls.schema()
        instance = cls.service.get_or_404(id)
        return schema.dump(instance), 200

    @classmethod
    def put(cls, id):
        """Update"""
        schema = cls.schema(partial=True, load_instance=False)
        data = schema.load_or_422(request.json)
        cls.service.update_or_abort(id, data)
        return '', 204

    @classmethod
    def delete(cls, id):
        """Delete"""
        cls.service.delete_or_404(id)
        return '', 204


class BaseResourceList(Resource):
    """Base Resource class with common routines for inheritance"""

    service: BaseService
    schema: ma.Schema
    parser: reqparse.RequestParser

    @classmethod
    def post(cls):
        """Create"""
        data = request.json
        schema = cls.schema(transient=True, partial=('id',))
        instance = schema.load_or_422(data)
        cls.service.save_or_422(instance)
        return {'id': instance.id}, 201

    @classmethod
    def get(cls):
        """Retrieve"""
        schema = cls.schema()
        args = cls.parser.parse_args()
        pagination = cls.service.get_filtered_pagination(**args)
        p_schema = pagination_schema(schema)()
        return p_schema.dump(pagination), 200
