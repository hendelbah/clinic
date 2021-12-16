"""
This module defines appointment service class:
"""
from datetime import date as date_

from sqlalchemy.orm import Query

from clinic_app.models import Appointment, Doctor, Patient
from clinic_app.service.base_service import BaseService


# pylint: disable=arguments-differ, no-member
class AppointmentService(BaseService):
    """Service class for querying Appointment model"""
    model = Appointment
    order_by = (model.date.desc(), model.time.desc())

    @classmethod
    def _filter_by(cls, *, doctor_uuid: str = None, patient_uuid: str = None,
                   date_from: date_ = None, date_to: date_ = None,
                   unfilled: bool = False, _query=None) -> Query:
        """
        Return query ordered and filtered.

        :param doctor_uuid: filter booked appointments related to doctors with this uuid
        :param patient_uuid: filter booked appointments related to patients with this uuid
        :param date_from: filter served appointments having date >= given value
        :param date_to: filter served appointments having date <= given value
        :param unfilled: filter booked appointments before now
        :param _query: query to override standard one
        """
        query = cls._order() if _query is None else _query
        if doctor_uuid is not None:
            query = query.filter_by(
                doctor_id=
                cls.db.session.query(Doctor.id).filter_by(uuid=doctor_uuid).scalar_subquery()
            )
        if patient_uuid is not None:
            query = query.filter_by(
                patient_id=
                cls.db.session.query(Patient.id).filter_by(uuid=patient_uuid).scalar_subquery()
            )
        if date_from == date_to is not None:
            query = query.filter_by(date=date_from)
        else:
            if date_from is not None:
                query = query.filter(cls.model.date >= date_from)
            if date_to is not None:
                query = query.filter(cls.model.date <= date_to)
        if unfilled:
            today = date_.today()
            query = query.filter_by(bill=None).filter(cls.model.date <= today)
        return query

    @classmethod
    def get_count(cls, **filters) -> int:
        """
        Return amount of appointments rows filtered using kwargs

        :param filters: kwargs for filtering function
        """
        query = cls.model.query
        return cls._filter_by(_query=query, **filters).count()

    @classmethod
    def get_income(cls, **filters) -> int:
        """
        Return sum of bills of appointments filtered using kwargs

        :param filters: kwargs for filtering function
        """
        query = cls.db.session.query(cls.db.func.sum(cls.model.bill))
        return int(cls._filter_by(_query=query, **filters).scalar())
