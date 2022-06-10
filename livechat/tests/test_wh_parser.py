''' Webhooks parser tests. '''

import pytest

from livechat.config import CONFIG
from livechat.webhooks.parser import parse_webhook

# pylint: disable=redefined-outer-name

stable_version = CONFIG.get('stable')


@pytest.fixture(scope='function')
def webhook_body() -> dict:
    ''' Returns a test webhook body in a form of a dict. '''
    return {
        'webhook_id': '166c029b-a2c6-4010-aa0c-5a984353a7dd',
        'secret_key': 'top_secret_value',
        'action': 'chat_deactivated',
        'organization_id': 'f9c7cc55-b35a-4e76-b0d5-ae9fce362314',
        'payload': {
            'chat_id': 'PJ0MRSHTDG',
            'thread_id': 'K600PKZON8'
        },
        'additional_data': {}
    }


@pytest.mark.parametrize('optional_field', [True, False])
def test_valid_webhook_parsed(
    webhook_body: dict,
    optional_field: bool,
):
    ''' Test if valid webhook body is parsed properly. '''
    if optional_field:
        webhook_body['payload'][
            'user_id'] = 'b7eff798-f8df-4364-8059-649c35c9ed0c'
    parsed_wh = parse_webhook(webhook_body)
    assert parsed_wh.webhook_id == webhook_body['webhook_id']
    assert parsed_wh.secret_key == webhook_body['secret_key']
    assert parsed_wh.action == webhook_body['action']
    assert parsed_wh.organization_id == webhook_body['organization_id']
    assert parsed_wh.additional_data == webhook_body['additional_data']
    assert parsed_wh.payload.chat_id == webhook_body['payload']['chat_id']
    assert parsed_wh.payload.thread_id == webhook_body['payload']['thread_id']
    if optional_field:
        assert parsed_wh.payload.user_id == webhook_body['payload']['user_id']
    else:
        assert parsed_wh.payload.user_id is None


def test_webhook_with_missing_fields_not_parsed(webhook_body: dict):
    ''' Test if webhook with missing fields is not parsed and proper exception
        raised. '''
    with pytest.raises(ValueError) as exception:
        del webhook_body['webhook_id']
        parse_webhook(webhook_body)
    assert 'Invalid webhook body' in str(exception.value)


def test_webhook_with_additional_fields_not_parsed(webhook_body: dict):
    ''' Test if webhook with additional fields is not parsed and proper exception
        raised. '''
    with pytest.raises(ValueError) as exception:
        webhook_body['foo'] = 'bar'
        parse_webhook(webhook_body)
    assert 'Invalid webhook body' in str(exception.value)


def test_webhook_with_invalid_action_not_parsed(webhook_body: dict):
    ''' Test if webhook with invalid `action` is not parsed and proper exception
        raised. '''
    action = 'test'
    with pytest.raises(ValueError) as exception:
        webhook_body['action'] = action
        parse_webhook(webhook_body)
    assert f'`{action}` is invalid webhook action' in str(exception.value)


def test_webhook_with_missing_fields_in_payload_not_parsed(webhook_body: dict):
    ''' Test if webhook with missing fields in payload is not parsed and proper
        exception raised. '''
    with pytest.raises(ValueError) as exception:
        del webhook_body['payload']['chat_id']
        parse_webhook(webhook_body)
    assert 'Invalid webhook payload' in str(exception.value)


def test_webhook_with_additional_fields_in_payload_not_parsed(
        webhook_body: dict):
    ''' Test if webhook with additional fields in payload is not parsed and proper
        exception raised. '''
    with pytest.raises(ValueError) as exception:
        webhook_body['payload']['foo'] = 'bar'
        parse_webhook(webhook_body)
    assert 'Invalid webhook payload' in str(exception.value)
