''' Tests for Customer Web API client. '''

# pylint: disable=E1120,W0621

import pytest

from livechat.customer.web.client import (CustomerWeb, CustomerWeb33,
                                          CustomerWeb34)

LICENSE_ID = 10386012
ORGANIZATION_ID = '30007dab-4c18-4169-978d-02f776e476a5'
STABLE_VERSION = '3.3'
DEV_PREVIEW_VERSION = '3.4'
ACCESS_TOKEN_INVALID = 'foo'


@pytest.fixture(name='stable_client')
def customer_web_api_client():
    ''' Fixture returning Customer Web API client. '''
    return CustomerWeb.get_client(license_id=LICENSE_ID,
                                  access_token=ACCESS_TOKEN_INVALID)


@pytest.fixture(name='dev_preview_client')
def customer_web_api_client_dev_preview():
    ''' Fixture returning Customer Web API client in dev-preview version. '''
    return CustomerWeb.get_client(version=DEV_PREVIEW_VERSION,
                                  organization_id=ORGANIZATION_ID,
                                  access_token=ACCESS_TOKEN_INVALID)


def test_get_client_without_args():
    ''' Test if ValueError raised without args. '''
    with pytest.raises(ValueError) as exception:
        CustomerWeb.get_client()
    assert str(
        exception.value
    ) == 'Incorrect or missing `access_token` argument (should be of type str.)'


def test_get_client_without_license_id():
    ''' Test if ValueError is raised without `license_id`. '''
    with pytest.raises(ValueError) as exception:
        CustomerWeb.get_client(access_token='foo')
    assert str(
        exception.value
    ) == 'Incorrect or missing `license_id` argument (should be of type int.)'


# TODO replace `test_get_client_without_license_id` with this when v3.4 becomes stable version.
def test_get_client_without_organization_id():
    ''' Test if ValueError is raised without `organization_id`. '''
    with pytest.raises(ValueError) as exception:
        CustomerWeb.get_client(access_token='foo', version='3.4')
    assert str(
        exception.value
    ) == 'Incorrect or missing `organization_id` argument (should be of type str.)'


def test_get_client_without_access_token():
    ''' Test if TypeError raised without access_token. '''
    with pytest.raises(ValueError) as exception:
        CustomerWeb.get_client(license_id=LICENSE_ID)
    assert str(
        exception.value
    ) == 'Incorrect or missing `access_token` argument (should be of type str.)'


def test_get_client_with_non_existing_version():
    ''' Test if ValueError raised for non-existing version. '''
    with pytest.raises(ValueError) as exception:
        CustomerWeb.get_client(license_id=LICENSE_ID,
                               access_token='test',
                               version='2.9')
    assert str(exception.value) == 'Provided version does not exist.'


def test_get_client_with_valid_args(stable_client: CustomerWeb33):
    ''' Test if production API URL is used and token is added to headers for valid args. '''
    assert stable_client.api_url == f'https://api.livechatinc.com/v{STABLE_VERSION}/customer/action'
    assert stable_client.query_string == f'?license_id={LICENSE_ID}'
    assert stable_client.session.headers.get(
        'Authorization') == ACCESS_TOKEN_INVALID


# TODO replace `test_get_client_with_valid_args` with this when v3.4 becomes stable version.
def test_get_dev_preview_client_with_valid_args(
        dev_preview_client: CustomerWeb34):
    ''' Test if production API URL is used and token is added to headers for valid args. '''
    assert dev_preview_client.api_url == f'https://api.livechatinc.com/v{DEV_PREVIEW_VERSION}/customer/action'
    assert dev_preview_client.query_string == f'?organization_id={ORGANIZATION_ID}'
    assert dev_preview_client.session.headers.get(
        'Authorization') == ACCESS_TOKEN_INVALID


def test_send_request(stable_client: CustomerWeb33):
    ''' Test if it's possible to send a basic request via Customer Web API
        client. '''
    assert stable_client.list_chats().json() == {
        'error': {
            'type': 'authentication',
            'message': 'Invalid access token'
        }
    }


# TODO replace `test_send_request` with this when v3.4 becomes stable version.
@pytest.mark.xfail(reason='Not implemented yet.')
def test_send_request_with_dev_preview_client(
        dev_preview_client: CustomerWeb34):
    ''' Test if a request can be sent using request in non-default version'''
    assert dev_preview_client.list_chats().json() == {
        'error': {
            'type': 'authentication',
            'message': 'Invalid access token'
        }
    }


def test_modify_header(stable_client):
    ''' Test if customer object header can be updated with custom value. '''
    assert 'test' not in stable_client.get_headers()
    stable_client.modify_header({'test': '1234'})
    assert 'test' in stable_client.get_headers()


def test_remove_header(stable_client):
    ''' Test if header can be removed from customer object. '''
    stable_client.modify_header({'test2': '1234'})
    assert 'test2' in stable_client.get_headers()
    stable_client.remove_header('test2')
    assert 'test2' not in stable_client.get_headers()


def test_custom_headers_within_the_request(stable_client):
    ''' Test if custom headers can be added to the session headers
        only within the particular request. '''
    headers = {'x-test': 'enabled'}
    response = stable_client.start_chat(headers=headers)
    assert headers.items() <= response.request.headers.items()
    assert 'x-test' not in stable_client.get_headers()


def test_client_supports_http_1():
    ''' Test if client supports HTTP/1.1 protocol. '''
    client = CustomerWeb.get_client(license_id=LICENSE_ID,
                                    access_token=ACCESS_TOKEN_INVALID)
    assert client.list_chats().http_version == 'HTTP/1.1'


def test_client_supports_http_2():
    ''' Test if client supports HTTP/2 protocol. '''
    client = CustomerWeb.get_client(license_id=LICENSE_ID,
                                    access_token=ACCESS_TOKEN_INVALID,
                                    http2=True)
    assert client.list_chats().http_version == 'HTTP/2'
