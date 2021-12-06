"""
This module defines base service classes with common routines and service functions.

Classes:

- `BaseService` defines common routines for service class

Functions:

- `handle_db_errors`: decorator for request handler functions. Throw http error
  if `sqlalchemy.exc.IntegrityError` occurs during decorated function execution
"""
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
    def get_or_404(cls, id_: int) -> db.Model:
        """Get model instance or throw 404 error
        :param id_:  model's database id
        """
        return cls.model.query.get_or_404(id_)

    @classmethod
    def exists(cls, id_: int) -> bool:
        """
        Check if there is row with given id in database
        :param id_: model's database id
        """
        exists = cls.model.query.filter(cls.model.id == id_).exists()
        return cls.db.session.query(exists).scalar()

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

    @classmethod
    def delete(cls, id_: int):
        """Delete row by id"""
        cls.model.query.filter(cls.model.id == id_).delete()
        cls.commit()

    @classmethod
    def commit(cls):
        """Commit to session"""
        cls.db.session.commit()

    @classmethod
    def save(cls, model: db.Model) -> int:
        """Save given model instance to db and return its id"""
        cls.db.session.add(model)
        cls.commit()
        return model.id


def handle_db_errors(func):
    """
    Wrap given function to handle db error. If error happens throw 422 http error

    :param func: request handlling function
    :return: wrapper function
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IntegrityError as err:
            return {'message': 'Request data violates database constraints',
                    'errors': err.orig.args[1]}, 422
        except DatabaseError as err:
            return {'message': 'Unexpected database error',
                    'errors': err.orig.args[1]}, 422

    return wrapper
