''' Tests for Agent Web API client. '''

# pylint: disable=E1120,W0621

from configparser import ConfigParser

import pytest

from livechat.agent.web.client import AgentWeb

config = ConfigParser()
config.read('configs/main.ini')
stable_version = config.get('api', 'stable')
api_url = config.get('api', 'url')
ACCESS_TOKEN_INVALID = 'foo'


@pytest.fixture
def agent_web_api_client():
    ''' Fixture returning Agent Web API client. '''
    return AgentWeb.get_client(access_token=ACCESS_TOKEN_INVALID)


def test_get_client_without_args():
    ''' Test if TypeError raised without args. '''
    with pytest.raises(TypeError) as exception:
        AgentWeb.get_client()
    assert str(
        exception.value
    ) == "get_client() missing 1 required positional argument: 'access_token'"


def test_get_client_without_access_token():
    ''' Test if TypeError raised without access_token. '''
    with pytest.raises(TypeError) as exception:
        AgentWeb.get_client(version='test')
    assert str(
        exception.value
    ) == "get_client() missing 1 required positional argument: 'access_token'"


def test_get_client_with_non_existing_version():
    ''' Test if ValueError raised for non-existing version. '''
    with pytest.raises(ValueError) as exception:
        AgentWeb.get_client(access_token='test', version='2.9')
    assert str(exception.value) == 'Provided version does not exist.'


def test_get_client_with_valid_args(agent_web_api_client):
    ''' Test if production API URL is used and token is added to headers for valid args. '''
    assert agent_web_api_client.api_url == f'https://{api_url}/v{stable_version}/agent/action'
    assert agent_web_api_client.session.headers.get(
        'Authorization') == ACCESS_TOKEN_INVALID


def test_send_request(agent_web_api_client):
    ''' Test if it's possible to send a basic request via Agent Web API
        client. '''
    assert agent_web_api_client.list_chats().json() == {
        'error': {
            'type': 'authentication',
            'message': 'Invalid access token'
        }
    }


def test_modify_header(agent_web_api_client):
    ''' Test if agent object header can be updated with custom value. '''
    assert 'test' not in agent_web_api_client.get_headers()
    agent_web_api_client.modify_header({'test': '1234'})
    assert 'test' in agent_web_api_client.get_headers()


def test_remove_header(agent_web_api_client):
    ''' Test if header can be removed from agent object. '''
    agent_web_api_client.modify_header({'test2': '1234'})
    assert 'test2' in agent_web_api_client.get_headers()
    agent_web_api_client.remove_header('test2')
    assert 'test2' not in agent_web_api_client.get_headers()


def test_custom_headers_within_the_request(agent_web_api_client):
    ''' Test if custom headers can be added to the session headers
        only within the particular request. '''
    headers = {'x-test': 'enabled'}
    response = agent_web_api_client.start_chat(headers=headers)
    assert headers.items() <= response.request.headers.items()
    assert 'x-test' not in agent_web_api_client.get_headers()


def test_client_supports_http_1():
    ''' Test if client supports HTTP/1.1 protocol. '''
    client = AgentWeb.get_client(access_token=ACCESS_TOKEN_INVALID)
    assert client.list_chats().http_version == 'HTTP/1.1'


def test_client_supports_http_2():
    ''' Test if client supports HTTP/2 protocol. '''
    client = AgentWeb.get_client(access_token=ACCESS_TOKEN_INVALID, http2=True)
    assert client.list_chats().http_version == 'HTTP/2'
