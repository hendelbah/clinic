from clinic_app.models import Doctor
from clinic_app.service.base_service import BaseService


class DoctorService(BaseService):
    model = Doctor
    order_by = (model.id,)

    @classmethod
    def filter_ordered(cls, full_name: str = None):
        query = cls.order()
        if full_name is not None:
            query = query.filter(cls.model.full_name.like('%' + full_name + '%'))
        return query
