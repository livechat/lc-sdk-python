''' Tests for Billing API client. '''

# pylint: disable=E1120,W0621

import pytest

from livechat.billing.base import BillingApi
from livechat.config import CONFIG

billing_url = CONFIG.get('billing_url')
billing_version = CONFIG.get('billing_version')


@pytest.fixture
def billing_api_client():
    ''' Fixture returning Billing API client. '''
    return BillingApi.get_client(token='test')


def test_get_client_without_args():
    ''' Test if TypeError raised without args. '''
    with pytest.raises(TypeError) as exception:
        BillingApi.get_client()
    assert str(
        exception.value
    ) == "get_client() missing 1 required positional argument: 'token'"


def test_get_client_without_access_token():
    ''' Test if TypeError raised without access_token. '''
    with pytest.raises(TypeError) as exception:
        BillingApi.get_client(version='test')
    assert str(
        exception.value
    ) == "get_client() missing 1 required positional argument: 'token'"


def test_get_client_with_non_existing_version():
    ''' Test if ValueError raised for non-existing version. '''
    with pytest.raises(ValueError) as exception:
        BillingApi.get_client(token='test', version='test')
    assert str(exception.value) == 'Provided version does not exist.'


def test_get_client_with_valid_args(billing_api_client):
    ''' Test if production API URL is used and token is added to headers for valid args. '''
    assert billing_api_client.api_url == f'https://{billing_url}/v{billing_version}'
    assert billing_api_client.session.headers.get('Authorization') == 'test'


def test_send_request(billing_api_client):
    ''' Test if it's possible to send a basic request via Billing API
        client with arbitrary chosen method. '''
    assert billing_api_client.create_direct_charge().json() == {
        'error':
        'invalid_request',
        'error_description':
        'The request is missing a required parameter, includes an invalid parameter value, includes a parameter more than once, or is otherwise malformed.'
    }


def test_modify_header(billing_api_client):
    ''' Test if Billing API object header can be updated with custom value. '''
    assert 'test' not in billing_api_client.get_headers()
    billing_api_client.modify_header({'test': '1234'})
    assert 'test' in billing_api_client.get_headers()


def test_remove_header(billing_api_client):
    ''' Test if header can be removed from Billing API object. '''
    billing_api_client.modify_header({'test2': '1234'})
    assert 'test2' in billing_api_client.get_headers()
    billing_api_client.remove_header('test2')
    assert 'test2' not in billing_api_client.get_headers()


def test_custom_headers_within_the_request(billing_api_client):
    ''' Test if custom headers can be added to the session headers
        only within the particular request. '''
    headers = {'x-test': 'enabled'}
    response = billing_api_client.create_direct_charge(headers=headers)
    assert headers.items() <= response.request.headers.items()
    assert 'x-test' not in billing_api_client.get_headers()


def test_client_supports_http_1():
    ''' Test if client supports HTTP/1.1 protocol. '''
    client = BillingApi.get_client(token='test')
    assert client.create_direct_charge().http_version == 'HTTP/1.1'
