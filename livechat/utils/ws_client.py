'''
Client for WebSocket connections.
'''

import concurrent.futures
import json
import random
import ssl
import threading
import time
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
    error_details = {
        'error_type': type(error).__name__,
        'error_message': str(error),
        'url': getattr(ws_client, 'url', 'unknown'),
        'keep_running': getattr(ws_client, 'keep_running', 'unknown')
    }
    logger.error(f'websocket error occurred: {error_details}')


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
            logger.debug(f'Starting WebSocket connection to {self.url}')

            # Use threading.Event for better synchronization
            connection_event = threading.Event()
            connection_error = threading.Event()

            # Store original callbacks
            original_on_open = getattr(self, 'on_open', None)
            original_on_error = getattr(self, 'on_error', None)

            # Create enhanced callbacks for connection tracking
            def on_open_with_event(ws):
                logger.info('WebSocket connection opened')
                connection_event.set()
                if original_on_open:
                    original_on_open(ws)

            def on_error_with_event(ws, error):
                logger.error(f'WebSocket connection error: {error}')
                connection_error.set()
                if original_on_error:
                    original_on_error(ws, error)

            # Set enhanced callbacks
            self.on_open = on_open_with_event
            self.on_error = on_error_with_event

            try:
                ping_thread = threading.Thread(target=self.run_forever,
                                               kwargs=run_forever_kwargs)
                ping_thread.daemon = True  # Make thread daemon to prevent hanging
                ping_thread.start()

                # Wait for either connection success or error
                if connection_event.wait(timeout=ws_conn_timeout):
                    logger.debug('WebSocket connection established via event')
                elif connection_error.is_set():
                    raise TimeoutError(
                        'WebSocket connection failed due to error')
                else:
                    # Fallback to original polling method
                    logger.debug(
                        'Event-based connection detection failed, falling back to polling'
                    )
                    self._wait_till_sock_connected(ws_conn_timeout)

            except Exception as e:
                logger.error(f'Failed to establish WebSocket connection: {e}')
                raise
            finally:
                # Restore original callbacks
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
        # Validate connection before sending
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

    def _wait_till_sock_connected(self,
                                  timeout: Union[float, int] = 10) -> NoReturn:
        ''' Polls until `self.sock` is connected.
            Args:
                timeout (float): timeout value in seconds, default 10. '''
        start_time = time.time()
        poll_interval = 0.05

        logger.debug(f'Waiting for WebSocket connection (timeout: {timeout}s)')

        while time.time() - start_time < timeout:
            try:
                if self.sock and hasattr(self.sock,
                                         'connected') and self.sock.connected:
                    logger.debug(
                        'WebSocket connection established successfully')
                    return

                # Check if socket exists but connection failed
                if self.sock and hasattr(
                        self.sock, 'connected') and not self.sock.connected:
                    # Give it a bit more time for connection to establish
                    pass

            except AttributeError:
                # Socket not yet created, continue waiting
                pass
            except Exception as e:
                logger.warning(
                    f'Unexpected error while checking WebSocket connection: {e}'
                )

            sleep(poll_interval)

        connection_status = 'unknown'
        if hasattr(self, 'sock') and self.sock:
            if hasattr(self.sock, 'connected'):
                connection_status = f'connected={self.sock.connected}'
            else:
                connection_status = 'sock exists but no connected attribute'
        else:
            connection_status = 'sock is None'

        error_msg = f'Timed out waiting for WebSocket to open after {timeout}s. Connection status: {connection_status}'
        logger.error(error_msg)
        raise TimeoutError(error_msg)

    def close(self, code: int = 1000, reason: str = 'Normal closure') -> None:
        ''' Close WebSocket connection gracefully. '''
        logger.debug(
            f'Closing WebSocket connection (code: {code}, reason: {reason})')
        try:
            if self.sock and hasattr(self.sock, 'close'):
                self.sock.close(code, reason)
            self.keep_running = False
        except Exception as e:
            logger.warning(f'Error during WebSocket close: {e}')

    def __del__(self):
        ''' Cleanup when object is destroyed. '''
        try:
            if hasattr(self, 'sock') and self.sock:
                self.close()
        except Exception:
            pass  # Ignore errors during cleanup
