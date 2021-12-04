from clinic_app.models import Patient
from clinic_app.service.base_service import BaseService


class PatientService(BaseService):
    model = Patient
    order_by = (model.id,)

    @classmethod
    def filter_ordered(cls, phone: str = None, name: str = None, surname: str = None):
        query = cls.order()
        if phone is not None:
            query = query.filter_by(phone_number=phone)
        if name is not None:
            query = query.filter_by(name=name)
        if surname is not None:
            query = query.filter_by(surname=surname)
        return query
