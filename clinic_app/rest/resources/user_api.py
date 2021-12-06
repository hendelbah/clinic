"""
Users REST API, this module defines the following classes:

- `UserMixIn`: user API mixin class
- `UserListApi`: user list API class
- `UserApi`: user API class
"""
from flask_restful.reqparse import RequestParser

from clinic_app.rest.resources.base_api import BaseResource, BaseResourceList
from clinic_app.rest.schemas import UserSchema
from clinic_app.service import UserService


class UserMixIn:
    """Mixin that provides class attribute values for user API's"""
    service = UserService
    schema = UserSchema
    parser = RequestParser()
    parser.add_argument('uuid', type=str)
    parser.add_argument('email', type=str)
    parser.add_argument('doctor_id', type=int)


class UserApi(BaseResource, UserMixIn):
    """User API class"""


class UserListApi(BaseResourceList, UserMixIn):
    """User list API class"""
