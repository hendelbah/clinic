"""
This module contains base resource classes with common routines.

Classes:

- `BaseItemResource` base resource class, defines routines for single item resources
- `BaseCollectionResource` base resource class, defines routines for collection resources

Functions:

- `validate_auth`: wrapper for validation api authentication.
"""
from functools import wraps

from flask import request, current_app
from flask_restful import Resource, reqparse, abort

from clinic_app import ma
from clinic_app.rest.schemas import pagination_schema
from clinic_app.service import BaseService


def validate_auth(func):
    """
    Wraps request handler function, throws 401 http error
    if valid api-key isn't provided in headers

    :param func: function with request context
    """

    # pylint: disable=inconsistent-return-statements
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'api-key' not in request.headers:
            abort(401, message="Credentials not present in request")
        elif request.headers['api-key'] != current_app.config['API_KEY']:
            abort(401, message="Credentials not valid")
        else:
            return func(*args, **kwargs)

    return wrapper


# pylint: disable=redefined-builtin
class BaseItemResource(Resource):
    """Base Resource class with common routines for inheritance"""

    service: BaseService
    schema: ma.Schema
    parser: reqparse.RequestParser

    @classmethod
    @validate_auth
    def get(cls, id):
        """Retrieve"""
        schema = cls.schema()
        instance = cls.service.get_or_404(id)
        return schema.dump(instance), 200

    @classmethod
    @validate_auth
    def put(cls, id):
        """Update"""
        schema = cls.schema(partial=True, load_instance=False)
        data = schema.load_or_422(request.json)
        cls.service.update_or_abort(id, data)
        return {}, 204

    @classmethod
    @validate_auth
    def delete(cls, id):
        """Delete"""
        cls.service.delete_or_404(id)
        return {}, 204


class BaseCollectionResource(Resource):
    """Base Resource class with common routines for inheritance"""

    service: BaseService
    schema: ma.Schema
    parser: reqparse.RequestParser

    @classmethod
    @validate_auth
    def post(cls):
        """Create"""
        data = request.json
        schema = cls.schema(transient=True, partial=('id',))
        instance = schema.load_or_422(data)
        cls.service.save_or_422(instance)
        return {'id': instance.id}, 201

    @classmethod
    @validate_auth
    def get(cls):
        """Retrieve"""
        schema = cls.schema()
        args = cls.parser.parse_args()
        pagination = cls.service.get_filtered_pagination(**args)
        p_schema = pagination_schema(schema)()
        return p_schema.dump(pagination), 200
