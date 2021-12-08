"""
This module defines base service classes with common routines and service functions.

Classes:

- `BaseService` defines common routines for service class

Functions:

- `handle_db_errors`: decorator for request handler functions. Throw http error
  if `sqlalchemy.exc.IntegrityError` occurs during decorated function execution
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
            cls.db.session.commit()
            return
        except IntegrityError as err:
            msg = 'Request data violates database constraints'
            errors = err.orig.args[1]
        except DatabaseError as err:
            msg = 'Database error'
            errors = err.orig.args[1]
        abort(422, message=msg, errors=errors)
        cls.db.session.close()

    @classmethod
    def get_or_404(cls, id_: int) -> db.Model:
        """Get model instance or throw 404 error

        :param id_:  model's database id
        """
        return cls.model.query.get_or_404(id_)

    @classmethod
    def update_or_abort(cls, id_: int, data: dict):
        """
        Update row with given id using data.
        If id is not found throw 404 http exception.
        In case of db conflicts throw 422 http error.

        :param id_: database id in model's table.
        :param data: dict with fields to update.
        """
        instance = cls.get_or_404(id_)
        for key in data:
            setattr(instance, key, data[key])
        cls._commit()

    @classmethod
    def save_or_422(cls, model_instance: db.Model) -> int:
        """
        Save given model instance to db and return its id.
        In case of db conflicts throw 422 http error.

        :param model_instance: instance to save to db.
        :return: id of saved instance
        """
        cls.db.session.add(model_instance)
        cls._commit()
        return model_instance.id

    @classmethod
    def delete_or_404(cls, id_: int):
        """Delete row by id. Throw 404 http exception if id is not found"""
        res = cls.model.query.filter(cls.model.id == id_).delete()
        if not res:
            abort(404)
        cls._commit()

    @classmethod
    def get_filtered_pagination(cls, page: int = None, per_page: int = None,
                                **kwargs) -> Pagination:
        """
        Return Pagination object, for model instances selected and filtered using kwargs

        :param page: pagination page
        :param per_page: items per page for pagination
        :param kwargs: kwargs for filtering
        """
        return cls._filter_by(**kwargs).paginate(page=page, per_page=per_page)
