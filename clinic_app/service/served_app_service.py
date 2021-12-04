from datetime import date as date_

from clinic_app.models import ServedAppointment
from clinic_app.service.base_service import BaseService


# pylint: disable=arguments-differ
class ServedAppointmentService(BaseService):
    model = ServedAppointment
    order_by = (model.date, model.time)

    @classmethod
    def _filter_by(cls, *, doctor_id: int = None, patient_id: int = None,
                   date_from: date_ = None, date_to: date_ = None, _query=None):
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

    @classmethod
    def get_filtered_count(cls, **kwargs):
        query = cls.model.query
        return cls._filter_by(_query=query, **kwargs).count()

    # pylint: disable=no-member
    @classmethod
    def get_filtered_income(cls, **kwargs):

        query = cls.db.session.query(cls.db.func.sum(cls.model.bill))
        return cls._filter_by(_query=query, **kwargs).scalar()
