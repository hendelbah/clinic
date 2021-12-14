"""
This module contains base resource classes with common routines.

Classes:

- `BaseResource` base resource class, defines routines for single item resources
- `BaseListResource` base resource class, defines routines for collection resources

Functions:

- `validate_auth`: wrapper for validation api authentication.
"""
from functools import wraps

from flask import request, current_app
from flask_restful import Resource, reqparse, abort
from werkzeug.http import http_date

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


# pylint: disable=missing-function-docstring
class BaseResource(Resource):
    """Base Resource class with common routines for inheritance"""

    service: BaseService
    schema: ma.Schema

    @classmethod
    @validate_auth
    def head(cls, uuid):
        modified = http_date(cls.service.get_item_modified(uuid))
        return {}, 204, {'Last-Modified': modified}

    @classmethod
    @validate_auth
    def get(cls, uuid):
        schema = cls.schema()
        instance = cls.service.get_or_404(uuid)
        modified = http_date(instance.last_modified)
        return schema.dump(instance), 200, {'Last-Modified': modified}

    @classmethod
    @validate_auth
    def put(cls, uuid):
        schema = cls.schema(partial=True)
        data = schema.load_or_422(request.json)
        instance = cls.service.update_or_abort(uuid, data)
        return schema.dump(instance), 200

    @classmethod
    @validate_auth
    def delete(cls, uuid):
        cls.service.delete_or_404(uuid)
        return {}, 204


class BaseListResource(Resource):
    """Base Resource class with common routines for inheritance"""

    service: BaseService
    schema: ma.Schema
    filters_parser: reqparse.RequestParser
    pagination_parser = reqparse.RequestParser()
    pagination_parser.add_argument('page', type=int, default=1)
    pagination_parser.add_argument('per_page', type=int, default=20)

    @classmethod
    @validate_auth
    def head(cls):
        filters = cls.filters_parser.parse_args()
        pages = cls.pagination_parser.parse_args()
        modified = http_date(cls.service.get_pagination_modified(**pages, **filters))
        return {}, 204, {'Last-Modified': modified}

    @classmethod
    @validate_auth
    def get(cls):
        schema = cls.schema()
        filters = cls.filters_parser.parse_args()
        pages = cls.pagination_parser.parse_args()
        pagination = cls.service.get_pagination(**pages, **filters)
        modified = http_date(max(map(lambda i: i.last_modified, pagination.items)))
        p_schema = pagination_schema(schema)
        return p_schema.dump(pagination), 200, {'Last-Modified': modified}

    @classmethod
    @validate_auth
    def post(cls):
        schema = cls.schema()
        data = schema.load_or_422(request.json)
        instance = cls.service.save_or_422(data)
        return schema.dump(instance), 201
