''' Tests for Agent Web API client. '''

# pylint: disable=E1120,W0621

import pytest

from agent.web.client import AgentWeb

VALID_VERSION = '3.3'
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
    assert agent_web_api_client.api_url == 'https://api.livechatinc.com/v30.30/agent/action'
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
