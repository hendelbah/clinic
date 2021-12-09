# pylint: disable=missing-module-docstring, missing-class-docstring
from flask_testing import TestCase

from clinic_app import config, app, db
from clinic_app.models import User, Doctor, Patient, BookedAppointment, ServedAppointment
from clinic_app.service.population import populate, clear_tables

app.config.from_object(config.DevelopmentConfig)

app.config['SQLALCHEMY_ECHO'] = False


class BaseTestCase(TestCase):
    db = db
    app = app
    api_auth = {'api_key': app.config['API_KEY']}
    models = {'user': User,
              'doctor': Doctor,
              'patient': Patient,
              'booked_app': BookedAppointment,
              'served_app': ServedAppointment}

    @classmethod
    def setUpClass(cls):
        cls.db.create_all()
        clear_tables()
        populate(100)

    def create_app(self):
        return app

    def tearDown(self):
        db.session.remove()
