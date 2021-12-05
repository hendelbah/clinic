"""
This module defines patient service class:
"""
from clinic_app.models import Patient
from clinic_app.service.service_routines import ServiceRoutine


# pylint: disable=arguments-differ
class PatientService(ServiceRoutine):
    """Service class for querying Patient model"""
    model = Patient
    order_by = (model.id,)

    @classmethod
    def _filter_by(cls, *, phone_number: str = None, name: str = None, surname: str = None):
        """
        Return query ordered and filtered.

        :param phone_number: filter patients having given phone number
        :param name: filter patients having given name
        :param surname: filter patients having given surname
        """
        query = cls._order()
        if phone_number is not None:
            query = query.filter_by(phone_number=phone_number)
        if name is not None:
            query = query.filter_by(name=name)
        if surname is not None:
            query = query.filter_by(surname=surname)
        return query
