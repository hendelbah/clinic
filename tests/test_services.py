# pylint: disable=missing-function-docstring, missing-module-docstring, missing-class-docstring
from datetime import date, timedelta

from flask_sqlalchemy import Pagination

from clinic_app.service import \
    DoctorService, UserService, PatientService, BookedAppointmentService, ServedAppointmentService
from tests.base_test_case import BaseTestCase


class TestAllServices(BaseTestCase):

    def test_get_filtered_pagination(self):
        cases = (
            (UserService, {'email': 'doctor_001@spam.ua', 'doctor_id': 1}, 1),
            (DoctorService, {'search_name': 'Геннад'}, 1),
            (PatientService, {'phone_number': '380000000012'}, 1),
            (BookedAppointmentService, {'past_only': True}, 19),
            (ServedAppointmentService, {'date_from': date.today() - timedelta(days=50)}, 30)
        )
        for service, kwargs, total in cases:
            with self.subTest(service.__name__):
                pagination = service.get_filtered_pagination(**kwargs)
                self.assertIsInstance(pagination, Pagination)
                self.assertEqual(pagination.total, total)
        self.assertEqual(pagination.page, 1)
        self.assertEqual(pagination.per_page, 20)
        pagination = PatientService.get_filtered_pagination(page=5, per_page=5)
        self.assertEqual(len(pagination.items), 5)
        self.assertEqual(pagination.page, 5)

    def test_served_app_get_filtered_count(self):
        kwargs = {'date_from': date.today() - timedelta(days=80),
                  'date_to': date.today() - timedelta(days=60)}
        count = ServedAppointmentService.get_filtered_count(**kwargs)
        self.assertEqual(count, 21)

    def test_served_app_get_filtered_income(self):
        kwargs = {'date_from': date.today() - timedelta(days=70),
                  'date_to': date.today() - timedelta(days=30)}
        count = ServedAppointmentService.get_filtered_income(**kwargs)
        self.assertEqual(count, 6150)
