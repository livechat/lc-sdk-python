'''
Client for WebSocket connections.
'''

import json
import random
import ssl
import threading
from time import sleep
from typing import List, NoReturn

from loguru import logger
from websocket import WebSocketApp, WebSocketConnectionClosedException
from websocket._abnf import ABNF

from livechat.utils.structures import RtmResponse


def on_message(ws_client: WebSocketApp, message: str):
    ''' Custom WebSocketApp handler that inserts new messages in front of `self.messages` list. '''
    ws_client.messages.insert(0, json.loads(message))


class WebsocketClient(WebSocketApp):
    ''' Custom extension of the WebSocketApp class for livechat python SDK. '''

    messages: List[dict] = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_message = on_message

    def open(self,
             origin: dict = None,
             timeout: float = 3,
             keep_alive: bool = True) -> NoReturn:
        ''' Opens websocket connection and keep running forever.
            Args:
                origin (dict): Specifies origin while creating websocket connection.
                timeout (int or float): time [seconds] to wait for server in ping/pong frame.
                keep_alive(bool): Bool which states if connection should be kept, by default sets to `True`. '''
        run_forever_kwargs = {
            'sslopt': {
                'cert_reqs': ssl.CERT_NONE
            },
            'origin': origin,
            'ping_timeout': timeout,
            'ping_interval': 5
        }
        if keep_alive:
            ping_thread = threading.Thread(target=self.run_forever,
                                           kwargs=run_forever_kwargs)
            ping_thread.start()
            self._wait_till_sock_connected()
            return
        self.run_forever(**run_forever_kwargs)

    def send(self,
             request: dict,
             opcode=ABNF.OPCODE_TEXT,
             response_timeout=2) -> dict:
        '''
        Sends message, assigining a random request ID, fetching and returning response(s).
            Args:
                request (dict): message to send. If you set opcode to OPCODE_TEXT,
                    data must be utf-8 string or unicode.
                opcode (int): operation code of data. default is OPCODE_TEXT.
                response_timeout (int): time in seconds to wait for the response.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        request_id = str(random.randint(1, 9999999999))
        request.update({'request_id': request_id})
        request_json = json.dumps(request, indent=4)
        logger.info(f'\nREQUEST:\n{request_json}')
        if not self.sock or self.sock.send(request_json, opcode) == 0:
            raise WebSocketConnectionClosedException(
                'Connection is already closed.')
        while not (response := next(
            (item
             for item in self.messages if item.get('request_id') == request_id
             and item.get('type') == 'response'),
                None)) and response_timeout > 0:
            sleep(0.2)
            response_timeout -= 0.2
        logger.info(f'\nRESPONSE:\n{json.dumps(response, indent=4)}')
        return RtmResponse(response)

    def _wait_till_sock_connected(self, timeout: float = 10) -> NoReturn:
        ''' Polls until `self.sock` is connected.
            Args:
                timeout (float): timeout value in seconds, default 10. '''
        if timeout < 0:
            raise TimeoutError('Timed out waiting for WebSocket to open.')
        try:
            assert self.sock.connected
            return
        except (AttributeError, AssertionError):
            sleep(0.1)
            return self._wait_till_sock_connected(timeout=timeout - 0.1)
