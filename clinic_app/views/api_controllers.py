"""
This module contains controller classes for interaction with API.

Classes:

- `BaseApiController` base controller class, contains core methods for making requests to API.
- `ItemApiController` controller class designed for making requests to endpoints with single items.
- `CollectionApiController` controller class for making requests to endpoints with collections.
- `ApiHelper` helper class, contains all api controllers as class attributes.
"""
import typing as t

from flask import current_app, url_for


class BaseApiController:
    """
    Base controller class, contains core methods for making requests to API.
    All methods should be used inside application context.
    """
    Method = t.Literal['GET', 'POST', 'PUT', 'DELETE']

    def __init__(self, endpoint: str):
        """
        :param endpoint: endpoint for controller instance
        """
        self._endpoint = endpoint
        self.__client = None

    @property
    def _api_key(self):
        """
        Returns API_KEY from current app
        """
        return current_app.config['API_KEY']

    @property
    def _client(self):
        """
        Returns test client from current app
        """
        if self.__client is None:
            self.__client = current_app.test_client()
        return self.__client

    def _request_api(self, method: Method, url_args: dict = None, headers: dict = None, **kwargs):
        """
        Make authorized request to api.

        :param method: http method
        :param url_args: parameters for adding to url
        :param headers: additional request headers
        :param kwargs: kwargs for test_client.open method
        :return: response
        """
        if url_args is None:
            url_args = {}
        kwargs['method'] = method
        if headers is None:
            headers = {'api-key': self._api_key}
        else:
            headers['api-key'] = self._api_key
        kwargs['headers'] = headers
        return self._client.open(url_for(self._endpoint, **url_args), **kwargs)


class ItemApiController(BaseApiController):
    """
    Controller class for making requests to endpoints with single items.
    """
    Endpoint = t.Literal['api.user', 'api.doctor', 'api.patient', 'api.booked_appointment',
                         'api.served_appointment']

    def __init__(self, endpoint: Endpoint):
        """
        :param endpoint: endpoint for controller instance
        """
        super().__init__(endpoint)

    def get(self, id_: int):
        """
        Make GET request.

        :param id_: resource id
        """
        return self._request_api('GET', {'id': id_})

    def put(self, id_: int, **data):
        """
        Make PUT request.

        :param id_: resource id
        :param data: resource fields to update
        :return: response
        """
        if len(data) == 1 and isinstance(data.get('data'), dict):
            data = data['data']
        return self._request_api('PUT', {'id': id_}, json=data)

    def delete(self, id_: int):
        """
        Make DELETE request.

        :param id_: resource id
        :return: response
        """
        return self._request_api('DELETE', {'id': id_})


class CollectionApiController(BaseApiController):
    """
    Controller class for making requests to endpoints with collections.
    """
    Endpoint = t.Literal['api.users', 'api.doctors', 'api.patients', 'api.booked_appointments',
                         'api.served_appointments']

    def __init__(self, endpoint: Endpoint):
        """
        :param endpoint: endpoint for controller instance
        """
        super().__init__(endpoint)

    def get(self, page: int = None, per_page: int = None, **filters):
        """
        Make GET request.

        :param page: page parameter for pagination
        :param per_page: per_page parameter for pagination
        :param filters: parameters for filtering results
        :return: response
        """
        filters['page'] = page
        filters['per_page'] = per_page
        return self._request_api('GET', filters)

    def post(self, **data):
        """
        Make POST request.

        :param data: resource fields for inserting
        :return: response
        """
        if len(data) == 1 and isinstance(data.get('data'), dict):
            data = data['data']
        return self._request_api('POST', json=data)


class ApiHelper:
    """
    Helper class for interacting with API, contains all api controllers as class attributes.
    """
    user = ItemApiController('api.user')
    doctor = ItemApiController('api.doctor')
    patient = ItemApiController('api.patient')
    b_appointment = ItemApiController('api.booked_appointment')
    s_appointment = ItemApiController('api.served_appointment')
    users = CollectionApiController('api.users')
    doctors = CollectionApiController('api.doctors')
    patients = CollectionApiController('api.patients')
    b_appointments = CollectionApiController('api.booked_appointments')
    s_appointments = CollectionApiController('api.served_appointments')
