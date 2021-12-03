"""
This module implements instance of doctor in database
"""
from clinic_app.models.basemodel import BaseModel, db


class Doctor(BaseModel):
    """
    Doctor object stands for representation of data row in `doctor` table.
    There is information about doctors that work in this clinic
    """
    __tablename__ = 'doctor'

    full_name = db.Column(db.String(127), nullable=False, index=True)
    speciality = db.Column(db.String(127), nullable=False)
    info = db.Column(db.String(1023), nullable=False)
    experience_years = db.Column(db.Integer, nullable=False)

    user = db.relationship('User', back_populates='doctor', uselist=False)
    booked_appointments = db.relationship('BookedAppointment', back_populates='doctor')
    fulfilled_appointments = db.relationship('FulfilledAppointment', back_populates='doctor')

    def __init__(self, full_name: str, speciality: str, info: str,
                 experience_years: int, id: int = None):
        """
        :param full_name: doctor's full name
        :param speciality: doctor's speciality
        :param info: some information about doctor to display on site
        :param experience_years: years of doctor's work experience
        :param id: doctor's id
        """
        self.full_name = full_name
        self.speciality = speciality
        self.info = info
        self.experience_years = experience_years
        self.id = id
