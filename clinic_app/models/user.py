"""
This module implements instance of user in database
"""
from flask_login import UserMixin
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from clinic_app import login_manager
from clinic_app.models.basemodel import BaseModel, db


class User(BaseModel, UserMixin):
    """
    User object stands for representation of data row in `user` table.
    It is a user class for authentication
    """
    __tablename__ = 'user'
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id', ondelete='CASCADE'), unique=True, index=True)
    uuid = db.Column(db.String(36), nullable=False, unique=True, index=True)
    email = db.Column(db.String(80), nullable=False, unique=True, index=True)
    password_hash = db.Column(db.String(127), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False)

    doctor = db.relationship('Doctor', back_populates='user')

    def __init__(self, email, password, doctor_id=None, is_admin=False, *, _hash=True):
        """
        :param str email: email of user
        :param str password: password for user's account
        :param int doctor_id: corresponding doctor id from `doctor` table
        :param bool is_admin: bool parameter for admins only, False by default
        """
        self.doctor_id = doctor_id
        self.uuid = str(uuid.uuid4())
        self.email = email
        self.is_admin = is_admin
        # Set _hash=False in case if you want to pass already hashed password
        if _hash:
            self.password = password
        else:
            self.password_hash = password

    def get_id(self):
        return self.uuid

    @property
    def password(self):
        """
        Prevent password from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        method checks equality of given password with user's
        :param str password: password to compare with employee's password
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
