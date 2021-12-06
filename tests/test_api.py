# pylint: disable=missing-function-docstring, missing-module-docstring, missing-class-docstring
from flask import url_for

from tests.base_test_case import BaseTestCase


class TestApi(BaseTestCase):
    endpoints_1 = ('api.users', 'api.doctors', 'api.patients', 'api.booked_appointments',
                   'api.served_appointments')
    endpoints_2 = ('api.user', 'api.doctor', 'api.patient', 'api.booked_appointment',
                   'api.served_appointment')
    post_data = (
        {'uuid': 'Somebody', 'email': 'once', 'password_hash': 'told me', 'is_admin': True},
        {'full_name': 'the world', 'speciality': 'is gonna', 'info': 'roll me',
         'experience_years': 100},
        {'phone_number': '88005553535', 'name': 'Slave', 'surname': 'Ass',
         'patronymic': '300$', 'birthday': '2012-12-12'},
        {'patient_id': 3, 'doctor_id': 5, 'date': '2012-12-12', 'time': '16:00:00'},
        {'patient_id': 4, 'doctor_id': 5, 'date': '2013-10-10', 'time': '10:00:01',
         'conclusion': 'will die soon', 'prescription': 'submit', 'bill': 5000},
    )
    post_wrong_cases = (
        ({'id': 1, 'uuid': 'Somebody', 'email': 'once'},
         ['id', 'is_admin', 'password_hash']),
        ({'id': 1, 'full_name': 'the world', 'speciality': 'is gonna'},
         ['id', 'experience_years', 'info']),
        ({'id': 1, 'phone_number': '88005553535', 'name': 'Slave', 'surname': 'Ass'},
         ['id', 'patronymic', 'birthday']),
        ({'id': 1, 'doctor_id': 5, 'time': '75:00:00'},
         ['id', 'patient_id', 'date', 'time']),
        ({'id': 1, 'patient_id': 4, 'date': '013-10-10', 'prescription': 'a', 'bill': 5},
         ['id', 'doctor_id', 'date', 'time', 'conclusion']),
    )

    def test_all_get_200(self):
        for endpoint in self.endpoints_1:
            with self.subTest(endpoint):
                response = self.client.get(url_for(endpoint, per_page=5))
                self.assert200(response)
                self.assertEqual(len(response.json['items']), 5)
        for endpoint in self.endpoints_2 + ('api.statistics',):
            with self.subTest(endpoint):
                response = self.client.get(url_for(endpoint, id=1))
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
                response = self.client.get(url_for(endpoint, id=2))
                self.assert200(response)
                self.assertEqual(response.json['id'], 2)
                self.assertEqual(response.json[prop[0]], prop[1])

    def test_post_and_delete(self):
        ids = []
        for endpoint, item in zip(self.endpoints_1, self.post_data):
            with self.subTest(endpoint + ':POST'):
                response = self.client.post(url_for(endpoint), json=item)
                self.assertStatus(response, 201)
                ids.append(response.json['id'])
        for endpoint, id_ in zip(self.endpoints_2, ids):
            with self.subTest(endpoint + ':DELETE'):
                response = self.client.delete(url_for(endpoint, id=id_))
                self.assertStatus(response, 204)

    def test_put_new(self):
        for endpoint, item in zip(self.endpoints_2, self.post_data):
            with self.subTest(endpoint):
                response = self.client.get(url_for(endpoint, id=400))
                self.assert404(response)
                response = self.client.put(url_for(endpoint, id=400), json=item)
                self.assertStatus(response, 204)
                response = self.client.get(url_for(endpoint, id=400))
                self.assert200(response)
                self.assertEqual(response.json['id'], 400)

    def test_put_update(self):
        data = (
            {'password_hash': 'cocos_olia_jojoba', 'uuid': 'cocojambo'},
            {'full_name': 'Артем Петрович', 'experience_years': 1488},
            {'name': 'McDonald\'s', 'birthday': '1940-05-15'},
            {'date': '2025-01-01', 'time': '07:00:00'},
            {'date': '2040-12-31', 'conclusion': 'very well'},
        )
        for endpoint, item in zip(self.endpoints_2, data):
            with self.subTest(endpoint):
                response = self.client.get(url_for(endpoint, id=10))
                self.assert200(response)
                response = self.client.put(url_for(endpoint, id=10), json=item)
                self.assertStatus(response, 204)

    def test_wrong_get_and_delete(self):
        for endpoint in self.endpoints_2:
            with self.subTest(endpoint):
                response = self.client.get(url_for(endpoint, id=0))
                self.assert404(response)
                response = self.client.delete(url_for(endpoint, id=300))
                self.assert404(response)

    def test_post_wrong_data(self):
        for endpoint, case in zip(self.endpoints_1, self.post_wrong_cases):
            with self.subTest(endpoint):
                response = self.client.post(url_for(endpoint), json=case[0])
                self.assertStatus(response, 422)
                for key in case[1]:
                    self.assertIsNotNone(response.json.get(key))

    def test_put_wrong_data(self):
        for endpoint, case in zip(self.endpoints_2, self.post_wrong_cases):
            with self.subTest(endpoint):
                response = self.client.put(url_for(endpoint, id=500), json=case[0])
                self.assertStatus(response, 422)
                for key in case[1]:
                    self.assertIsNotNone(response.json.get(key))
                response = self.client.put(url_for(endpoint, id=1), json=case[0])
                self.assertStatus(response, 422)
                errs = 2 if endpoint.endswith('pointment') else 1  # there are wrong data and time
                self.assertEqual(len(response.json), errs)
                self.assertIsNotNone(response.json.get('id'))
