"""
This module describes basic model for creating tables
"""
from clinic_app import db


class BaseModel(db.Model):
    """
    Just custom basic model with common functionality
    implements id primary key and __repr__
    """
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def __repr__(self):
        values = (f"{key}={repr(getattr(self, key))}" for key in self.__table__.columns.keys())
        values_str = ", ".join(values)
        return f"<{self.__class__.__name__}({values_str})>"
