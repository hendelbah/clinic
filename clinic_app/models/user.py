"""
This module implements instance of user in database
"""
from .basemodel import BaseModel, db
from clinic_app import login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import uuid


class User(BaseModel, UserMixin):
    """
    User object stands for representation of data row in user table.
    It is a user class for authentication
    """
    __tablename__ = 'user'

    uuid = db.Column(db.String(36), nullable=False, unique=True, index=True)
    email = db.Column(db.String(60), nullable=False, unique=True, index=True)
    password_hash = db.Column(db.String(127), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False)
    active = db.Column(db.Boolean, default=True, nullable=False)

    patient_account = db.relationship('Patient', back_populates='user', uselist=False)
    doctor_account = db.relationship('Doctor', back_populates='user', uselist=False)

    def get_id(self):
        return self.uuid

    @property
    def is_active(self):
        return self.active

    def __init__(self, email, password, is_admin=False):
        """
        :param str email: email of user
        :param str password: password for user account
        :param bool is_admin: bool parameter for admins only, False by default
        """
        self.uuid = str(uuid.uuid4())
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.is_admin = is_admin

    def check_password(self, password):
        """
        method checks equality of given password with user's
        :param password: password to compare with employee's password
        :return True if given password hash is equal to password hash of employee
        """
        return check_password_hash(self.password, password)


@login_manager.user_loader
def load_user(user_uuid: str):
    """
    method gives user object for current registered user
    :param user_uuid: id of employee in db
    :return: employee object
    """
    return User.query.filter(User.uuid == user_uuid).first()
