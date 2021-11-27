from .basemodel import BaseModel, db
from clinic_app import login_manager
from flask_login import UserMixin

import uuid


class User(BaseModel, UserMixin):
    __tablename__ = 'user'

    uuid = db.Column(db.String(36), nullable=False, unique=True)
    email = db.Column(db.String(60), nullable=False, unique=True)
    password_hash = db.Column(db.String(127), nullable=False, default="test")
    is_admin = db.Column(db.Boolean, default=False)
    active = db.Column(db.Boolean, default=False)
    time_created = db.Column(db.DateTime, server_default=db.func.now())

    patient_account = db.relationship('Patient', back_populates='user', uselist=False)
    doctor_account = db.relationship('Doctor', back_populates='user', uselist=False)

    def __init__(self):
        pass

    def get_id(self):
        return self.uuid


@login_manager.user_loader
def load_user(user_uuid: str):
    """
    method gives user object for current registered user
    :param user_uuid: id of employee in db
    :return: employee object
    """
    return User.query.filter(User.uuid == user_uuid).first()
