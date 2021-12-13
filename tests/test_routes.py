# pylint: disable=missing-function-docstring, missing-module-docstring, missing-class-docstring
from flask import url_for

from clinic_app.service.population.population_data import ROOT_PASSWORD
from tests.base_test_case import BaseTestCase


class TestRoutes(BaseTestCase):
    def test_200(self):
        endpoints = ('general.index', 'general.doctors')
        for endpoint in endpoints:
            with self.subTest(endpoint):
                response = self.client.get(url_for(endpoint=endpoint))
                self.assert200(response)

    def test_login_logout(self):
        with self.client as client:
            response = client.post(url_for('auth.login'),
                                   json={'email': 'root', 'pwd': ROOT_PASSWORD, 'remember': False})
            self.assertStatus(response, 302)
            response = self.client.get(url_for('auth.profile'))
            self.assertStatus(response, 200)
            response = self.client.get(url_for('auth.logout'))
            self.assertStatus(response, 302)

    def test_wrong_login_logout(self):
        with self.client as client:
            response = client.post(url_for('auth.login'),
                                   json={'email': 'do@gmail.com', 'pwd': 'a', 'remember': False})
            self.assertStatus(response, 200)
            response = self.client.get(url_for('auth.logout'))
            self.assertStatus(response, 302)

    def test_unauthorized_redirect(self):
        endpoints = ('auth.profile', 'auth.logout')
        for endpoint in endpoints:
            with self.subTest(endpoint):
                response = self.client.get(url_for(endpoint=endpoint))
                self.assertStatus(response, 302)