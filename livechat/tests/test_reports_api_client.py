''' Tests for Reports API client. '''

# pylint: disable=E1120,W0621

import pytest

from livechat.config import CONFIG
from livechat.reports.client import ReportsApi

stable_version = CONFIG.get('stable')
api_url = CONFIG.get('url')


@pytest.fixture
def reports_api_client():
    ''' Fixture returning Reports API client. '''
    return ReportsApi.get_client(token='test')


def test_get_client_with_non_existing_version():
    ''' Test if ValueError raised for non-existing version. '''
    with pytest.raises(ValueError) as exception:
        ReportsApi.get_client(token='test', version='test')
    assert str(exception.value) == 'Provided version does not exist.'


def test_get_client_with_valid_args(reports_api_client):
    ''' Test if production API URL is used and token is added to headers for valid args. '''
    assert reports_api_client.api_url == f'https://{api_url}/v{stable_version}/reports'
    assert reports_api_client.session.headers.get('Authorization') == 'test'


def test_send_request(reports_api_client):
    ''' Test if it's possible to send a basic request via Reports API
        client with arbitrary chosen method. '''
    assert reports_api_client.total_chats().json() == {
        'error': {
            'type': 'authentication',
            'message': 'Invalid access token'
        }
    }


def test_modify_header(reports_api_client):
    ''' Test if Reports-api object header can be updated with custom value. '''
    assert 'test' not in reports_api_client.get_headers()
    reports_api_client.modify_header({'test': '1234'})
    assert 'test' in reports_api_client.get_headers()


def test_remove_header(reports_api_client):
    ''' Test if header can be removed from Reports-api object. '''
    reports_api_client.modify_header({'test2': '1234'})
    assert 'test2' in reports_api_client.get_headers()
    reports_api_client.remove_header('test2')
    assert 'test2' not in reports_api_client.get_headers()


def test_custom_headers_within_the_request(reports_api_client):
    ''' Test if custom headers can be added to the session headers
        only within the particular request. '''
    headers = {'x-test': 'enabled'}
    response = reports_api_client.total_chats(headers=headers)
    assert headers.items() <= response.request.headers.items()
    assert 'x-test' not in reports_api_client.get_headers()


def test_client_supports_http_1():
    ''' Test if client supports HTTP/1.1 protocol. '''
    client = ReportsApi.get_client(token='test')
    assert client.total_chats().http_version == 'HTTP/1.1'


def test_client_supports_http_2():
    ''' Test if client supports HTTP/2 protocol. '''
    client = ReportsApi.get_client(token='test', http2=True)
    assert client.total_chats().http_version == 'HTTP/2'
