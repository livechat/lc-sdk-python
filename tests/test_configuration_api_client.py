''' Tests for Configuration API client. '''

# pylint: disable=E1120,W0621

import pytest

from configuration.client import ConfigurationApi


@pytest.fixture
def conf_api_client():
    ''' Fixture returning Configuration API client. '''
    return ConfigurationApi.get_api_client(token='test')


def test_get_api_client_without_args():
    ''' Test if TypeError raised without args. '''
    with pytest.raises(TypeError) as exception:
        ConfigurationApi.get_api_client()
    assert str(
        exception.value
    ) == "get_api_client() missing 1 required positional argument: 'token'"


def test_get_api_client_without_token():
    ''' Test if TypeError raised without token. '''
    with pytest.raises(TypeError) as exception:
        ConfigurationApi.get_api_client(version='test')
    assert str(
        exception.value
    ) == "get_api_client() missing 1 required positional argument: 'token'"


def test_get_api_client_with_non_existing_version():
    ''' Test if ValueError raised for non-existing version. '''
    with pytest.raises(ValueError) as exception:
        ConfigurationApi.get_api_client(token='test', version='test')
    assert str(exception.value) == 'Provided version does not exist.'


def test_get_api_client_with_valid_args(conf_api_client):
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
