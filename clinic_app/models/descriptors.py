"""
This module contains proxy descriptors for setting some model's foreign key using uuid field
"""

from clinic_app import db
from clinic_app.models.doctor import Doctor
from clinic_app.models.patient import Patient


# pylint: disable=missing-function-docstring
class DoctorUUID:
    """
    Proxy descriptor for setting doctor_id foreign key using doctor's uuid
    """

    def __set__(self, instance, value: str):
        instance.doctor_id = None if value is None else \
            db.session.query(Doctor.id).filter_by(uuid=value).scalar()


class PatientUUID:
    """
    Proxy descriptor for setting patient_id foreign key using patient's uuid
    """

    def __set__(self, instance, value: str):
        instance.patient_id = None if value is None else \
            db.session.query(Patient.id).filter_by(uuid=value).scalar()
