"""
This module implements instance of clinic's medical area in database
"""
from clinic_app.models.basemodel import BaseModel, db


class MedicalArea(BaseModel):
    """
    MedicalArea object stands for representation of data row in medical_area table.
    There is information about this clinic's areas of medicine.
    """
    __tablename__ = 'medical_area'
    name = db.Column(db.String(60), nullable=False, unique=True)
    description = db.Column(db.String(511))

    doctors = db.relationship('Doctor', back_populates='medical_area')

    def __init__(self, name, description):
        """
        :param str name: the name of medical area
        :param str description: area description/clinic's achievements
        """
        self.name = name
        self.description = description
