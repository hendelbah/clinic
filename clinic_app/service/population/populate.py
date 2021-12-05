"""
This module contains main populating functions
"""
from datetime import date, time, timedelta
from random import choice, randint
from uuid import uuid4

from clinic_app import db
from clinic_app.models import BookedAppointment, ServedAppointment, Doctor, Patient, User
from clinic_app.service.population.population_data import (
    DOCTORS_SRC, NAMES_SRC, SURNAMES_SRC, PATRONYMICS_SRC, ROOT_PASSWORD, DOCTORS_PASSWORD)
from clinic_app.service.population.random_utils import random_9d_number, random_date
from clinic_app.views.authorization import UserAccount

root_pass_hash = UserAccount.hash_password(ROOT_PASSWORD)
doctors_pass_hash = UserAccount.hash_password(DOCTORS_PASSWORD)


def clear_tables():
    """
    Clear all tables.
    """
    BookedAppointment.query.delete()
    ServedAppointment.query.delete()
    Patient.query.delete()
    User.query.delete()
    Doctor.query.delete()
    db.session.commit()


# pylint: disable=no-member
def populate(patients_amount=100):
    """
    Populate database with sample data, using population_data and random_utils.

    :param patients_amount: amount of random patients to insert
    """
    root_user = {'id': 1,
                 'uuid': UserAccount.generate_uuid(),
                 'email': 'root',
                 'password_hash': root_pass_hash,
                 'is_admin': True}
    db.session.execute(db.insert(User).values(root_user))
    users_doctors_src = [
        {
            'id': user_id,
            'doctor_id': doctor["id"],
            'uuid': uuid4(),
            'email': f'doctor_{doctor["id"]:0>3}@spam.ua',
            'password_hash': doctors_pass_hash,  # hashing is too slow to do it for every user
            'is_admin': False
        }
        for user_id, doctor in enumerate(DOCTORS_SRC, 2)  # 1st user is root
    ]
    patients_src = []
    booked_apps_src = []
    served_apps_src = []
    for i in range(1, patients_amount + 1):
        sex = randint(0, 1)
        patient = {
            'id': i,
            'phone_number': '380' + random_9d_number(),
            'surname': choice(SURNAMES_SRC),
            'name': choice(NAMES_SRC[sex]),
            'patronymic': choice(PATRONYMICS_SRC[sex]),
            'birthday': random_date(date(1950, 1, 1), date(2005, 12, 31))
        }
        b_appointment = {
            'id': i,
            'patient_id': i,
            'doctor_id': randint(1, len(DOCTORS_SRC)),
            'date': date.today() + timedelta(days=i - 20),
            'time': time(hour=11),
        }
        f_appointment = {
            'id': i,
            'patient_id': i,
            'doctor_id': randint(1, len(DOCTORS_SRC)),
            'date': date.today() - timedelta(days=20 + i),
            'time': time(hour=12),
            'conclusion': 'Diagnosis: common cold',
            'prescription': 'Panadol 500mg',
            'bill': randint(200, 400),
        }
        patients_src.append(patient)
        booked_apps_src.append(b_appointment)
        served_apps_src.append(f_appointment)

    db.session.bulk_insert_mappings(Doctor, DOCTORS_SRC)
    db.session.bulk_insert_mappings(User, users_doctors_src)
    db.session.bulk_insert_mappings(Patient, patients_src)
    db.session.bulk_insert_mappings(BookedAppointment, booked_apps_src)
    db.session.bulk_insert_mappings(ServedAppointment, served_apps_src)
    db.session.commit()
