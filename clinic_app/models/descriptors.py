"""
This module contains proxy descriptors for setting some model's foreign key using uuid field
"""

from clinic_app import db
from clinic_app.models.doctor import Doctor
from clinic_app.models.patient import Patient


class DoctorUUID:
    """
    Proxy descriptor for setting doctor_id foreign key using doctor's uuid
    """

    def __set__(self, instance, value: str):
        """
        Set instance's doctor_id attribute to id of doctor with given uuid.
        If value is None - set doctor_id to None

        :raise ValueError: if doctor is not found
        """
        if value is None:
            instance.doctor_id = None
        else:
            doctor_id = db.session.query(Doctor.id).filter_by(uuid=value).scalar()
            if doctor_id is None:
                raise ValueError('Invalid doctor_uuid')
            instance.doctor_id = doctor_id


class PatientUUID:
    """
    Proxy descriptor for setting patient_id foreign key using patient's uuid
    """

    def __set__(self, instance, value: str):
        """
        Set instance's patient_id attribute to id of patient with given uuid.
        If value is None - set patient_id to None

        :raise ValueError: if patient is not found
        """
        if value is None:
            instance.patient_id = None
        else:
            patient_id = db.session.query(Patient.id).filter_by(uuid=value).scalar()
            if patient_id is None:
                raise ValueError('Invalid patient_uuid')
            instance.patient_id = patient_id
