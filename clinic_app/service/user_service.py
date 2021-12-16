"""
This module defines user service class:
"""
import typing as t

from sqlalchemy.exc import DatabaseError
from sqlalchemy.orm import Query

from clinic_app.models import User
from clinic_app.service.base_service import BaseService


# pylint: disable=arguments-differ
class UserService(BaseService):
    """Service class for querying User model"""
    model = User
    order_by = (model.id,)

    @classmethod
    def _filter_by(cls, *, email: str = None) -> Query:
        """
        Return query ordered and filtered.

        :param email: filter users having given email
        """
        query = cls._order()
        if email is not None:
            query = query.filter_by(email=email)
        return query

    @classmethod
    def get_by_email(cls, email: str) -> t.Optional[User]:
        """
        Load user from db by email, return User instance if success, else return None

        :param email: user's email
        """
        return cls.model.query.filter_by(email=email).first()

    @classmethod
    def save_instance(cls, user: User) -> t.Optional[str]:
        """
        Save User instance to database. If db error happens return
        error message, else return None.
        """
        try:
            cls.db.session.add(user)
            cls.db.session.commit()
        except DatabaseError as error:
            return error.orig.args[-1]
        return None
