''' Tests for WS client. '''

# pylint: disable=E1120,W0621,C0103,R1702

import pytest

from livechat.utils.ws_client import WebsocketClient


def test_websocket_client():
    ''' Test if ws can be created and has correct url. '''
    ws = WebsocketClient(
        url='wss://api.livechatinc.com/v3.3/customer/rtm/ws?license_id=10386012'
    )
    assert ws is not None, 'Websocket object was not created.'
    assert ws.url == 'wss://api.livechatinc.com/v3.3/customer/rtm/ws?license_id=10386012', 'Incorrect WS address.'


def test_websocket_connections_states():
    ''' Test if ws connection states open and close are set correctly. '''
    ws = WebsocketClient(
        url='wss://api.livechatinc.com/v3.3/customer/rtm/ws?license_id=10386012'
    )
    ws.open()
    opened_state = ws.keep_alive
    ws.close()
    closed_state = ws.keep_alive
    assert opened_state is True, 'Client did not open socket.'
    assert closed_state is False, 'Client did not close socket.'


def test_websocket_connect_with_invalid_url():
    ''' Test if ValueError is thrown when ws url is invalid. '''
    with pytest.raises(ValueError) as exception:
        WebsocketClient(url='invalid').open()
    assert str(exception.value) == 'url is invalid'


def test_websocket_connect_with_invalid_timeout():
    ''' Test if ValueError is thrown when ws timeout is invalid. '''
    with pytest.raises(TypeError) as exception:
        WebsocketClient(
            url=
            'wss://api.livechatinc.com/v3.3/customer/rtm/ws?license_id=10386012',
            timeout='test_timeout').open()
    assert str(exception.value) == 'an integer is required (got type str)'


def test_websocket_send_through_not_opened_pipe():
    ''' Test if message cannot be sent through not opened pipe. '''
    with pytest.raises(AttributeError) as exception:
        ws = WebsocketClient(
            url=
            'wss://api.livechatinc.com/v3.3/customer/rtm/ws?license_id=10386012'
        )
        ws.send({'action': 'login', 'payload': {'token': 'Bearer xxx'}})
    assert str(
        exception.value) == "'NoneType' object has no attribute 'connected'"


def test_websocket_send_and_receive_message():
    ''' Test if websocket client sends and receives messages. '''
    ws = WebsocketClient(
        url='wss://api.livechatinc.com/v3.3/customer/rtm/ws?license_id=10386012'
    )
    ws.open()
    response = ws.send({'action': 'login', 'payload': {'token': 'Bearer xxx'}})
    ws.close()
    assert response['response']['payload'] == {
        'error': {
            'type': 'authentication',
            'message': 'Invalid access token'
        }
    }, 'Request was not sent or received.'
