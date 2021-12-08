import typing as t

from flask import current_app, url_for


class BaseApiController:
    Method = t.Literal['GET', 'POST', 'PUT', 'DELETE']

    def __init__(self, endpoint: str):
        self._endpoint = endpoint

    @property
    def _api_key(self):
        return current_app.config['API_KEY']

    @property
    def _client(self):
        return current_app.test_client()

    def _request_api(self, method: Method, url_args: dict = None, headers: dict = None, **kwargs):
        if url_args is None:
            url_args = {}
        if headers is None:
            headers = {'api-key': self._api_key}
        else:
            headers['api-key'] = self._api_key
        kwargs['headers'] = headers
        kwargs['method'] = method
        return self._client.open(url_for(self._endpoint, **url_args), **kwargs)


class ItemApiController(BaseApiController):
    Endpoint = t.Literal['api.user', 'api.doctor', 'api.patient', 'api.booked_appointment',
                         'api.served_appointment']

    def __init__(self, endpoint: Endpoint):
        super().__init__(endpoint)

    def get(self, id_: int):
        return self._request_api('GET', {'id': id_})

    def put(self, id_: int, **data):
        if len(data) == 1 and isinstance(data.get('data'), dict):
            data = data['data']
        return self._request_api('PUT', {'id': id_}, json=data)

    def delete(self, id_: int):
        return self._request_api('DELETE', {'id': id_})


class CollectionApiController(BaseApiController):
    Endpoint = t.Literal['api.users', 'api.doctors', 'api.patients', 'api.booked_appointments',
                         'api.served_appointments']

    def __init__(self, endpoint: Endpoint):
        super().__init__(endpoint)

    def get(self, **filters):
        return self._request_api('GET', filters)

    def post(self, **data):
        if len(data) == 1 and isinstance(data.get('data'), dict):
            data = data['data']
        return self._request_api('POST', json=data)
