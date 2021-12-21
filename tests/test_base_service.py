# pylint: disable=missing-function-docstring, missing-module-docstring, missing-class-docstring
from datetime import datetime
from unittest.mock import patch, Mock

from sqlalchemy.exc import DatabaseError, IntegrityError
from sqlalchemy.orm import Query

from clinic_app.models import User
from clinic_app.service import BaseService
from tests.base_test_case import BaseTestCase


# pylint: disable=protected-access
@patch.object(BaseService, 'model', User, create=True)
class TestBaseService(BaseTestCase):

    def test_filter_by(self):
        self.assertRaises(NotImplementedError, BaseService._filter_by)

    def test_order(self):
        self.assertRaises(AttributeError, BaseService._order)
        BaseService.order_by = ()
        self.assertIsInstance(BaseService._order(), Query)

    def test_commit(self):
        with patch.object(BaseTestCase.db.session, 'commit') as method:
            result = BaseService._commit()
        self.assertIsNone(result)
        method.assert_called()
        # 'orig' object for DatabaseError initialization
        orig = Mock(args=(0, 'Oh no..'))
        errors = (DatabaseError(0, 0, orig), IntegrityError(0, 0, orig))
        for error in errors:
            with patch.object(BaseTestCase.db.session, 'commit', side_effect=error) as method:
                result = BaseService._commit()
            method.assert_called()
            self.assertEqual(result['errors'][error.__class__.__name__], 'Oh no..')
            self.assertIsNotNone(result.get('message'))

    def test_get(self):
        user = BaseService.get(uuid='1')
        self.assertIsInstance(user, User)
        self.assertEqual(user.uuid, '1')
        result = BaseService.get(uuid='asd')
        self.assertIsNone(result)

    def test_get_modified(self):
        modified = BaseService.get_modified(uuid='1')
        self.assertIsInstance(modified, datetime)
        modified = BaseService.get_modified(uuid='asd')
        self.assertIsNone(modified)

    def test_update(self):
        data = {'email': 'hello'}
        result, code = BaseService.update('7', data)
        self.assertIsInstance(result, User)
        self.assertEqual(result.email, data['email'])
        self.assertEqual(code, 200)
        email = self.db.session.query(User.email).filter_by(uuid='7').scalar()
        self.assertEqual(email, data['email'])
        # unknown uuid
        result, code = BaseService.update('qwe', data)
        self.assertEqual(code, 404)
        self.assertEqual(result, {})
        # duplicate 'doctor_uuid' filed
        result, code = BaseService.update('8', {'doctor_uuid': '8'})
        self.assertEqual(code, 422)
        self.assertIn('IntegrityError', result['errors'])
        self.assertEqual(result['message'], 'Request data violates database constraints')

    def test_create(self):
        data = {'email': 'email@spam.net', 'password_hash': '1234', 'is_admin': False}
        result, code = BaseService.create(data)
        self.assertEqual(code, 201)
        self.assertIsInstance(result, User)
        for key, value in data.items():
            self.assertEqual(getattr(result, key), value)
        # same data
        result, code = BaseService.create(data)
        self.assertEqual(code, 422)
        self.assertEqual(result['message'], 'Request data violates database constraints')
        self.assertIn('IntegrityError', result['errors'])
        # missing fields
        result, code = BaseService.create({'email': 'email@spam.net', 'password_hash': '1234'})
        self.assertEqual(code, 422)
        self.assertEqual(result['message'], 'Wrong data')
        self.assertIn('TypeError', result['errors'])

    @patch.object(BaseTestCase.db.session, 'commit')
    def test_delete(self, mock):
        result = BaseService.delete(uuid='15')
        self.assertTrue(result)
        self.assertIsNone(User.query.filter_by(uuid='15').first())
        result = BaseService.delete(uuid='15')
        self.assertFalse(result)
        mock.assert_called()

    def test_get_pagination(self):
        self.assertRaises(NotImplementedError, BaseService.get_pagination)
        self.assertRaises(NotImplementedError, BaseService.get_pagination_modified)
