"""
Users REST API, this module defines the following classes:

- `UserMixIn`: user API mixin class
- `UsersApi`: users collection API resource class
- `UserApi`: user API resource class
"""
from flask_restful.reqparse import RequestParser

from clinic_app.rest.resources.base_api import BaseItemResource, BaseCollectionResource
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


class UserApi(BaseItemResource, UserMixIn):
    """User API class"""


class UsersApi(BaseCollectionResource, UserMixIn):
    """User list API class"""
