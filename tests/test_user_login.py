# pylint: disable=missing-function-docstring, missing-module-docstring, missing-class-docstring
from clinic_app.service.population.population_data import ROOT_PASSWORD
from clinic_app.views.user_login import UserLogin
from tests.base_test_case import BaseTestCase


class TestUserLogin(BaseTestCase):
    def test_load_by_uuid(self):
        user = UserLogin.load_by_uuid('1')
        self.assertIsNotNone(user)
        self.assertEqual(str(user), "<User(email='root', is_admin=True, uuid='1')>")
        user = UserLogin.load_by_uuid('asdf')
        self.assertIsNone(user)

    def test_load_by_email(self):
        user = UserLogin.load_by_email('root')
        self.assertIsNotNone(user)
        user = UserLogin.load_by_email('zxcv')
        self.assertIsNone(user)

    def test_check_password(self):
        user = UserLogin.load_by_email('root')
        self.assertTrue(user.check_password(ROOT_PASSWORD))

    def test_hash_password(self):
        pass_hash = UserLogin.hash_password('123')
        self.assertEqual(len(pass_hash), 102)
