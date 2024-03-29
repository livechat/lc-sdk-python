''' Tests for Agent RTM client. '''

# pylint: disable=E1120,W0621,C0103

import pytest

from livechat.agent.rtm.base import AgentRTM
from livechat.config import CONFIG

stable_version = CONFIG.get('stable')
api_url = CONFIG.get('url')


def test_get_client_with_non_existing_version():
    ''' Test if ValueError raised for non-existing version. '''
    with pytest.raises(ValueError) as exception:
        AgentRTM.get_client(version='2.9')
    assert str(exception.value) == 'Provided version does not exist.'


def test_get_client():
    ''' Test if created client opens and closes socket in default url. '''
    client = AgentRTM.get_client()
    client.open_connection()
    opened_state = client.ws.keep_running
    client_url = client.ws.url
    client.close_connection()
    closed_state = client.ws.keep_running
    assert client_url == f'wss://{api_url}/v{stable_version}/agent/rtm/ws', 'Incorrect WS address.'
    assert opened_state is True, 'Client did not open socket.'
    assert closed_state is False, 'Client did not close socket.'


def test_client_logs_in_with_token():
    ''' Test if created client can send request. '''
    client = AgentRTM.get_client()
    client.open_connection()
    response = client.login(token='Bearer 10386012')
    client.close_connection()
    assert response.payload == {
        'error': {
            'type': 'authentication',
            'message': 'Invalid access token'
        }
    }, 'Request was not sent.'


def test_client_logs_in_with_payload():
    ''' Test if created client can send request. '''
    client = AgentRTM.get_client()
    client.open_connection()
    response = client.login(payload={
        'customer_monitoring_level': 'online',
        'token': 'Bearer 10386012'
    })
    client.close_connection()
    assert response.payload == {
        'error': {
            'type': 'authentication',
            'message': 'Invalid access token'
        }
    }, 'Request was not sent.'


def test_rtm_response_structure():
    ''' Test if returned `RtmResponse` structure contains expected properties. '''
    client = AgentRTM.get_client()
    client.open_connection()
    response = client.login(token='Bearer 10386012')
    client.close_connection()
    assert isinstance(response.request_id,
                      str) and len(response.request_id) >= 1
    assert response.action == 'login'
    assert response.type == 'response'
    assert response.success is False
    assert isinstance(response.payload, dict)
