# pylint: disable=missing-function-docstring, missing-module-docstring, missing-class-docstring
from unittest.mock import patch, Mock

from sqlalchemy.exc import DatabaseError, IntegrityError
from sqlalchemy.orm import Query
from werkzeug.exceptions import NotFound, UnprocessableEntity

from clinic_app.service import BaseService
from tests.base_test_case import BaseTestCase

User = BaseTestCase.models['user']


# pylint: disable=protected-access
class TestBaseService(BaseTestCase):
    service = BaseService

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

    def test_commit(self):
        with patch.object(BaseTestCase.db.session, 'commit') as method:
            self.service._commit()
        method.assert_called()
        # some 'orig' object for DatabaseError initialization
        orig = Mock(args=(0, 'Oh no..'))
        errors = (DatabaseError(0, 0, orig), IntegrityError(0, 0, orig))
        for error in errors:
            with patch.object(BaseTestCase.db.session, 'commit', side_effect=error) as method:
                with self.assertRaises(UnprocessableEntity) as err_context:
                    self.service._commit()
            method.assert_called()
            # noinspection PyUnresolvedReferences
            exc_data = err_context.exception.data
            self.assertEqual(exc_data.get('errors'), 'Oh no..')
            self.assertIsNotNone(exc_data.get('message'))

    def test_get_or_404(self):
        user = self.service.get_or_404(id_=1)
        self.assertIsInstance(user, User)
        self.assertEqual(user.id, 1)
        self.assertRaises(NotFound, self.service.get_or_404, id_=0)

    def test_update_or_422(self):
        data = {'email': 'hello'}
        self.service.update_or_abort(7, data)
        email = self.db.session.query(User.email).filter_by(id=7).scalar()
        self.assertEqual(email, 'hello')
        self.assertRaises(UnprocessableEntity, self.service.update_or_abort, 8, data)

    def test_save_or_422(self):
        user1 = User(uuid='qwerty', email='email@spam.net', password_hash='1234')
        self.service.save_or_422(user1)
        # same email
        user2 = User(uuid='qwerty', email='email@spam.net', password_hash='12')
        self.assertRaises(UnprocessableEntity, self.service.save_or_422, model_instance=user2)

    @patch.object(service, '_commit')
    def test_delete_or_404(self, mock):
        self.service.delete_or_404(id_=15)
        self.assertIsNone(User.query.get(15))
        self.assertRaises(NotFound, self.service.delete_or_404, id_=321)
        mock.assert_called()

    def test_get_filtered_pagination(self):
        self.assertRaises(NotImplementedError, self.service.get_filtered_pagination)
