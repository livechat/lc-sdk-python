''' Tests for Customer RTM client. '''

# pylint: disable=E1120,W0621,C0103

import pytest

from livechat.config import CONFIG
from livechat.customer.rtm.base import CustomerRTM

stable_version = CONFIG.get('stable')
dev_version = CONFIG.get('dev')
api_url = CONFIG.get('url')

ORGANIZATION_ID = '30007dab-4c18-4169-978d-02f776e476a5'


def test_get_client_with_non_existing_version():
    ''' Test if ValueError raised for non-existing version. '''
    with pytest.raises(ValueError) as exception:
        CustomerRTM.get_client(organization_id=ORGANIZATION_ID, version='2.9')
    assert str(exception.value) == 'Provided version does not exist.'


def test_get_client():
    ''' Test if created client opens and closes socket in default url. '''
    client = CustomerRTM.get_client(organization_id=ORGANIZATION_ID)
    client.ws.open()
    opened_state = client.ws.keep_running
    client_url = client.ws.url
    client.ws.close()
    closed_state = client.ws.keep_running
    assert client_url == f'wss://{api_url}/v{stable_version}/customer/rtm/ws?organization_id={ORGANIZATION_ID}', 'Incorrect WS address.'
    assert opened_state is True, 'Client did not open socket.'
    assert closed_state is False, 'Client did not close socket.'


def test_client_logs_in_with_token():
    ''' Test if created client can send request. '''
    client = CustomerRTM.get_client(organization_id=ORGANIZATION_ID)
    client.ws.open()
    response = client.login(token='Bearer 10386012')
    client.ws.close()
    assert response.payload == {
        'error': {
            'type': 'authentication',
            'message': 'Invalid access token'
        }
    }, 'Request was not sent.'


def test_client_logs_in_with_payload():
    ''' Test if created client can send request. '''
    client = CustomerRTM.get_client(organization_id=ORGANIZATION_ID)
    client.ws.open()
    response = client.login(
        payload={
            'customer_page': {
                'url': 'https://www.livechatinc.com',
                'title':
                'LiveChat | Live Chat Software and Chat Support Software'
            },
            'token': 'Bearer 10386012'
        })
    client.ws.close()
    assert response.payload == {
        'error': {
            'type': 'authentication',
            'message': 'Invalid access token'
        }
    }, 'Request was not sent.'


def test_rtm_response_structure():
    ''' Test if returned `RtmResponse` structure contains expected properties. '''
    client = CustomerRTM.get_client(organization_id=ORGANIZATION_ID)
    client.ws.open()
    response = client.login(token='Bearer 10386012')
    client.ws.close()
    assert isinstance(response.request_id,
                      str) and len(response.request_id) >= 1
    assert response.action == 'login'
    assert response.type == 'response'
    assert response.success is False
    assert isinstance(response.payload, dict)
