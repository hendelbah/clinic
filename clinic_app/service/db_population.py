"""
This module stands for populating database
"""
from datetime import date
from random import choice, randrange
from werkzeug.security import generate_password_hash
from clinic_app.service.utils import random_9d_number, random_date
from clinic_app.models import MedicalArea, Doctor, User, Patient, BookedAppointment, FulfilledAppointment, db
from clinic_app.service.population_data import AREAS_SRC, DOCTORS_SRC, NAMES_SRC, SURNAMES_SRC, PATRONYMICS_SRC

ADMIN_PASSWORD = 'yBU6nWPoVRLTtUl'
DOCTORS_PASSWORD = 'cepjaKotDsM5PnG'


def populate():
    """
    Clear tables and populate database with sample data, using population_data.
    """
    # BookedAppointment.query.delete()
    # FulfilledAppointment.query.delete()
    Patient.query.delete()
    # User.query.delete()
    # Doctor.query.delete()
    # MedicalArea.query.delete()
    #
    # root_user = User('clinic_admin', ADMIN_PASSWORD, is_admin=True)
    # db.session.add(root_user)
    # medical_areas = [MedicalArea(*area_data) for area_data in AREAS_SRC]
    # # hashing is too slow to do it for every user
    # doctors_pass_hash = generate_password_hash(DOCTORS_PASSWORD)
    # for i, doctor_src in enumerate(DOCTORS_SRC):
    #     doctor = Doctor(*doctor_src['data'])
    #     doctor.medical_area = medical_areas[doctor_src['area_index']]
    #     user_doctor = User(f'doctor_{i:0>2}@spam.ua', doctors_pass_hash, _hash=False)
    #     user_doctor.doctor = doctor
    #     db.session.add(user_doctor)
    patients_src = []
    for i in range(1, 201):
        sex = randrange(2)
        patient = {
            'id': i,
            'phone_number': '+380' + random_9d_number(),
            'surname': choice(SURNAMES_SRC),
            'name': choice(NAMES_SRC[sex]),
            'patronymic': choice(PATRONYMICS_SRC[sex]),
            'birthday': random_date(1950, 2005)
        }
        patients_src.append(patient)

    db.session.execute(db.insert(Patient).values(patients_src))
    # db.session.commit()
