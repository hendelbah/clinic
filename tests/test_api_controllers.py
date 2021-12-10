# pylint: disable=missing-function-docstring, missing-module-docstring, missing-class-docstring
from unittest.mock import patch

from flask import url_for

from clinic_app.views.api_controllers import \
    BaseApiController, ItemApiController, CollectionApiController, ApiHelper
from tests.base_test_case import BaseTestCase


# pylint: disable=protected-access
class TestApiControllers(BaseTestCase):
    def test_base_api_controller(self):
        controller = BaseApiController('api.user')
        key = self.app.config['API_KEY']
        self.assertEqual(controller._api_key, key)
        self.assertIsInstance(controller._client, self.client.__class__)
        with patch.object(controller._client, 'open') as meth:
            controller._request_api('GET', {'uuid': 1}, headers={'a': 1})
        meth.assert_called_with(url_for('api.user', uuid=1), method='GET',
                                headers={'a': 1, 'api-key': key})

    def test_item_api_controller(self):
        controller = ItemApiController('api.user')
        key = self.app.config['API_KEY']
        with patch.object(controller._client, 'open') as meth:
            controller.get('1')
            meth.assert_called_with(url_for('api.user', uuid=1), method='GET',
                                    headers={'api-key': key})
            controller.put('1', email='asd')
            meth.assert_called_with(url_for('api.user', uuid=1), method='PUT',
                                    headers={'api-key': key}, json={'email': 'asd'})
            controller.delete('1')
            meth.assert_called_with(url_for('api.user', uuid=1), method='DELETE',
                                    headers={'api-key': key})

    def test_collection_api_controller(self):
        controller = CollectionApiController('api.users')
        key = self.app.config['API_KEY']
        with patch.object(controller._client, 'open') as meth:
            controller.get(email='asd', page=1)
            meth.assert_called_with(url_for('api.users', email='asd', page=1), method='GET',
                                    headers={'api-key': key})
            controller.post(data={'email': 'asd', 'password_hash': 'zxc'})
            meth.assert_called_with(url_for('api.users'), method='POST', headers={'api-key': key},
                                    json={'email': 'asd', 'password_hash': 'zxc'})

    def test_api_helper(self):
        with patch.object(ApiHelper.user, '_request_api') as meth:
            ApiHelper.user.get(1)
        meth.assert_called_with('GET', {'uuid': 1})
        with patch.object(ApiHelper.appointments, '_request_api') as meth:
            ApiHelper.appointments.post(doctor_id=1, patient_id=2)
        meth.assert_called_with('POST', json={'doctor_id': 1, 'patient_id': 2})
        self.assertIsNotNone(ApiHelper.patient)
