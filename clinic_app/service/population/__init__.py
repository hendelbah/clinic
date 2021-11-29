"""
Package contains tools for database population with test data.
This module contains main populating functions
"""
from random import choice, randrange
from uuid import uuid4
from clinic_app.service.population.random_utils import random_9d_number, random_date
from clinic_app.models import *
from clinic_app.service.population.population_data import *


def populate(patients_amount=100):
    """
    Clear tables and populate database with sample data, using population_data and random_utils.

    :param patients_amount: amount of random patients to insert
    """
    BookedAppointment.query.delete()
    FulfilledAppointment.query.delete()
    Patient.query.delete()
    User.query.delete()
    Doctor.query.delete()
    MedicalArea.query.delete()

    db.session.bulk_insert_mappings(MedicalArea, AREAS_SRC)
    db.session.bulk_insert_mappings(Doctor, DOCTORS_SRC)
    users_doctors_src = [
        {
            'id': doctor["id"],
            'doctor_id': doctor["id"],
            'uuid': uuid4(),
            'email': f'doctor_{doctor["id"]:0>3}@spam.ua',
            'password_hash': DOCTORS_PASS_HASH,  # hashing is too slow to do it for every user
            'is_admin': False
        }
        for doctor in DOCTORS_SRC
    ]
    db.session.bulk_insert_mappings(User, users_doctors_src)
    root_user = {'id': 18,
                 'uuid': 'root_user',
                 'email': 'clinic_admin',
                 'password_hash': ADMIN_PASS_HASH,
                 'is_admin': True}
    db.session.execute(db.insert(User).values(root_user))
    patients_src = []
    for i in range(1, patients_amount + 1):
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
    db.session.bulk_insert_mappings(Patient, patients_src)

    db.session.commit()
