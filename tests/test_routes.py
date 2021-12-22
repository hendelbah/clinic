# pylint: disable=missing-function-docstring, missing-module-docstring, missing-class-docstring
from unittest.mock import patch, Mock

from flask import url_for, request
from werkzeug.datastructures import TypeConversionDict

from clinic_app.service.populate.population_data import ROOT_PASSWORD
from clinic_app.views.routes.admin import user_endpoints, doctor_endpoints, patient_endpoints, \
    appointment_endpoints
from clinic_app.views.utils import random_password, get_pagination_args, extract_filters, \
    parse_filters
from tests.base_test_case import BaseTestCase

endpoints_bundle = [user_endpoints, doctor_endpoints, patient_endpoints, appointment_endpoints]


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

    def test_admin_routes(self):
        response = self.client.post(url_for('auth.login'),
                                    json={'email': 'root', 'pwd': ROOT_PASSWORD, 'remember': False})
        self.assertRedirects(response, url_for('general.index'))
        self.assertMessageFlashed('You successfully logged in', 'success')
        response = self.client.get(url_for('admin.index'))
        self.assert200(response)
        post_data = (
            {'email': 'cocojambo@gmail.com', 'is_admin': False, 'doctor_uuid': ''},
            {'full_name': 'the world', 'speciality': 'is gonna', 'info': 'roll me',
             'experience_years': 100},
            {'phone_number': '88005553535', 'full_name': 'Slave Ass 300', 'birthday': '2012-12-12'},
            {'date': '2013-10-10', 'time': '10:00'},
        )
        filters_data = (
            {'search_email': 'asd'},
            {'search_name': 'qwe'},
            {'search_phone': 'aboba', 'search_name': 'bobak'},
            {'doctor_name': 'amogus', 'date_from': '2012-12-12'},
        )
        i = 0
        for endpoints, data, filters in zip(endpoints_bundle, post_data, filters_data):
            with self.subTest(str(i := i + 1)):
                response = self.client.get(url_for(endpoints['list']))
                self.assert200(response)
                response = self.client.post(url_for(endpoints['list']), json=filters)
                self.assertRedirects(response, url_for(endpoints['list'], **filters))
                response = self.client.get(url_for(endpoints['item'], uuid='10'))
                self.assert200(response)
                response = self.client.get(url_for(endpoints['item'], uuid='new'))
                if i == 4:
                    self.assertRedirects(response, url_for('admin.doctors', act=1))
                    args = {'doctor': '3', 'patient': '5'}
                else:
                    self.assert200(response)
                    args = {}
                response = self.client.post(
                    url_for(endpoints['item'], uuid='new', **args), json=data)
                self.assertStatus(response, 302)
                response = self.client.post(url_for(endpoints['item'], uuid='10'))
                self.assert200(response)
                response = self.client.post(url_for(endpoints['delete'], uuid='10'))
                self.assertRedirects(response, url_for(endpoints['list']))
        data = {'date': '2013-10-10', 'time': '10:00', 'conclusion': 'oao',
                'prescription': 'kek', 'bill': 5}
        response = self.client.post(url_for('admin.appointment', uuid='11'), json=data)
        self.assertRedirects(response, url_for('admin.appointment', uuid='11'))


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

    def test_parse_filters(self):
        form = Mock()
        with self.app.test_request_context(), \
                patch.object(request, 'args', TypeConversionDict({'a': 1, 'b': 'z'})):
            res = parse_filters([{'key': 'a', 'type': int}, {'key': 'b'}], form)
            self.assertEqual(res, {'a': 1, 'b': 'z'})

    def test_extract_filters(self):
        field1 = Mock(data=3)
        field2 = Mock(data='a')
        form = Mock(a=field1, b=field2)
        res = extract_filters(['a', 'b'], form)
        self.assertEqual(res, {'a': 3, 'b': 'a'})
