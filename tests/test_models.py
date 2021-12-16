# pylint: disable=missing-function-docstring, missing-module-docstring, missing-class-docstring
from clinic_app.models import User
from clinic_app.models.descriptors import DoctorUUID, PatientUUID
from clinic_app.service.population.population_data import ROOT_PASSWORD
from tests.base_test_case import BaseTestCase


class TestModels(BaseTestCase):

    def test_user_set_password(self):
        user = User.query.get(3)
        p_hash = user.password_hash
        user.set_password('12345')
        self.assertNotEqual(p_hash, user.password_hash)
        self.assertEqual(len(user.password_hash), 102)

    def test_user_check_password(self):
        user = User.query.get(1)
        self.assertTrue(user.check_password(ROOT_PASSWORD))

    def test_descriptors(self):
        descriptors = {'doctor_id': DoctorUUID, 'patient_id': PatientUUID}
        for key, value in descriptors.items():
            class GuineaPig:
                uuid = value()

            test_obj = GuineaPig()
            test_obj.uuid = None
            self.assertIsNone(getattr(test_obj, key))
            test_obj.uuid = '1'
            self.assertEqual(getattr(test_obj, key), 1)
            with self.assertRaises(ValueError):
                test_obj.uuid = 'asd'
