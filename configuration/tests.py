''' Tests for Configuration API client. '''

import pytest

from configuration.client import ConfigurationApi


@pytest.fixture
def conf_api_client():
    ''' Fixture returning Configuration API client. '''
    return ConfigurationApi.get_api_client(token='test', version='3.3')


def test_get_api_client_without_args():
    ''' Test if TypeError raised without args. '''
    with pytest.raises(TypeError) as exception:
        ConfigurationApi.get_api_client()
    assert str(
        exception.value
    ) == "get_api_client() missing 2 required positional arguments: 'token' and 'version'"


def test_get_api_client_without_version():
    ''' Test if TypeError raised without version. '''
    with pytest.raises(TypeError) as exception:
        ConfigurationApi.get_api_client(token='test')
    assert str(
        exception.value
    ) == "get_api_client() missing 1 required positional argument: 'version'"


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


def test_get_api_client_with_non_existing_environment():
    ''' Test if production API URL is used when non-existing environment provided. '''
    version = '3.3'
    conf_api = ConfigurationApi.get_api_client(token='test',
                                               version=version,
                                               env='test')
    assert conf_api.api_url == f'https://api.livechatinc.com/v{version}/configuration/action'


@pytest.mark.parametrize('env', ['labs', 'staging'])
def test_get_api_client_with_development_environments(env):
    ''' Test if development environments are used for `labs` and `staging`. '''
    version = '3.3'
    conf_api = ConfigurationApi.get_api_client(token='test',
                                               version=version,
                                               env=env)
    assert conf_api.api_url == f'https://api.{env}.livechatinc.com/v{version}/configuration/action'


def test_send_request(conf_api_client):
    ''' Test if it's possible to send a basic request via Configuration API
        client. '''
    assert conf_api_client.get_agent().json() == {
        'error': {
            'type': 'authentication',
            'message': 'Invalid access token'
        }
    }