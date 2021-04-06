''' Tests for Customer Web API client. '''

# pylint: disable=E1120,W0621

import pytest

from customer.web.client import CustomerWeb

LICENSE_ID = 10386012
VALID_VERSION = '3.3'
ACCESS_TOKEN_INVALID = 'foo'


@pytest.fixture
def customer_web_api_client():
    ''' Fixture returning Customer Web API client. '''
    return CustomerWeb.get_client(license_id=LICENSE_ID,
                                  access_token=ACCESS_TOKEN_INVALID)


def test_get_client_without_args():
    ''' Test if TypeError raised without args. '''
    with pytest.raises(TypeError) as exception:
        CustomerWeb.get_client()
    assert str(
        exception.value
    ) == "get_client() missing 2 required positional arguments: 'license_id' and 'access_token'"


def test_get_client_without_license_id():
    ''' Test if TypeError raised without license_id. '''
    with pytest.raises(TypeError) as exception:
        CustomerWeb.get_client(access_token='foo')
    assert str(
        exception.value
    ) == "get_client() missing 1 required positional argument: 'license_id'"


def test_get_client_without_access_token():
    ''' Test if TypeError raised without access_token. '''
    with pytest.raises(TypeError) as exception:
        CustomerWeb.get_client(license_id=LICENSE_ID)
    assert str(
        exception.value
    ) == "get_client() missing 1 required positional argument: 'access_token'"


def test_get_client_with_non_existing_version():
    ''' Test if ValueError raised for non-existing version. '''
    with pytest.raises(ValueError) as exception:
        CustomerWeb.get_client(license_id=LICENSE_ID,
                               access_token='test',
                               version='2.9')
    assert str(exception.value) == 'Provided version does not exist.'


def test_get_client_with_valid_args(customer_web_api_client):
    ''' Test if production API URL is used and token is added to headers for valid args. '''
    assert customer_web_api_client.api_url == f'https://api.livechatinc.com/v{VALID_VERSION}/customer/action'
    assert customer_web_api_client.license_id == LICENSE_ID
    assert customer_web_api_client.session.headers.get(
        'Authorization') == ACCESS_TOKEN_INVALID


def test_send_request(customer_web_api_client):
    ''' Test if it's possible to send a basic request via Customer Web API
        client. '''
    assert customer_web_api_client.list_chats().json() == {
        'error': {
            'type': 'authentication',
            'message': 'Invalid access token'
        }
    }


def test_modify_header(customer_web_api_client):
    ''' Test if customer object header can be updated with custom value. '''
    assert 'Test' not in customer_web_api_client.get_headers()
    customer_web_api_client.modify_header({'Test': '1234'})
    assert 'Test' in customer_web_api_client.get_headers()


def test_remove_header(customer_web_api_client):
    ''' Test if header can be removed from customer object. '''
    customer_web_api_client.modify_header({'Test2': '1234'})
    assert 'Test2' in customer_web_api_client.get_headers()
    customer_web_api_client.remove_header('Test2')
    assert 'Test2' not in customer_web_api_client.get_headers()