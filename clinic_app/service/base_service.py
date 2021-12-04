import typing as t

from sqlalchemy.exc import IntegrityError

from clinic_app import db


class ServiceMixIn:
    db = db
    model: db.Model
    order_by: t.Tuple[db.Column]


class BaseService(ServiceMixIn):
    @classmethod
    def _filter_by(cls, **kwargs):
        raise NotImplementedError

    @classmethod
    def _order(cls):
        return cls.model.query.order_by(*cls.order_by)

    @classmethod
    def get_or_404(cls, id_: int):
        return cls.model.query.get_or_404(id_)

    @classmethod
    def exists(cls, id_: int):
        exists = cls.model.query.filter(cls.model.id == id_).exists()
        return cls.db.session.query(exists).scalar()

    @classmethod
    def get_filtered_pagination(cls, **kwargs):
        return cls._filter_by(**kwargs).paginate()

    @classmethod
    def delete(cls, id_: int):
        res = cls.model.query.filter(cls.model.id == id_).delete()
        cls.commit()
        return res

    @classmethod
    def commit(cls):
        cls.db.session.commit()

    @classmethod
    def save(cls, model: db.Model):
        cls.db.session.add(model)
        cls.commit()
        return model.id


def handle_db_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IntegrityError as err:
            return {'message': 'Request data violates database constraints',
                    'errors': err.orig.args[1]}, 422

    return wrapper
