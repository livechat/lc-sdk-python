''' Tests for Configuration API client. '''

# pylint: disable=E1120,W0621

import pytest

from livechat.config import CONFIG
from livechat.configuration.base import ConfigurationApi

stable_version = CONFIG.get('stable')
api_url = CONFIG.get('url')


@pytest.fixture
def conf_api_client():
    ''' Fixture returning Configuration API client. '''
    return ConfigurationApi.get_client(token='test')


def test_get_client_without_args():
    ''' Test if TypeError raised without args. '''
    with pytest.raises(TypeError) as exception:
        ConfigurationApi.get_client()
    assert str(
        exception.value
    ) == "get_client() missing 1 required positional argument: 'token'"


def test_get_client_without_token():
    ''' Test if TypeError raised without token. '''
    with pytest.raises(TypeError) as exception:
        ConfigurationApi.get_client(version='test')
    assert str(
        exception.value
    ) == "get_client() missing 1 required positional argument: 'token'"


def test_get_client_with_non_existing_version():
    ''' Test if ValueError raised for non-existing version. '''
    with pytest.raises(ValueError) as exception:
        ConfigurationApi.get_client(token='test', version='test')
    assert str(exception.value) == 'Provided version does not exist.'


def test_get_client_with_valid_args(conf_api_client):
    ''' Test if production API URL is used and token is added to headers for valid args. '''
    assert conf_api_client.api_url == f'https://{api_url}/v{stable_version}/configuration/action'
    assert conf_api_client.session.headers.get('Authorization') == 'test'


def test_send_request(conf_api_client):
    ''' Test if it's possible to send a basic request via Configuration API
        client with arbitrary chosen method. '''
    assert conf_api_client.get_agent().json() == {
        'error': {
            'type': 'authentication',
            'message': 'Invalid access token'
        }
    }


def test_modify_header(conf_api_client):
    ''' Test if configuration-api object header can be updated with custom value. '''
    assert 'test' not in conf_api_client.get_headers()
    conf_api_client.modify_header({'test': '1234'})
    assert 'test' in conf_api_client.get_headers()


def test_remove_header(conf_api_client):
    ''' Test if header can be removed from configuration-api object. '''
    conf_api_client.modify_header({'test2': '1234'})
    assert 'test2' in conf_api_client.get_headers()
    conf_api_client.remove_header('test2')
    assert 'test2' not in conf_api_client.get_headers()


def test_custom_headers_within_the_request(conf_api_client):
    ''' Test if custom headers can be added to the session headers
        only within the particular request. '''
    headers = {'x-test': 'enabled'}
    response = conf_api_client.create_bot(headers=headers)
    assert headers.items() <= response.request.headers.items()
    assert 'x-test' not in conf_api_client.get_headers()


def test_client_supports_http_1():
    ''' Test if client supports HTTP/1.1 protocol. '''
    client = ConfigurationApi.get_client(token='test')
    assert client.create_agent().http_version == 'HTTP/1.1'


def test_client_supports_http_2():
    ''' Test if client supports HTTP/2 protocol. '''
    client = ConfigurationApi.get_client(token='test', http2=True)
    assert client.create_agent().http_version == 'HTTP/2'
