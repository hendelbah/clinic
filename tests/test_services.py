# pylint: disable=missing-function-docstring, missing-module-docstring, missing-class-docstring
from datetime import date, timedelta

from flask_sqlalchemy import Pagination

from clinic_app.service import DoctorService, UserService, PatientService, AppointmentService
from tests.base_test_case import BaseTestCase


class TestAllServices(BaseTestCase):
    services = (UserService,
                DoctorService,
                PatientService,
                AppointmentService,)

    def test_get_pagination(self):
        today = date.today()
        cases = (
            ([{'email': 'doctor_001@spam.ua'}, 1],
             ),
            ([{'search_name': 'Геннад'}, 1],
             [{'no_user': True}, 0],
             ),
            ([{'phone': '380000000012'}, 1],
             [{'name': 'giga'}, 0],
             [{'surname': 'chad'}, 0],
             [{'patronymic': 'orewa'}, 0],
             ),
            ([{'doctor_uuid': '2'}, 12],
             [{'patient_uuid': '4'}, 2],
             [{'date_from': today}, 81],
             [{'date_to': today}, 120],
             [{'date_from': today, 'date_to': today}, 1],
             [{'unfilled': True}, 20],
             ),
        )
        for service, bundle in zip(self.services, cases):
            for kwargs, total in bundle:
                with self.subTest(f'{service.__name__}:{list(kwargs.keys())[0]}'):
                    pagination = service.get_pagination(**kwargs)
                    self.assertIsInstance(pagination, Pagination)
                    self.assertEqual(pagination.total, total)
        self.assertEqual(pagination.page, 1)
        self.assertEqual(pagination.per_page, 20)
        pagination = PatientService.get_pagination(page=5, per_page=5)
        self.assertEqual(len(pagination.items), 5)
        self.assertEqual(pagination.page, 5)

    def test_get_instance(self):
        for service, model in zip(self.services, self.models.values()):
            with self.subTest(service.__name__):
                instance = service.get_or_404('5')
                self.assertIsInstance(instance, model)
                self.assertEqual(instance.id, 5)
                self.assertTrue(repr(instance).startswith(f'<{model.__name__}('))

    def test_appointment_get_count(self):
        kwargs = {'date_from': date.today() - timedelta(days=80),
                  'date_to': date.today() + timedelta(days=60)}
        count = AppointmentService.get_count(**kwargs)
        self.assertEqual(count, 140)

    def test_appointment_get_income(self):
        kwargs = {'date_from': date.today() - timedelta(days=70),
                  'date_to': date.today() - timedelta(days=30)}
        count = AppointmentService.get_income(**kwargs)
        self.assertEqual(count, 6150)
