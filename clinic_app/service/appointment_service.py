from datetime import datetime, date as date_
from clinic_app.models import BookedAppointment, FulfilledAppointment
from clinic_app.service.base_service import BaseService


class BookedAppointmentService(BaseService):
    model = BookedAppointment
    order_by = (model.date, model.time)

    @classmethod
    def filter_ordered(cls, doctor_id: int = None, patient_id: int = None,
                       date: date_ = None, past: bool = False):
        query = cls.order()
        if doctor_id is not None:
            query = query.filter_by(doctor_id=doctor_id)
        if patient_id is not None:
            query = query.filter_by(patient_id=patient_id)
        if date is not None:
            query = query.filter_by(date=date)
        if past:
            now = datetime.now()
            query = (query.filter(cls.model.date <= now.date())
                     .filter((cls.model.time < now.time()) | (cls.model.date < now.date())))
        return query


class FulfilledAppointmentService(BookedAppointmentService):
    model = FulfilledAppointment

