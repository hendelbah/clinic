# pylint: disable=missing-function-docstring, missing-module-docstring, missing-class-docstring
from flask import url_for

from tests.base_test_case import BaseTestCase


class TestApi(BaseTestCase):
    endpoints_1 = ('api.users', 'api.doctors', 'api.patients', 'api.booked_appointments',
                   'api.served_appointments')
    endpoints_2 = ('api.user', 'api.doctor', 'api.patient', 'api.booked_appointment',
                   'api.served_appointment')

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
        data = (
            {'uuid': 'Somebody', 'email': 'once', 'password_hash': 'told me', 'is_admin': True},
            {'full_name': 'the world', 'speciality': 'is gonna', 'info': 'roll me',
             'experience_years': 100},
            {'phone_number': '88005553535', 'name': 'Slave', 'surname': 'Ass',
             'patronymic': '300', 'birthday': '2012-12-12'},
            {'patient_id': 3, 'doctor_id': 5, 'date': '2012-12-12', 'time': '16:00:00'},
            {'patient_id': 4, 'doctor_id': 5, 'date': '2013-10-10', 'time': '10:00:01',
             'conclusion': 'will die soon', 'prescription': 'submit', 'bill': 5000},
        )
        ids = []
        for endpoint, item in zip(self.endpoints_1, data):
            with self.subTest(endpoint):
                response = self.client.post(url_for(endpoint), json=item)
                self.assertStatus(response, 201)
                ids.append(response.json['id'])
        for endpoint, id_ in zip(self.endpoints_2, ids):
            with self.subTest(endpoint):
                response = self.client.delete(url_for(endpoint, id=id_))
                self.assertStatus(response, 204)
