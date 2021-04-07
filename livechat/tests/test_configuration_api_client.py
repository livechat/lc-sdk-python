''' Tests for Configuration API client. '''

# pylint: disable=E1120,W0621

import pytest

from livechat.configuration.client import ConfigurationApi


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
    assert conf_api_client.api_url == 'https://api.livechatinc.com/v3.3/configuration/action'
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
    assert 'Test' not in conf_api_client.get_headers()
    conf_api_client.modify_header({'Test': '1234'})
    assert 'Test' in conf_api_client.get_headers()


def test_remove_header(conf_api_client):
    ''' Test if header can be removed from configuration-api object. '''
    conf_api_client.modify_header({'Test2': '1234'})
    assert 'Test2' in conf_api_client.get_headers()
    conf_api_client.remove_header('Test2')
    assert 'Test2' not in conf_api_client.get_headers()
