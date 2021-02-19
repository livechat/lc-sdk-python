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
        ''' Open WebSocket connection. '''
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

    def send(self,
             request):
        ''' Send request via WebSocket. '''
        responses = {}
        if self.websocket.connected:
            request.update({'request_id': str(random.randint(1, 9999999999))})
            request_json = json.dumps(request, indent=4)
            self.logger.info(f'\nREQUEST:\n{request_json}')
            self.websocket.send(request_json)
            sleep(self.timeout)
            responses = self._receive(request)
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

    def _receive(self, request, expected_responses=1):
        ''' Receive data from WebSocket. '''
        all_responses = {
            'response': None,
            'pushes': []
        }
        for _ in range(70):
            if self.websocket.connected:
                try:
                    response = json.loads(self.websocket.recv())
                except (WebSocketTimeoutException,
                        WebSocketConnectionClosedException) as error:
                    self.logger.critical(f'Exception caught while collecting responses: {error}.')
                else:
                    if response.get('request_id') == request.get('request_id'):
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





