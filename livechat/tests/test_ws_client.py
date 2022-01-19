''' Tests for WS client. '''

# pylint: disable=E1120,W0621,C0103,R1702

from configparser import ConfigParser

import pytest
import websocket

from livechat.utils.ws_client import WebsocketClient

config = ConfigParser()
config.read('configs/main.ini')
stable_version = config.get('api_versions', 'stable')
query_string = 'organization_id=30007dab-4c18-4169-978d-02f776e476a5'


def test_websocket_client():
    ''' Test if ws can be created and has correct url. '''
    ws = WebsocketClient(
        url=
        f'wss://api.livechatinc.com/v{stable_version}/customer/rtm/ws?{query_string}'
    )
    assert ws is not None, 'Websocket object was not created.'
    assert ws.url == f'wss://api.livechatinc.com/v{stable_version}/customer/rtm/ws?{query_string}', 'Incorrect WS address.'


def test_websocket_connections_states():
    ''' Test if ws connection states open and close are set correctly. '''
    ws = WebsocketClient(
        url=
        f'wss://api.livechatinc.com/v{stable_version}/customer/rtm/ws?{query_string}'
    )
    ws.open()
    opened_state = ws.keep_running
    ws.close()
    closed_state = ws.keep_running
    assert opened_state is True, 'Client did not open socket.'
    assert closed_state is False, 'Client did not close socket.'


def test_websocket_send_through_not_opened_pipe():
    ''' Test if message cannot be sent through not opened pipe. '''
    with pytest.raises(websocket._exceptions.WebSocketConnectionClosedException
                       ) as exception:
        ws = WebsocketClient(
            url=
            f'wss://api.livechatinc.com/v{stable_version}/customer/rtm/ws?{query_string}'
        )
        ws.send({'action': 'login', 'payload': {'token': 'Bearer xxx'}})
    assert str(exception.value) == 'Connection is already closed.'


def test_websocket_send_and_receive_message():
    ''' Test if websocket client sends and receives messages. '''
    ws = WebsocketClient(
        url=
        f'wss://api.livechatinc.com/v{stable_version}/customer/rtm/ws?{query_string}'
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
