"""
This module implements instance of user in database
"""
from clinic_app import db


# pylint: disable=redefined-builtin
class User(db.Model):
    """
    User object stands for representation of data row in `user` table.
    Table stores user information for authentication
    """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id', ondelete='CASCADE'),
                          unique=True, index=True)
    uuid = db.Column(db.String(36), nullable=False, unique=True, index=True)
    email = db.Column(db.String(80), nullable=False, unique=True, index=True)
    password_hash = db.Column(db.String(127), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False)

    doctor = db.relationship('Doctor', back_populates='user')

    def __init__(self, uuid: str, email: str, password_hash: str, is_admin,
                 doctor_id: int = None, id: int = None):
        """
        :param doctor_id: corresponding doctor id from `doctor` table
        :param uuid: application's uuid of user
        :param email: email of user
        :param password_hash: user's password hash
        :param is_admin: bool parameter for admins only, False by default
        :param id: user's table id
        """
        self.uuid = uuid
        self.email = email
        self.password_hash = password_hash
        self.is_admin = is_admin
        self.id = id
        self.doctor_id = doctor_id

    def __repr__(self):
        keys = ('id', 'email', 'is_admin')
        values = (f"{key}={getattr(self, key)!r}" for key in keys)
        return f'<User({", ".join(values)})>'
