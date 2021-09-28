'''
Client for WebSocket connections.
'''

import json
import logging
import random
import ssl
from time import sleep
from typing import List

from websocket import WebSocketApp, WebSocketConnectionClosedException
from websocket._abnf import ABNF


class WebsocketClient(WebSocketApp):
    ''' Custom extension of the WebSocketApp class for livechat python SDK. '''

    messages: List[dict] = []

    def __init__(self, *args, **kwargs):
        def on_message(self, message):
            ''' Custom WebSocketApp handler that inserts new messages in front of `self.messages` list. '''
            self.messages.insert(0, json.loads(message))

        logging.basicConfig()
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        super().__init__(*args, **kwargs)
        self.on_message = on_message

    def open(self, origin: dict = None, timeout: float = 3):
        ''' Open websocket connection and keep running forever. '''
        self.run_forever(sslopt={'cert_reqs': ssl.CERT_NONE},
                         origin=origin,
                         ping_timeout=timeout,
                         ping_interval=5)

    def send(self, request: dict, opcode=ABNF.OPCODE_TEXT, response_timeout=2):
        '''
        Send message, assigining a random request ID, fetching and returning response(s).
            Args:
                request (dict): message to send. If you set opcode to OPCODE_TEXT,
                    data must be utf-8 string or unicode.
                opcode (int): operation code of data. default is OPCODE_TEXT.
                response_timeout (int): time in seconds to wait for the response.
            Returns:
                dict: Dictionary with response.
        '''
        request_id = str(random.randint(1, 9999999999))
        request.update({'request_id': request_id})
        request_json = json.dumps(request, indent=4)
        self.logger.info(f'\nREQUEST:\n{request_json}')
        if not self.sock or self.sock.send(request_json, opcode) == 0:
            raise WebSocketConnectionClosedException(
                'Connection is already closed.')
        while not (response := next(
            (item for item in self.messages
             if item.get('request_id') == request_id), None)):
            sleep(0.2)
            response_timeout -= 0.2
        self.logger.info(f'\nRESPONSE:\n{json.dumps(response, indent=4)}')
        return response
