"""
This module defines booked appointment service class:
"""
from datetime import datetime, date as date_

from clinic_app.models import BookedAppointment
from clinic_app.service.service_routines import ServiceRoutine


# pylint: disable=arguments-differ
class BookedAppointmentService(ServiceRoutine):
    """Service class for querying BookedAppointment model"""
    model = BookedAppointment
    order_by = (model.date, model.time)

    @classmethod
    def _filter_by(cls, *, doctor_id: int = None, patient_id: int = None,
                   date: date_ = None, past_only: bool = False):
        """
        Return query ordered and filtered.

        :param doctor_id: filter booked appointments having given doctor_id
        :param patient_id: filter booked appointments having given patient_id
        :param date: filter booked appointments having given date
        :param past_only: filter booked appointments before now
        """
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
