# pylint: disable=missing-module-docstring, missing-class-docstring
from flask_testing import TestCase

from clinic_app import config, app, db
from clinic_app.models import User, Doctor, Patient, Appointment
from clinic_app.service.population import populate, clear_tables

app.config.from_object(config.TestingConfig)
db.create_all()


class BaseTestCase(TestCase):
    db = db
    app = app
    models = (User, Doctor, Patient, Appointment)
    api_auth = {'api_key': app.config['API_KEY']}

    @classmethod
    def setUpClass(cls):
        clear_tables()
        populate(100)

    def create_app(self):
        return app

    def tearDown(self):
        db.session.remove()
