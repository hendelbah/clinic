# pylint: disable=missing-function-docstring, missing-module-docstring, missing-class-docstring
from clinic_app.service.population import clear_tables, populate
from tests.base_test_case import BaseTestCase


class TestPopulation(BaseTestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def test_populate(self):
        populate()
        counts = (18, 17, 100, 100, 100)
        for model, count in zip(self.models.values(), counts):
            with self.subTest(model.__name__):
                self.assertEqual(model.query.count(), count)

    def test_clear_tables(self):
        clear_tables()
        for model in self.models.values():
            with self.subTest(model.__name__):
                self.assertEqual(model.query.count(), 0)
