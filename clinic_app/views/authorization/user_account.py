"""
Module defines user class for authorization in web app
"""
from uuid import uuid4

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


# from clinic_app import login_manager


class UserAccount(UserMixin):
    """
    This is a user class for authentication
    """

    def __init__(self, doctor_id: int, uuid: str, email: str, password_hash: str,
                 is_admin: bool, id_: int = None):
        """
        :param id_: user's db id
        :param doctor_id: doctor id that user has access to
        :param uuid: uuid of user
        :param email: email of user
        :param password_hash: user's password hash
        :param is_admin: indicates admin users, False by default
        """
        self.id_ = id_
        self.doctor_id = doctor_id
        self.uuid = uuid
        self.email = email
        self.password_hash = password_hash
        self.is_admin = is_admin

    @classmethod
    def new(cls, email: str, password: str, doctor_id: int = None, is_admin: bool = False):
        """
        Create a new user.

        :param email: user's email
        :param doctor_id: id of attached doctor
        :param password: user's password, if not provided - generate random one
        :param is_admin: whether user is admin
        :return: new user instance
        """
        pass_hash = cls.hash_password(password)
        uuid = cls.generate_uuid()
        return cls(doctor_id, uuid, email, pass_hash, is_admin)

    def get_id(self):
        """Get user identifier for authorization"""
        return self.uuid

    def check_password(self, password):
        """
        Check equality of given password with user's

        :param str password: password to compare with employee's password
        :return True if given password hash is equal to password hash of employee
        """
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def hash_password(password):
        """
        Return hashed password
        """
        return generate_password_hash(password)

    @staticmethod
    def generate_uuid():
        """Generate new uuid"""
        return str(uuid4())

# @login_manager.user_loader
# def load_user(user_uuid: str):
#     """
#     method gives user object for current registered user
#
#     :param user_uuid: id of employee in db
#     :return: employee object
#     """
#     return User.query.filter(User.uuid == user_uuid).first()
