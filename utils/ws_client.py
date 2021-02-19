'''
Client for WebSocket connections.
'''

import json
import ssl
import threading
from time import sleep
import logging
import websocket
from websocket import (WebSocketException, WebSocketTimeoutException,
                WebSocketProtocolException, WebSocketPayloadException,
                WebSocketConnectionClosedException, WebSocketProxyException,
                WebSocketBadStatusException, WebSocketAddressException)
from utils.tools import parse_url_and_return_origin
import random
from timeit import default_timer as timer

class WebsocketClient:
    ''' WebSocket synchronous client based on websocket-client module. '''

    def __init__(self, url, timeout=2):
        self.url = url
        self.timeout = timeout
        self.websocket = None
        self.keep_alive = True
        logging.basicConfig()
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)


    def open(self, keep_alive=True):
        ''' Open WebSocket connection.
                Args:
                    keep_alive(bool): Bool which states if connection should be kept, by default sets to `True`.
        '''
        try:
            self.websocket = websocket.create_connection(
                self.url,
                self.timeout,
                origin=parse_url_and_return_origin(self.url),
                sslopt={'cert_reqs': ssl.CERT_NONE},
                enable_multithread=True)
        except (WebSocketException, WebSocketTimeoutException,
                WebSocketProtocolException, WebSocketPayloadException,
                WebSocketConnectionClosedException, WebSocketProxyException,
                WebSocketBadStatusException, WebSocketAddressException) as exception:
            self.logger.critical(f'WebSocket Exception: {exception}')
        else:
            if keep_alive:
                self.keep_alive = True
                threading.Thread(target=self._keep_ws_alive).start()

    def close(self):
        ''' Close WebSocket connection. '''
        self.keep_alive = False
        if self.websocket.connected:
            try:
                self.websocket.close()
            except WebSocketConnectionClosedException as error:
                self.logger.critical(
                    f'Exception caught while closing the WebSocket: {error}.'
                )

    def send(self, request: dict) -> dict:
        ''' Send request via WebSocket.
               Args:
                    request (dict): Dictionary which is being converted to payload.
               Returns:
                    dict: Dictionary with response.
        '''
        responses = {}
        if self.websocket.connected:
            request_id = str(random.randint(1, 9999999999))
            request.update({'request_id': request_id})
            request_json = json.dumps(request, indent=4)
            self.logger.info(f'\nREQUEST:\n{request_json}')
            self.websocket.send(request_json)
            responses = self._receive(request_id)
            self.logger.info(
                    f'\nRESPONSES:\n{json.dumps(responses, indent=4)}'
            )
        else:
            self.logger.info('send() : WebSocket connection is closed.')
        return responses

    def _keep_ws_alive(self):
        ''' Method which keeps WebSocket alive. '''
        keep_alive_counter = 0
        while self.keep_alive:
            if self.websocket.connected and keep_alive_counter % 10 == 0:
                try:
                    self.websocket.send(json.dumps(
                            {
                                'action': 'ping',
                                'payload': {}
                            }, indent=4))
                except (WebSocketConnectionClosedException,
                        ConnectionResetError, BrokenPipeError) as error:
                    self.logger.critical(f'Exception caught while pinging the WebSocket: {error}.')
                    break
                else:
                    self.logger.info('Ping action sent.')
            sleep(1)
            keep_alive_counter += 1

    def _receive(self, request_id: str, expected_responses=1) -> dict:
        ''' Receive data from WebSocket.
               Args:
                    request_id (dict): String which shows request_id for matching request with response.
                    expected_responses (int): Which states how many response messages should be returned, default value should be set to 1.
               Returns:
                    dict: Dictionary with response.
        '''
        all_responses = {
            'response': None,
            'pushes': []
        }
        start = timer()
        while timer() - start < 5:
            if self.websocket.connected:
                try:
                    response = json.loads(self.websocket.recv())
                except (WebSocketTimeoutException,
                        WebSocketConnectionClosedException) as error:
                    self.logger.critical(f'Exception caught while collecting responses: {error}.')
                else:
                    if response.get('request_id') == request_id:
                        if response.get('type') == 'response':
                            all_responses['response'] = response
                        else:
                            action = response.get('action')
                            if action not in all_responses:
                                all_responses[action] = response
                        expected_responses -= 1
                    else:
                        if response.get('action') != 'ping':
                           all_responses['pushes'].append(response)
                if expected_responses <= 0 and all_responses.get(
                        'response') is not None:
                    break
            else:
                break
        return all_responses





