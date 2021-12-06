# pylint: disable=missing-module-docstring, missing-class-docstring
from flask_testing import TestCase

from clinic_app import config, app, db
from clinic_app.models import User, Doctor, Patient, BookedAppointment, ServedAppointment
from clinic_app.service.population import populate, clear_tables


class BaseTestCase(TestCase):
    db = db
    models = {'user': User,
              'doctor': Doctor,
              'patient': Patient,
              'booked_app': BookedAppointment,
              'served_app': ServedAppointment}

    @classmethod
    def setUpClass(cls):
        clear_tables()
        populate(100)

    def create_app(self):
        app.config.from_object(config.DevelopmentConfig)
        self.db.create_all()
        return app

    def tearDown(self):
        db.session.remove()
