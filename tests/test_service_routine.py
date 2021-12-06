# pylint: disable=missing-function-docstring, missing-module-docstring, missing-class-docstring
from unittest import TestCase
from unittest.mock import patch, Mock

from sqlalchemy.exc import DatabaseError, IntegrityError
from sqlalchemy.orm import Query
from werkzeug.exceptions import NotFound

from clinic_app.service import ServiceRoutine, handle_db_errors
from tests.base_test_case import BaseTestCase

User = BaseTestCase.models['user']


# pylint: disable=protected-access
class TestServiceRoutine(BaseTestCase):
    service = ServiceRoutine

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.service.model = User

    def test_filter_by(self):
        self.assertRaises(NotImplementedError, self.service._filter_by)

    def test_order(self):
        self.assertRaises(AttributeError, self.service._order)
        self.service.order_by = ()
        self.assertIsInstance(self.service._order(), Query)

    def test_get_or_404(self):
        user = self.service.get_or_404(id_=1)
        self.assertIsInstance(user, User)
        self.assertEqual(user.id, 1)
        self.assertRaises(NotFound, self.service.get_or_404, id_=0)

    def test_exists(self):
        self.assertTrue(self.service.exists(id_=1))
        self.assertFalse(self.service.exists(id_=0))

    def test_get_filtered_pagination(self):
        self.assertRaises(NotImplementedError, self.service.get_filtered_pagination)

    @patch.object(BaseTestCase.db.session, 'commit')
    def test_delete(self, mock):
        self.assertIsNotNone(User.query.get(15))
        self.service.delete(id_=15)
        self.assertIsNone(User.query.get(15))
        mock.assert_called_with()

    @patch.object(BaseTestCase.db.session, 'commit')
    def test_commit(self, mock):
        self.service.commit()
        mock.assert_called_with()

    @patch.object(BaseTestCase.db.session, 'commit')
    def test_save(self, mock):
        self.assertIsNone(User.query.get(30))
        user = User(doctor_id=None, uuid='qwerty', email='email@spam.net',
                    password_hash='12345678', is_admin=False, id=30)
        self.service.save(user)
        self.assertIsNotNone(User.query.get(30))
        mock.assert_called_with()


class TestHandleErrors(TestCase):

    def test_plain_exception(self):
        mock = Mock(side_effect=Exception)
        decorated = handle_db_errors(mock)
        self.assertRaises(Exception, decorated)
        mock.assert_called()

    def test_database_errors(self):
        errors = (DatabaseError, IntegrityError)
        # some 'orig' object for DatabaseError initialization
        orig = Mock()
        orig.args = (0, 'Oh no..')
        for error in errors:
            with self.subTest(error.__name__):
                mock = Mock(side_effect=error(0, 0, orig))
                decorated = handle_db_errors(mock)
                response, code = decorated()
                self.assertEqual(response['errors'], 'Oh no..')
                self.assertEqual(code, 422)
