'''
Client for WebSocket connections.
'''

import concurrent.futures
import json
import random
import ssl
import threading
from time import sleep
from typing import List, NoReturn, Union

from loguru import logger
from websocket import WebSocketApp, WebSocketConnectionClosedException
from websocket._abnf import ABNF

from livechat.utils.structures import RtmResponse


def on_message(ws_client: WebSocketApp, message: str):
    ''' Custom WebSocketApp handler that inserts new messages in front of `self.messages` list. '''
    ws_client.messages.insert(0, json.loads(message))


def on_close(ws_client: WebSocketApp, close_status_code: int, close_msg: str):
    logger.info('websocket closed:')

    if close_status_code or close_msg:
        logger.info('close status code: ' + str(close_status_code))
        logger.info('close message: ' + str(close_msg))


def on_error(ws_client: WebSocketApp, error: Exception):
    logger.error(f'websocket error occurred: {str(error)}')


class WebsocketClient(WebSocketApp):
    ''' Custom extension of the WebSocketApp class for livechat python SDK. '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.messages: List[dict] = []
        self.on_message = on_message
        self.on_close = on_close
        self.on_error = on_error
        self.response_timeout = None

    def open(self,
             origin: dict = None,
             ping_timeout: Union[float, int] = 3,
             ping_interval: Union[float, int] = 5,
             ws_conn_timeout: Union[float, int] = 10,
             keep_alive: bool = True,
             response_timeout: Union[float, int] = 3) -> NoReturn:
        ''' Opens websocket connection and keep running forever.
            Args:
                origin (dict): Specifies origin while creating websocket connection.
                ping_timeout (int or float): timeout (in seconds) if the pong message is not received,
                    by default sets to 3 seconds.
                ping_interval (int or float): automatically sends "ping" command every specified period (in seconds).
                    If set to 0, no ping is sent periodically, by default sets to 5 seconds.
                ws_conn_timeout (int or float): timeout (in seconds) to wait for WebSocket connection,
                    by default sets to 10 seconds.
                keep_alive(bool): Bool which states if connection should be kept, by default sets to `True`.
                response_timeout (int or float): timeout (in seconds) to wait for the response,
                    by default sets to 3 seconds. '''
        if self.sock and self.sock.connected:
            logger.warning(
                'Cannot open new websocket connection, already connected.')
            return
        self.response_timeout = response_timeout
        run_forever_kwargs = {
            'sslopt': {
                'cert_reqs': ssl.CERT_NONE
            },
            'origin': origin,
            'ping_timeout': ping_timeout,
            'ping_interval': ping_interval,
        }
        if keep_alive:
            ping_thread = threading.Thread(target=self.run_forever,
                                           kwargs=run_forever_kwargs)
            ping_thread.start()
            self._wait_till_sock_connected(ws_conn_timeout)
            return
        self.run_forever(**run_forever_kwargs)

    def send(self, request: dict, opcode=ABNF.OPCODE_TEXT) -> dict:
        '''
        Sends message, assigning a random request ID, fetching and returning response(s).
            Args:
                request (dict): message to send. If you set opcode to OPCODE_TEXT,
                    data must be utf-8 string or unicode.
                opcode (int): operation code of data. default is OPCODE_TEXT.

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

        def await_message(stop_event: threading.Event) -> dict:
            while not stop_event.is_set():
                for item in self.messages:
                    if item.get('request_id') == request_id and item.get(
                            'type') == 'response':
                        return item
                sleep(0.2)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            stop_event = threading.Event()
            future = executor.submit(await_message, stop_event)
            try:
                response = future.result(timeout=self.response_timeout)
                logger.info(f'\nRESPONSE:\n{json.dumps(response, indent=4)}')
            except concurrent.futures.TimeoutError:
                stop_event.set()
                logger.error(
                    f'timed out waiting for message with request_id {request_id}'
                )
                logger.debug('all websocket messages received before timeout:')
                logger.debug(self.messages)
                return None

        return RtmResponse(response)

    def _wait_till_sock_connected(self,
                                  timeout: Union[float, int] = 10) -> NoReturn:
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
