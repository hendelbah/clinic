from .basemodel import BaseModel, db
from flask_login import UserMixin
import uuid


class User(BaseModel, UserMixin):
    __tablename__ = 'user'

    uuid = db.Column(db.String(36), nullable=False, unique=True)
    email = db.Column(db.String(60), nullable=False, unique=True)
    password = db.Column(db.String(127), nullable=False, default="test")
    is_admin = db.Column(db.Boolean, default=False)
    time_created = db.Column(db.DateTime, server_default=db.func.now())

    patient_account = db.relationship('Patient', back_populates='user', uselist=False)
    doctor_account = db.relationship('Doctor', back_populates='user', uselist=False)

