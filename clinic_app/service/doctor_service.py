"""
This module defines doctor service class:
"""
from clinic_app.models import Doctor
from clinic_app.service.service_routines import ServiceRoutine


# pylint: disable=arguments-differ
class DoctorService(ServiceRoutine):
    """Service class for querying Doctor model"""
    model = Doctor
    order_by = (model.id,)

    @classmethod
    def _filter_by(cls, *, search_name: str = None):
        """
        Return query ordered and filtered.

        :param search_name: filter doctors with full_name containing search_name
        """
        query = cls._order()
        if search_name is not None:
            query = query.filter(cls.model.full_name.like('%' + search_name + '%'))
        return query
