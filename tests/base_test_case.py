# pylint: disable=missing-module-docstring, missing-class-docstring, wrong-import-position
import os

from flask_testing import TestCase

os.environ['FLASK_CONFIG'] = 'testing'

from clinic_app import app, db
from clinic_app.models import User, Doctor, Patient, Appointment
from clinic_app.service.population import populate, clear_tables


class BaseTestCase(TestCase):
    db = db
    app = app
    models = (User, Doctor, Patient, Appointment)
    api_auth = {'api_key': app.config['API_KEY']}

    @classmethod
    def setUpClass(cls):
        populate(100)

    @classmethod
    def tearDownClass(cls) -> None:
        clear_tables()

    def create_app(self):
        return app

    def tearDown(self):
        db.session.remove()
