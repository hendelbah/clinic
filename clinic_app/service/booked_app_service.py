from datetime import datetime, date as date_

from clinic_app.models import BookedAppointment
from clinic_app.service.base_service import BaseService


# pylint: disable=arguments-differ
class BookedAppointmentService(BaseService):
    model = BookedAppointment
    order_by = (model.date, model.time)

    @classmethod
    def _filter_by(cls, *, doctor_id: int = None, patient_id: int = None,
                   date: date_ = None, past_only: bool = False):
        query = cls._order()
        if doctor_id is not None:
            query = query.filter_by(doctor_id=doctor_id)
        if patient_id is not None:
            query = query.filter_by(patient_id=patient_id)
        if date is not None:
            query = query.filter_by(date=date)
        if past_only:  # filter appointments with datetime < now
            now = datetime.now()
            query = query.filter(cls.model.date <= now.date()).filter(
                (cls.model.time < now.time()) | (cls.model.date < now.date())
            )
        return query
