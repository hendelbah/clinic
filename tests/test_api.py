# pylint: disable=missing-function-docstring, missing-module-docstring, missing-class-docstring
from flask import url_for

from tests.base_test_case import BaseTestCase


class TestApi(BaseTestCase):
    endpoints_1 = ('api.users', 'api.doctors', 'api.patients', 'api.booked_appointments',
                   'api.served_appointments')
    endpoints_2 = ('api.user', 'api.doctor', 'api.patient', 'api.booked_appointment',
                   'api.served_appointment')

    def test_unauthorized_request(self):
        response = self.client.get(url_for('api.users'))
        self.assertStatus(response, 401)
        self.assertEqual(response.json['message'], "Credentials not present in request")
        response = self.client.get(url_for('api.users'), headers={'api-key': 'zxc'})
        self.assertStatus(response, 401)
        self.assertEqual(response.json['message'], "Credentials not valid")

    def test_all_get_200(self):
        for endpoint in self.endpoints_1:
            with self.subTest(endpoint):
                response = self.client.get(url_for(endpoint, per_page=5), headers=self.api_auth)
                self.assert200(response)
                self.assertEqual(len(response.json['items']), 5)
        for endpoint in self.endpoints_2:
            with self.subTest(endpoint):
                response = self.client.get(url_for(endpoint, id=1), headers=self.api_auth)
                self.assert200(response)

    def test_get_by_id(self):
        properties = (
            ('email', 'doctor_001@spam.ua'),
            ('full_name', 'Аблялимова Альбина Шевкетовна'),
            ('phone_number', '380000000006'),
            ('time', '11:00:00'),
            ('time', '12:00:00')
        )
        for endpoint, prop in zip(self.endpoints_2, properties):
            with self.subTest(endpoint):
                response = self.client.get(url_for(endpoint, id=2), headers=self.api_auth)
                self.assert200(response)
                self.assertEqual(response.json['id'], 2)
                self.assertEqual(response.json[prop[0]], prop[1])

    def test_post_and_delete(self):
        data = (
            {'uuid': 'Somebody', 'email': 'once', 'password_hash': 'told me', 'is_admin': True},
            {'full_name': 'the world', 'speciality': 'is gonna', 'info': 'roll me',
             'experience_years': 100},
            {'phone_number': '88005553535', 'name': 'Slave', 'surname': 'Ass',
             'patronymic': '300$', 'birthday': '2012-12-12'},
            {'patient_id': 3, 'doctor_id': 5, 'date': '2012-12-12', 'time': '16:00:00'},
            {'patient_id': 4, 'doctor_id': 5, 'date': '2013-10-10', 'time': '10:00:01',
             'conclusion': 'will die soon', 'prescription': 'submit', 'bill': 5000},
        )
        ids = []
        for endpoint, item in zip(self.endpoints_1, data):
            with self.subTest(endpoint + ':POST'):
                response = self.client.post(url_for(endpoint), json=item, headers=self.api_auth)
                self.assertStatus(response, 201)
                ids.append(response.json['id'])
        for endpoint, id_ in zip(self.endpoints_2, ids):
            with self.subTest(endpoint + ':DELETE'):
                response = self.client.delete(url_for(endpoint, id=id_), headers=self.api_auth)
                self.assertStatus(response, 204)

    def test_put(self):
        data = (
            {'password_hash': 'cocos_olia_jojoba', 'uuid': 'cocojambo'},
            {'full_name': 'Артем Петрович', 'experience_years': 1488},
            {'name': 'McDonald\'s', 'birthday': '1940-05-15'},
            {'id': 403, 'date': '2025-01-01', 'time': '07:00:00'},
            {'date': '2040-12-31', 'conclusion': 'very well'},
        )
        for endpoint, item in zip(self.endpoints_2, data):
            with self.subTest(endpoint):
                response = self.client.put(url_for(endpoint, id=10), json=item,
                                           headers=self.api_auth)
                self.assertStatus(response, 204)

    def test_wrong_get_put_delete(self):
        for endpoint in self.endpoints_2:
            with self.subTest(endpoint):
                response = self.client.get(url_for(endpoint, id=0), headers=self.api_auth)
                self.assert404(response)
                response = self.client.put(url_for(endpoint, id=517), json={'id': 433},
                                           headers=self.api_auth)
                self.assert404(response)
                response = self.client.delete(url_for(endpoint, id=300), headers=self.api_auth)
                self.assert404(response)

    def test_post_wrong_data(self):
        cases = (
            ({'id': 1, 'uuid': 'Somebody', 'email': 'once', 'is_admin': False,
              'password_hash': 'a'},
             []),
            ({'full_name': 'the world', 'speciality': 'is gonna'},
             ['experience_years', 'info']),
            ({'name': 'S', 'surname': 'A', 'patronymic': 'a', 'birthday': '20123-10-10'},
             ['phone_number', 'birthday']),
            ({'doctor_id': 5, 'time': '75:00:00'},
             ['patient_id', 'date', 'time']),
            ({'id': 365, 'patient_id': 4, 'date': '013-10-10', 'prescription': 'a', 'bill': 5},
             ['doctor_id', 'date', 'time', 'conclusion']),
        )
        for endpoint, case in zip(self.endpoints_1, cases):
            with self.subTest(endpoint):
                response = self.client.post(url_for(endpoint), json=case[0], headers=self.api_auth)
                self.assertStatus(response, 422)
                errors = response.json['errors']
                if case[1]:
                    for key in case[1]:
                        self.assertIsNotNone(errors.get(key))
                else:
                    self.assertIsInstance(errors, str)

    def test_put_wrong_data(self):
        cases = (
            ({'id': 1, 'uu': 'Somebody', 'email': 'once'},
             ['uu']),
            ({'fu': 'the world', 'spe': 'is gonna'},
             ['fu', 'spe']),
            ({'phone_number': '380000000003', 'name': 'Slave'},
             []),
            ({'doctor_id': 0, 'time': '75:00:00'},
             ['time']),
            ({'date': '013-10-10', 'time': '75:00:00', 'aoa': 'oao'},
             ['date', 'time', 'aoa']),
        )
        for endpoint, case in zip(self.endpoints_2, cases):
            with self.subTest(endpoint):
                response = self.client.put(url_for(endpoint, id=2), json=case[0],
                                           headers=self.api_auth)
                self.assertStatus(response, 422)
                errors = response.json['errors']
                if case[1]:
                    for key in case[1]:
                        self.assertIsNotNone(errors.get(key))
                else:
                    self.assertIsInstance(errors, str)
