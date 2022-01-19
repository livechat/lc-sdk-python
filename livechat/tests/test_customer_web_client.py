''' Tests for Customer Web API client. '''

# pylint: disable=E1120,W0621

from configparser import ConfigParser

import pytest

from livechat.customer.web.client import CustomerWeb

config = ConfigParser()
config.read('configs/main.ini')
stable_version = config.get('api_versions', 'stable')
organization_id = '30007dab-4c18-4169-978d-02f776e476a5'
invalid_access_token = 'foo'


@pytest.fixture
def customer_web_api_client():
    ''' Fixture returning Customer Web API client. '''
    return CustomerWeb.get_client(organization_id=organization_id,
                                  access_token=invalid_access_token)


def test_get_client_without_args():
    ''' Test if ValueError raised without args. '''
    with pytest.raises(ValueError) as exception:
        CustomerWeb.get_client()
    assert str(
        exception.value) == 'Something`s wrong with your `access_token`.'


def test_get_client_with_incorrect_organization_id_type():
    ''' Test if ValueError raised with incorrect `organization_id` type. '''
    with pytest.raises(ValueError) as exception:
        CustomerWeb.get_client(organization_id=123, access_token='test')
    assert str(
        exception.value) == 'Something`s wrong with your `organization_id`.'


def test_get_client_without_access_token():
    ''' Test if ValueError raised without `access_token`. '''
    with pytest.raises(ValueError) as exception:
        CustomerWeb.get_client(organization_id=organization_id)
    assert str(
        exception.value) == 'Something`s wrong with your `access_token`.'


def test_get_client_with_non_existing_version():
    ''' Test if ValueError raised for non-existing version. '''
    with pytest.raises(ValueError) as exception:
        CustomerWeb.get_client(organization_id=organization_id,
                               access_token='test',
                               version='9.9')
    assert str(exception.value) == 'Provided version does not exist.'


def test_get_client_with_valid_args(customer_web_api_client):
    ''' Test if production API URL is used and token is added to headers for valid args. '''
    assert customer_web_api_client.api_url == f'https://api.livechatinc.com/v{stable_version}/customer/action'
    assert customer_web_api_client.organization_id == organization_id
    assert customer_web_api_client.session.headers.get(
        'Authorization') == invalid_access_token


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
