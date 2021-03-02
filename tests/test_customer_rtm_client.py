''' Tests for Customer RTM client. '''

# pylint: disable=E1120,W0621,C0103

import pytest

from customer.rtm.client import CustomerRTM

LICENSE_ID = 10386012


def test_get_client_without_args():
    ''' Test if ValueError raised without args. '''
    with pytest.raises(ValueError) as exception:
        CustomerRTM.get_client()
    assert str(
        exception.value
    ) == 'Pipe was not opened. Something`s wrong with your `license_id`.'


def test_get_client_with_incorrect_license_id_type():
    ''' Test if ValueError raised with incorrect `license_id` type. '''
    with pytest.raises(ValueError) as exception:
        CustomerRTM.get_client(license_id='Not integer')
    assert str(
        exception.value
    ) == 'Pipe was not opened. Something`s wrong with your `license_id`.'


def test_get_client_with_non_existing_version():
    ''' Test if ValueError raised for non-existing version. '''
    with pytest.raises(ValueError) as exception:
        CustomerRTM.get_client(license_id=LICENSE_ID, version='2.9')
    assert str(exception.value) == 'Provided version does not exist.'


def test_get_client():
    ''' Test if created client opens and closes socket in default url. '''
    client = CustomerRTM.get_client(license_id=LICENSE_ID)
    opened_state = client.ws.keep_alive
    client_url = client.ws.url
    client.close_connection()
    closed_state = client.ws.keep_alive
    assert client_url == f'wss://api.livechatinc.com/v3.3/customer/rtm/ws?license_id={LICENSE_ID}', 'Incorrect WS address.'
    assert opened_state is True, 'Client did not open socket.'
    assert closed_state is False, 'Client did not close socket.'


def test_client_logs_in_with_token():
    ''' Test if created client can send request. '''
    client = CustomerRTM.get_client(license_id=LICENSE_ID)
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
    client = CustomerRTM.get_client(license_id=LICENSE_ID)
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
