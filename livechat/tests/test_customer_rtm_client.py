''' Tests for Customer RTM client. '''

# pylint: disable=E1120,W0621,C0103

from configparser import ConfigParser

import pytest

from livechat.customer.rtm.client import CustomerRTM

config = ConfigParser()
config.read('configs/main.ini')
stable_version = config.get('api', 'stable')
dev_version = config.get('api', 'dev')
api_url = config.get('api', 'url')

ORGANIZATION_ID = '30007dab-4c18-4169-978d-02f776e476a5'


def test_get_client_without_args():
    ''' Test if ValueError raised without args. '''
    with pytest.raises(ValueError) as exception:
        CustomerRTM.get_client()
    assert str(
        exception.value
    ) == 'Pipe was not opened. Please check your `organization_id` argument.'


def test_get_client_with_incorrect_organization_id_type():
    ''' Test if ValueError raised with incorrect `organization_id` type. '''
    with pytest.raises(ValueError) as exception:
        CustomerRTM.get_client(organization_id=420)
    assert str(
        exception.value
    ) == 'Pipe was not opened. Please check your `organization_id` argument.'


def test_get_client_with_non_existing_version():
    ''' Test if ValueError raised for non-existing version. '''
    with pytest.raises(ValueError) as exception:
        CustomerRTM.get_client(organization_id=ORGANIZATION_ID, version='2.9')
    assert str(exception.value) == 'Provided version does not exist.'


def test_get_client():
    ''' Test if created client opens and closes socket in default url. '''
    client = CustomerRTM.get_client(organization_id=ORGANIZATION_ID)
    client.open_connection()
    opened_state = client.ws.keep_running
    client_url = client.ws.url
    client.close_connection()
    closed_state = client.ws.keep_running
    assert client_url == f'wss://{api_url}/v{stable_version}/customer/rtm/ws?organization_id={ORGANIZATION_ID}', 'Incorrect WS address.'
    assert opened_state is True, 'Client did not open socket.'
    assert closed_state is False, 'Client did not close socket.'


def test_client_logs_in_with_token():
    ''' Test if created client can send request. '''
    client = CustomerRTM.get_client(organization_id=ORGANIZATION_ID)
    client.open_connection()
    response = client.login(token='Bearer 10386012')
    client.close_connection()
    assert response['response']['payload'] == {
        'error': {
            'type': 'authentication',
            'message': 'Invalid access token'
        }
    }, 'Request was not sent.'


def test_client_logs_in_with_payload():
    ''' Test if created client can send request. '''
    client = CustomerRTM.get_client(organization_id=ORGANIZATION_ID)
    client.open_connection()
    response = client.login(
        payload={
            'customer_page': {
                'url': 'https://www.livechatinc.com',
                'title':
                'LiveChat | Live Chat Software and Chat Support Software'
            },
            'token': 'Bearer 10386012'
        })
    client.close_connection()
    assert response['response']['payload'] == {
        'error': {
            'type': 'authentication',
            'message': 'Invalid access token'
        }
    }, 'Request was not sent.'
