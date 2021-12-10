"""
Users REST API, this module defines the following classes:

- `UserMixIn`: user API mixin class
- `UsersApi`: users collection API resource class
- `UserApi`: user API resource class
"""
from flask_restful.reqparse import RequestParser

from clinic_app.rest.resources.base_api import BaseResource, BaseListResource
from clinic_app.rest.schemas import UserSchema
from clinic_app.service import UserService


class UserMixIn:
    """Mixin that provides class attribute values for user API's"""
    service = UserService
    schema = UserSchema
    filters_parser = RequestParser()
    filters_parser.add_argument('email')


class UserApi(BaseResource, UserMixIn):
    """User API class"""


class UsersApi(BaseListResource, UserMixIn):
    """User list API class"""
