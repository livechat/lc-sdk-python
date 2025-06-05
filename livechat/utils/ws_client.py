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
    logger.info('websocket closed')

    if close_status_code or close_msg:
        logger.info(f'close status code: {close_status_code}')
        logger.info(f'close message: {close_msg}')


def on_error(ws_client: WebSocketApp, error: Exception):
    error_details = {
        'error_type': type(error).__name__,
        'error_message': str(error),
        'url': getattr(ws_client, 'url', 'unknown'),
    }
    logger.error(f'WebSocket error occurred: {error_details}')


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
            logger.debug(
                f'Starting WebSocket connection to:\n{self.url}\nwith header:\n{self.header}'
            )

            connection_event = threading.Event()
            connection_error = threading.Event()
            handshake_info = {
                'status': None,
                'headers': None,
                'error': None,
                'url': self.url
            }

            error_info = {'message': None}

            original_on_open = getattr(self, 'on_open', None)
            original_on_error = getattr(self, 'on_error', None)

            def on_open_with_event(ws):
                try:
                    if hasattr(ws.sock, 'handshake_response'):
                        handshake_info[
                            'status'] = ws.sock.handshake_response.status
                        handshake_info[
                            'headers'] = ws.sock.handshake_response.headers
                        logger.debug(
                            f'WebSocket handshake successful - Status: {handshake_info["status"]}'
                        )
                        logger.debug(
                            f'WebSocket handshake headers: {handshake_info["headers"]}'
                        )
                    else:
                        logger.debug(
                            'WebSocket handshake completed but no response details available'
                        )
                except Exception as e:
                    logger.warning(f'Could not capture handshake details: {e}')

                connection_event.set()
                if original_on_open:
                    original_on_open(ws)

            def on_error_with_event(ws, error):
                error_type = type(error).__name__
                error_msg = str(error)

                try:
                    if hasattr(ws.sock, 'handshake_response'
                               ) and ws.sock.handshake_response:
                        handshake_info[
                            'status'] = ws.sock.handshake_response.status
                        handshake_info[
                            'headers'] = ws.sock.handshake_response.headers
                except Exception:
                    pass

                handshake_info['error'] = {
                    'type': error_type,
                    'message': error_msg,
                    'during_handshake': True
                }

                logger.error(
                    f'WebSocket error during connection: {error_type}: {error_msg}'
                )

                error_info['message'] = error_msg
                connection_error.set()
                if original_on_error:
                    original_on_error(ws, error)

            self.on_open = on_open_with_event
            self.on_error = on_error_with_event

            try:
                ping_thread = threading.Thread(target=self.run_forever,
                                               kwargs=run_forever_kwargs)
                ping_thread.daemon = True
                ping_thread.start()

                if connection_event.wait(timeout=ws_conn_timeout):
                    logger.debug(
                        f'WebSocket connection established successfully.\nHandshake status: {handshake_info["status"]}'
                    )
                elif connection_error.is_set():
                    error_msg = error_info[
                        'message'] or 'Unknown connection error'
                    logger.error(f'WebSocket connection failed: {error_msg}')
                    logger.error(
                        f'Handshake info:\n {json.dumps(handshake_info, indent=4)}'
                    )

                    raise TimeoutError(
                        f'WebSocket connection failed due to error: {error_msg}'
                    )
                else:
                    logger.error(
                        'WebSocket connection timeout - no response within timeout period'
                    )
                    if self.sock:
                        if hasattr(self.sock, 'handshake_response'):
                            handshake_info[
                                'status'] = self.sock.handshake_response.status
                            handshake_info[
                                'headers'] = self.sock.handshake_response.headers
                        else:
                            handshake_info['status'] = 'unknown'
                            handshake_info['headers'] = 'unknown'
                    else:
                        handshake_info['status'] = 'no socket'
                        handshake_info['headers'] = 'no socket'

                    logger.error(
                        f'Timeout details: {ws_conn_timeout}s waiting for connection to {handshake_info["url"]}'
                    )
                    logger.error(
                        f'Handshake info:\n {json.dumps(handshake_info, indent=4)}'
                    )

                    raise TimeoutError(
                        f'WebSocket handshake timeout after {ws_conn_timeout}s - server did not respond to HTTP upgrade request'
                    )

            except Exception as e:
                logger.error(f'Failed to establish WebSocket connection: {e}')
                raise
            finally:
                self.on_open = original_on_open
                self.on_error = original_on_error

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
        if not self.is_connected():
            raise WebSocketConnectionClosedException(
                'Connection is already closed.')

        request_id = str(random.randint(1, 9999999999))
        request.update({'request_id': request_id})
        request_json = json.dumps(request, indent=4)
        logger.info(f'\nREQUEST:\n{request_json}')

        try:
            send_result = self.sock.send(request_json, opcode)
            if send_result == 0:
                raise WebSocketConnectionClosedException(
                    'Failed to send data - connection closed.')
        except Exception as e:
            logger.error(f'Failed to send WebSocket message: {e}')
            raise WebSocketConnectionClosedException(f'Connection error: {e}')

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

    def is_connected(self) -> bool:
        ''' Check if WebSocket connection is active and healthy. '''
        try:
            return (self.sock is not None and hasattr(self.sock, 'connected')
                    and self.sock.connected
                    and getattr(self, 'keep_running', False))
        except Exception:
            return False

    def close(self, code: int = 1000, reason: str = 'Normal closure') -> None:
        ''' Close WebSocket connection gracefully. '''
        logger.info(
            f'Closing WebSocket connection (code: {code}, reason: {reason})')
        try:
            if self.sock:
                self.sock.close(code, reason)
            self.keep_running = False
        except Exception as e:
            logger.warning(f'Error during WebSocket close: {e}')
