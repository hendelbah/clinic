"""
This module defines served appointment service class:
"""
from datetime import date as date_

from clinic_app.models import ServedAppointment
from clinic_app.service.base_service import BaseService


# pylint: disable=arguments-differ
class ServedAppointmentService(BaseService):
    """Service class for querying ServedAppointment model"""
    model = ServedAppointment
    order_by = (model.date, model.time)

    @classmethod
    def _filter_by(cls, *, doctor_id: int = None, patient_id: int = None,
                   date_from: date_ = None, date_to: date_ = None, _query=None):
        """
        Return query ordered and filtered.

        :param doctor_id: filter served appointments having given doctor_id
        :param patient_id: filter served appointments having given patient_id
        :param date_from: filter served appointments having date >= given value
        :param date_to: filter served appointments having date <= given value
        :param _query: query to override standard one
        """
        query = cls._order() if _query is None else _query
        if doctor_id is not None:
            query = query.filter_by(doctor_id=doctor_id)
        if patient_id is not None:
            query = query.filter_by(patient_id=patient_id)
        if date_from is not None:
            query = query.filter(cls.model.date >= date_from)
        if date_to is not None:
            query = query.filter(cls.model.date <= date_to)
        return query
