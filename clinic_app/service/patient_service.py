from clinic_app.models import Patient
from clinic_app.service.base_service import BaseService


# pylint: disable=arguments-differ
class PatientService(BaseService):
    model = Patient
    order_by = (model.id,)

    @classmethod
    def _filter_by(cls, *, phone_number: str = None, name: str = None, surname: str = None):
        query = cls._order()
        if phone_number is not None:
            query = query.filter_by(phone_number=phone_number)
        if name is not None:
            query = query.filter_by(name=name)
        if surname is not None:
            query = query.filter_by(surname=surname)
        return query
