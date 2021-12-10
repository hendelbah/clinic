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
    Endpoint = t.Literal['api.user', 'api.doctor', 'api.patient', 'api.appointment']

    def __init__(self, endpoint: Endpoint):
        """
        :param endpoint: endpoint for controller instance
        """
        super().__init__(endpoint)

    def get(self, uuid: str):
        """
        Make GET request.

        :param uuid: resource id
        """
        return self._request_api('GET', {'uuid': uuid})

    def put(self, uuid: str, **data):
        """
        Make PUT request.

        :param uuid: resource id
        :param data: resource fields to update
        :return: response
        """
        if len(data) == 1 and isinstance(data.get('data'), dict):
            data = data['data']
        return self._request_api('PUT', {'uuid': uuid}, json=data)

    def delete(self, uuid: str):
        """
        Make DELETE request.

        :param uuid: resource id
        :return: response
        """
        return self._request_api('DELETE', {'uuid': uuid})


class CollectionApiController(BaseApiController):
    """
    Controller class for making requests to endpoints with collections.
    """
    Endpoint = t.Literal['api.users', 'api.doctors', 'api.patients', 'api.appointments']

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


class StatisticsController(BaseApiController):
    """
    Controller class for making requests to api.statistics endpoint.
    """

    def __init__(self):
        super().__init__('api.statistics')

    def get(self, **filters):
        """
        Get statistics on appointments.

        :param filters: parameters for filtering data
        :return: response
        """
        return self._request_api('GET', filters)


class ApiHelper:
    """
    Helper class for interacting with API, contains all api controllers as class attributes.
    """
    user = ItemApiController('api.user')
    doctor = ItemApiController('api.doctor')
    patient = ItemApiController('api.patient')
    appointment = ItemApiController('api.appointment')
    users = CollectionApiController('api.users')
    doctors = CollectionApiController('api.doctors')
    patients = CollectionApiController('api.patients')
    appointments = CollectionApiController('api.appointments')
    stats = StatisticsController()
