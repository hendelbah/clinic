from clinic_app.models import Doctor
from clinic_app.service.base_service import BaseService


# pylint: disable=arguments-differ
class DoctorService(BaseService):
    model = Doctor
    order_by = (model.id,)

    @classmethod
    def _filter_by(cls, *, search_name: str = None):
        query = cls._order()
        if search_name is not None:
            query = query.filter(cls.model.full_name.like('%' + search_name + '%'))
        return query
