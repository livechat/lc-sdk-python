'''
Async client for WebSocket connections.
'''

# pylint: disable=R1702

import json
import logging

import websockets
from websockets import WebSocketException


class AsyncWebsocketClient:
    ''' WebSocket asynchronous client based on websockets module. '''
    def __init__(self, url: str):
        self.url = url
        self.websocket = None
        logging.basicConfig()
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

    async def open(self, ping_interval: int = 10, origin: dict = None) -> None:
        ''' Open WebSocket connection.
                Args:
                    ping_interval(int): Specifies how often ping the server.
                        Default: 10 seconds.
                    origin (dict): Specifies origin while creating websocket connection.
        '''
        try:
            if origin:
                self.websocket = await websockets.connect(
                    self.url, ping_interval=ping_interval, origin=origin)
            else:
                self.websocket = await websockets.connect(
                    self.url, ping_interval=ping_interval)
        except WebSocketException as exception:
            self.logger.critical(f'WebSocket Exception: {exception}')

    async def close(self) -> None:
        ''' Close WebSocket connection. '''
        if self.websocket is not None:
            await self.websocket.close()
            self.websocket = None

    async def send(self, request: dict) -> None:
        ''' Send request via WebSocket.
                Args:
                    request (dict): Dictionary which is being converted to payload.
        '''
        if self.websocket is not None:
            await self.websocket.send(json.dumps(request))

    async def receive(self) -> dict:
        ''' Receive data from WebSocket.
                Returns:
                    dict: Dictionary containing response from WebSocket.
        '''
        if self.websocket is not None:
            results = await self.websocket.recv()
            return json.loads(results)
