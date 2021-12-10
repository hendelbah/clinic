"""
This module defines base service classes with common routines and service functions.

Classes:

- `BaseService` defines common routines for service class
"""
from flask_restful import abort
from flask_sqlalchemy import Pagination
from sqlalchemy.exc import IntegrityError, DatabaseError
from sqlalchemy.orm import Query

from clinic_app import db


class BaseService:
    """Base abstract service class with common routines"""
    db = db
    model: db.Model
    order_by: tuple[db.Column]

    @classmethod
    def _filter_by(cls, **kwargs) -> Query:
        """Should return some query with filtering clause using given kwargs"""
        raise NotImplementedError

    @classmethod
    def _order(cls) -> Query:
        """Return model's base query with ORDER BY clause using order_by class argument"""
        return cls.model.query.order_by(*cls.order_by)

    @classmethod
    def _commit(cls):
        """Commit current session. If db error happens throw 422 http error"""
        try:
            db.session.commit()
            return
        except IntegrityError as error:
            msg = 'Request data violates database constraints'
            err = error
        except DatabaseError as error:
            msg = 'Error occurred when committing data to database'
            err = error
        abort(422, message=msg, errors={err.__class__.__name__: err.orig.args[1]})

    @classmethod
    def get_or_404(cls, uuid: str) -> db.Model:
        """Get model instance or throw 404 error

        :param uuid: model's uuid
        """
        instance = cls.model.query.filter_by(uuid=uuid).first()
        if instance is None:
            abort(404)
        return instance

    @classmethod
    def update_or_abort(cls, uuid: str, data: dict):
        """
        Update row with given id using data.
        If id is not found throw 404 http exception.
        In case of db conflicts throw 422 http error.

        :param uuid: model's uuid.
        :param data: dict with fields to update.
        """
        instance = cls.get_or_404(uuid)
        for key in data:
            setattr(instance, key, data[key])
        cls._commit()
        return instance

    @classmethod
    def save_or_422(cls, data: dict) -> db.Model:
        """
        Save given model instance to db and return its id.
        In case of db conflicts throw 422 http error.

        :param data: dict with fields to initialize the model
        :return: saved model instance
        """
        instance = cls.model(**data)
        db.session.add(instance)
        cls._commit()
        return instance

    @classmethod
    def delete_or_404(cls, uuid: str):
        """
        Delete row by id. Throw 404 http exception if id is not found

        :param uuid: model's uuid.
        """
        res = cls.model.query.filter_by(uuid=uuid).delete()
        if not res:
            abort(404)
        cls._commit()

    @classmethod
    def get_pagination(cls, page: int = None, per_page: int = None,
                       **filters) -> Pagination:
        """
        Return Pagination object, for model instances selected and filtered using kwargs

        :param page: pagination page
        :param per_page: items per page for pagination
        :param filters: kwargs for filtering
        """
        return cls._filter_by(**filters).paginate(page=page, per_page=per_page)
