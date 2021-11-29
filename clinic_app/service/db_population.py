from random import choices
from string import digits
from datetime import date
from werkzeug.security import generate_password_hash
from clinic_app.models import *
from .population_data import *


def populate():
    """
    Clear tables and populate database with sample data, using population_data source.
    """
    # User.query.filter(User.email.like('doctor\___@spam.ua')).delete(synchronize_session=False)
    BookedAppointment.query.delete()
    FulfilledAppointment.query.delete()
    Patient.query.delete()
    User.query.delete()
    Doctor.query.delete()
    MedicalArea.query.delete()

    medical_areas = [MedicalArea(*area_data) for area_data in AREAS_SRC]
    doctors_pass_hash = generate_password_hash('Doctor1488_322')
    for i, doctor_src in enumerate(DOCTORS_SRC):
        doctor = Doctor(*doctor_src['data'])
        doctor.medical_area = medical_areas[doctor_src['area_index']]
        user_doctor = User(f'doctor_{i:0>2}@spam.ua', doctors_pass_hash, _hash=False)
        print(user_doctor)
        user_doctor.doctor = doctor
        db.session.add(user_doctor)
    db.session.commit()
