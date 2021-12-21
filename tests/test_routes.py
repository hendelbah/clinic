# pylint: disable=missing-function-docstring, missing-module-docstring, missing-class-docstring
from unittest.mock import patch

from flask import url_for

from clinic_app.service.population.population_data import ROOT_PASSWORD
from clinic_app.views.utils import random_password, get_pagination_args
from tests.base_test_case import BaseTestCase


class TestRoutes(BaseTestCase):
    def test_200(self):
        endpoints = ('general.index', 'general.doctors')
        for endpoint in endpoints:
            with self.subTest(endpoint):
                response = self.client.get(url_for(endpoint=endpoint))
                self.assert200(response)

    def test_login_profile_logout(self):
        # successful login
        response = self.client.post(url_for('auth.login'),
                                    json={'email': 'root', 'pwd': ROOT_PASSWORD, 'remember': False})
        self.assertRedirects(response, url_for('general.index'))
        self.assertMessageFlashed('You successfully logged in', 'success')
        # log in again when already logged
        response = self.client.get(url_for('auth.login'))
        self.assertRedirects(response, url_for('general.index'))
        # get profile page
        response = self.client.get(url_for('auth.profile'))
        self.assertStatus(response, 200)
        # change pass with wrong current pass
        response = self.client.post(
            url_for('auth.profile'),
            json={'password': '123456', 'new_pass': '123456', 'confirm': '123456'}
        )
        self.assertRedirects(response, url_for('auth.profile'))
        self.assertMessageFlashed('Wrong current password', 'error')
        # successful password change
        response = self.client.post(
            url_for('auth.profile'),
            json={'password': ROOT_PASSWORD, 'new_pass': '123456', 'confirm': '123456'}
        )
        self.assertRedirects(response, url_for('auth.profile'))
        self.assertMessageFlashed('Your password was changed', 'success')
        # successful logout
        response = self.client.get(url_for('auth.logout'))
        self.assertRedirects(response, url_for('general.index'))
        self.assertMessageFlashed('You successfully logged out', 'success')

    def test_wrong_login_logout(self):
        response = self.client.post(
            url_for('auth.login'),
            json={'email': 'do@gmail.com', 'pwd': '123456', 'remember': False}
        )
        self.assertStatus(response, 200)
        response = self.client.post(url_for('auth.login'),
                                    json={'email': 'root', 'pwd': '123456', 'remember': False})
        self.assertStatus(response, 200)
        response = self.client.get(url_for('auth.logout'))
        self.assertRedirects(response, url_for('general.index'))

    def test_unauthorized_redirect(self):
        endpoints = ('auth.profile', 'auth.logout')
        redirects = (url_for('auth.login', next='/profile'), url_for('general.index'))
        for endpoint, redirect in zip(endpoints, redirects):
            with self.subTest(endpoint):
                response = self.client.get(url_for(endpoint=endpoint))
                self.assertRedirects(response, redirect)


class TestUtils(BaseTestCase):
    @patch('clinic_app.views.utils.choice', return_value='a')
    def test_random_password(self, mock):
        pwd = random_password(10)
        self.assertEqual(pwd, 'aaaaaaaaaa')
        self.assertEqual(mock.call_count, 10)

    def test_pagination_args(self):
        with self.app.test_request_context():
            page, per_page = get_pagination_args()
            self.assertEqual(page, 1)
            self.assertEqual(per_page, 20)
        with self.app.test_request_context(path='/?page=3&per_page=23'):
            page, per_page = get_pagination_args()
            self.assertEqual(page, 3)
            self.assertEqual(per_page, 23)
