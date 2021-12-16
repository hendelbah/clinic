"""
This module defines patient service class:
"""
from sqlalchemy.orm import Query

from clinic_app.models import Patient
from clinic_app.service.base_service import BaseService


# pylint: disable=arguments-differ
class PatientService(BaseService):
    """Service class for querying Patient model"""
    model = Patient
    order_by = (model.name, model.surname, model.patronymic)

    @classmethod
    def _filter_by(cls, *, phone: str = None, name: str = None, surname: str = None,
                   patronymic: str = None) -> Query:
        """
        Return query ordered and filtered.

        :param phone: filter patients having this phone number
        :param name: filter patients having this name
        :param surname: filter patients having this surname
        :param surname: filter patients having this patronymic
        """
        query = cls._order()
        if phone is not None:
            query = query.filter_by(phone_number=phone)
        if name is not None:
            query = query.filter_by(name=name)
        if surname is not None:
            query = query.filter_by(surname=surname)
        if patronymic is not None:
            query = query.filter_by(patronymic=patronymic)
        return query
