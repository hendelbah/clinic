"""
This module defines user service class:
"""
from clinic_app.models import User
from clinic_app.service.base_service import BaseService


# pylint: disable=arguments-differ
class UserService(BaseService):
    """Service class for querying User model"""
    model = User
    order_by = (model.id,)

    @classmethod
    def _filter_by(cls, *, email: str = None):
        """
        Return query ordered and filtered.

        :param email: filter users having given email
        """
        query = cls._order()
        if email is not None:
            query = query.filter_by(email=email)
        return query
