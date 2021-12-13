"""
Module defines user class for authorization in web app
"""

# from random import choices
# from string import digits, ascii_letters

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from clinic_app import login_manager
from clinic_app.views.api_controllers import ApiHelper


class UserLogin(UserMixin):
    """
    This is a flask_login user class for authentication
    """

    def __init__(self, uuid: str, email: str, password_hash: str, is_admin: bool, doctor: dict):
        """
        :param email: email of user
        :param password_hash: user's password hash
        :param is_admin: indicates admin users, False by default
        :param doctor: doctor object that user has access to
        :param uuid: uuid of user
        """
        self.doctor = doctor
        self.uuid = uuid
        self.email = email
        self.password_hash = password_hash
        self.is_admin = is_admin

    def __repr__(self):
        """Custom instance representation"""
        return f'<User(email={self.email!r}, is_admin={self.is_admin}, uuid={self.uuid!r})>'

    @classmethod
    def load_by_email(cls, email: str):
        """
        Load user by email using API, return class instance if success, else return None

        :param email: user's email
        """
        response = ApiHelper.users.get(email=email)
        if response.status_code == 200 and response.json.get('items'):
            return cls(**response.json['items'][0])
        return None

    @classmethod
    def load_by_uuid(cls, uuid: str):
        """
        Load user by uuid using API, return class instance if success, else return None

        :param uuid: user's uuid
        """
        response = ApiHelper.user.get(uuid)
        if response.status_code == 200:
            return UserLogin(**response.json)
        return None

    # @classmethod
    # def register_new(cls, email: str, password: str, is_admin: bool = False,
    #                  doctor_uuid: str = None):
    #     """
    #     Send post request to API for registering new user. Return response object.
    #
    #     :param email: new user's email
    #     :param password: new user's password
    #     :param is_admin: whether new user should be admin
    #     :param doctor_uuid: uuid of doctor if user should have access to one
    #     :return: api response with code 201 if success, 422 in case of incorrect data
    #     """
    #     user_data = {
    #         'email': email,
    #         'password_hash': cls.hash_password(password),
    #         'is_admin': is_admin,
    #         'doctor_uuid': doctor_uuid
    #     }
    #     return ApiHelper.users.post(data=user_data)

    def get_id(self):
        """Get user's identifier for authorization"""
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


# def random_password(length=15) -> str:
#     """
#     Return random password with given length, generated from ascii letters and digits
#
#     :param int length: password length
#     """
#     return ''.join(choices(ascii_letters + digits, k=length))


@login_manager.user_loader
def load_user(user_uuid: str):
    """
    Return UserLogin instance for current registered user

    :param user_uuid: uuid of user
    """
    return UserLogin.load_by_uuid(user_uuid)
