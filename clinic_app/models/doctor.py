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

    medical_area_id = db.Column(db.Integer, db.ForeignKey('medical_area.id', ondelete='SET NULL'), index=True)
    full_name = db.Column(db.String(127), nullable=False)
    speciality = db.Column(db.String(127), nullable=False)
    info = db.Column(db.String(1023), nullable=False)
    experience_years = db.Column(db.Integer, nullable=False)
    time_created = db.Column(db.DateTime, server_default=db.func.now())

    user = db.relationship('User', back_populates='doctor', uselist=False)
    medical_area = db.relationship('MedicalArea', back_populates='doctors')
    booked_appointments = db.relationship('BookedAppointment', back_populates='doctor')
    fulfilled_appointments = db.relationship('FulfilledAppointment', back_populates='doctor')

    def __init__(self, full_name, speciality, info, experience_years, area_id=None):
        """
        :param str full_name: doctor's full name
        :param str speciality: doctor's speciality
        :param str info: some information about doctor to display on site
        :param int experience_years: years of doctor's work experience
        :param int area_id: area id from `medical_area` table
        """
        self.medical_area_id = area_id
        self.full_name = full_name
        self.speciality = speciality
        self.info = info
        self.experience_years = experience_years
