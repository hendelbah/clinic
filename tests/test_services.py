# pylint: disable=missing-function-docstring, missing-module-docstring, missing-class-docstring
from datetime import date, timedelta

from flask_sqlalchemy import Pagination

from clinic_app.service import \
    DoctorService, UserService, PatientService, BookedAppointmentService, ServedAppointmentService
from tests.base_test_case import BaseTestCase


class TestAllServices(BaseTestCase):
    services = (UserService,
                DoctorService,
                PatientService,
                BookedAppointmentService,
                ServedAppointmentService,)

    def test_get_filtered_pagination(self):
        cases = (
            ([{'email': 'doctor_001@spam.ua'}, 1],
             [{'doctor_id': 1}, 1],
             [{'uuid': '91'}, 1],
             ),
            ([{'search_name': 'Геннад'}, 1],
             [{'no_user': True}, 0],
             ),
            ([{'phone_number': '380000000012'}, 1],
             [{'name': 'giga'}, 0],
             [{'surname': 'chad'}, 0],
             ),
            ([{'doctor_id': 2}, 6],
             [{'patient_id': 4}, 1],
             [{'date': date.today() + timedelta(days=20)}, 1],
             [{'past_only': True}, 20],
             ),
            ([{'doctor_id': 5}, 7],
             [{'patient_id': 7}, 1],
             [{'date_from': date.today() - timedelta(days=50)}, 30],
             [{'date_to': date.today() - timedelta(days=50)}, 71],
             # date_from > date_to:
             [{'date_from': date.today(), 'date_to': date.today() - timedelta(days=2)}, 0],
             ),
        )
        for service, bundle in zip(self.services, cases):
            for kwargs, total in bundle:
                with self.subTest(f'{service.__name__}:{list(kwargs.keys())[0]}'):
                    pagination = service.get_filtered_pagination(**kwargs)
                    self.assertIsInstance(pagination, Pagination)
                    self.assertEqual(pagination.total, total)
        self.assertEqual(pagination.page, 1)
        self.assertEqual(pagination.per_page, 20)
        pagination = PatientService.get_filtered_pagination(page=5, per_page=5)
        self.assertEqual(len(pagination.items), 5)
        self.assertEqual(pagination.page, 5)

    def test_get_instance(self):
        for service, model in zip(self.services, self.models.values()):
            with self.subTest(service.__name__):
                instance = service.get_or_404(5)
                self.assertIsInstance(instance, model)
                self.assertEqual(instance.id, 5)
                self.assertTrue(repr(instance).startswith(f'<{model.__name__}('))

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
