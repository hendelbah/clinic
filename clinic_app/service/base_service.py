"""
This module defines base service class with common routines for working with database.

Classes:

- `BaseService` defines common routines for service class
"""
import typing as t
from datetime import datetime

from flask_sqlalchemy import Pagination
from sqlalchemy.exc import IntegrityError, DatabaseError
from sqlalchemy.orm import Query

from clinic_app import db


class BaseService:
    """Base abstract service class for querying database with common routines"""
    db = db
    model: db.Model
    order_by: tuple[db.Column]

    @staticmethod
    def wrap_error(error: Exception, message: str = 'Wrong data'):
        """
        Wrap error with dict to representable form.

        :param error: exception
        :param message: message to add
        """
        error_info = error.orig.args[-1] if isinstance(error, DatabaseError) else str(error)
        return {'message': message, 'errors': {error.__class__.__name__: error_info}}

    @classmethod
    def _filter_by(cls, **kwargs) -> Query:
        """Should return some query with filtering clause using given kwargs"""
        raise NotImplementedError

    @classmethod
    def _order(cls) -> Query:
        """Return model's base query with ORDER BY clause using order_by class argument"""
        return cls.model.query.order_by(*cls.order_by)

    @classmethod
    def _commit(cls) -> t.Optional[dict]:
        """
        Commit current session state. If db error happens return
        dict with error info, else return None
        """
        try:
            db.session.commit()
        except IntegrityError as error:
            return cls.wrap_error(error, 'Request data violates database constraints')
        except DatabaseError as error:
            return cls.wrap_error(error, 'Error occurred when committing transaction')
        return None

    @classmethod
    def get(cls, uuid: str):
        """
        Return model instance by uuid, None if not found

        :param uuid: model's uuid
        """
        return cls.model.query.filter_by(uuid=uuid).first()

    @classmethod
    def get_modified(cls, uuid: str) -> t.Optional[datetime]:
        """
        Return last modified datetime of db row with given uuid, None if not found

        :param uuid: model's uuid
        """
        return db.session.query(cls.model.last_modified).filter_by(uuid=uuid).scalar()

    @classmethod
    def update(cls, uuid: str, data: dict) -> t.Tuple[t.Union[dict, object], int]:
        """
        Update row with given uuid using data.
        Return tuple of data and suitable http status code.
        If success return updated model instance and code 200.
        If uuid is not found return {} and code 404.
        In case of db conflicts return dict with error info and code 422.

        :param uuid: model's uuid.
        :param data: dict with fields to update.
        """
        instance = cls.get(uuid)
        if instance is None:
            return {}, 404
        try:
            for key in data:
                setattr(instance, key, data[key])
        except ValueError as error:
            return cls.wrap_error(error), 422
        errors = cls._commit()
        if errors:
            return errors, 422
        return instance, 200

    @classmethod
    def create(cls, data: dict) -> t.Tuple[t.Union[object, dict], int]:
        """
        Create new model instance and save it to db using data dict.
        Return tuple of data and suitable http status code.
        If success return new model instance and code 200.
        In case of wrong data or db conflicts return dict with error info and code 422.

        :param data: dict with for model initialization
        :return: saved model instance
        """
        try:
            instance = cls.model(**data)
        except (TypeError, ValueError) as error:
            return cls.wrap_error(error), 422
        db.session.add(instance)
        errors = cls._commit()
        if errors:
            return errors, 422
        return instance, 201

    @classmethod
    def delete(cls, uuid: str) -> bool:
        """
        Delete record by uuid. Return True if Success else False.

        :param uuid: model's uuid.
        """
        res = cls.model.query.filter_by(uuid=uuid).delete()
        if res:
            db.session.commit()
        return bool(res)

    @classmethod
    def get_pagination(cls, page: int = 1, per_page: int = 20, **filters) -> t.Optional[Pagination]:
        """200
        Return Pagination object, for model instances selected and filtered using kwargs.

        :param page: pagination page
        :param per_page: items per page for pagination
        :param filters: kwargs for filtering
        """
        return cls._filter_by(**filters).paginate(page=page, per_page=per_page)

    # pylint: disable=no-member
    @classmethod
    def get_pagination_modified(cls, page: int = 1, per_page: int = 20, **filters) -> \
            t.Optional[datetime]:
        """
        Return datetime of last modification of filtered collection.
        If there is no items in filtered collection return None.

        :param page: pagination page
        :param per_page: items per page for pagination
        :param filters: kwargs for filtering
        """
        offset = (page - 1) * per_page
        subquery = cls._filter_by(**filters).limit(per_page).offset(offset).subquery()
        aliased_model = db.aliased(cls.model, subquery)
        return db.session.query(db.func.max(aliased_model.last_modified)).scalar()
