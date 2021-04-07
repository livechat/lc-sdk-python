'''
Async client for WebSocket connections.
'''

# pylint: disable=R1702

import asyncio
import json
import logging
from abc import ABCMeta

import websockets
from websockets import WebSocketException


def parse_url_and_return_origin(url: str) -> str:
    ''' Parse url and return correct origin.

           Args:
                url (str): String which defines environment.

           Returns:
                str: String with correct origin depends on environment.
    '''
    domain = 'livechatinc.com'
    if 'labs' in url:
        return f'https://secure.labs.{domain}'
    if 'staging' in url:
        return f'https://secure-lc.{domain}'
    return f'https://secure.{domain}'


def prepare_payload(parameters: dict) -> dict:
    ''' Prepares payload for request based on provided parameters by removing
        unnecessary or protected variables and removing `None` values. Please
        note that main use is to pass `locals()` as `parameters`.

        Args:
            parameters (dict): parameters provided as key -> value pairs.

        Returns:
            dict: payload object without unnecessary items to be used in requests.
    '''
    return {
        key: value
        for key, value in parameters.items()
        if key not in ['self', 'payload'] and value is not None
    }


class AsyncWebsocketClient:
    ''' WebSocket asynchronous client based on websockets module. '''
    def __init__(self, url: str):
        self.url = url
        self.websocket = None
        self.keep_alive = True
        logging.basicConfig()
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

    async def open(self, keep_alive: bool = True) -> None:
        ''' Open WebSocket connection.
                Args:
                    keep_alive(bool): Bool which states if connection should be kept, by default sets to `True`.
        '''
        try:
            self.websocket = await websockets.connect(self.url)
        except WebSocketException as exception:
            self.logger.critical(f'WebSocket Exception: {exception}')
        else:
            if keep_alive:
                self.keep_alive = True
                asyncio.ensure_future(self._keep_ws_alive())

    async def close(self) -> None:
        ''' Close WebSocket connection. '''
        if self.websocket is not None:
            await self.websocket.close()
            self.websocket = None
            self.keep_alive = False

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

    async def _keep_ws_alive(self, interval: int = 10) -> None:
        ''' Ping WebSocket connection to keep it alive. '''
        while self.keep_alive:
            if self.websocket:
                try:
                    await self.websocket.send(
                        json.dumps({
                            'action': 'ping',
                            'payload': {}
                        }, indent=4))
                except WebSocketException as exception:
                    self.logger.critical(
                        f'Exception caught while pinging the WebSocket: {exception}.'
                    )
                    break
                else:
                    self.logger.info('Ping action sent.')
            await asyncio.sleep(interval)


class AsyncMetaClass:
    '''
    Allows to define an async __init__.
    '''
    async def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        await instance.__init__(*args, **kwargs)
        return instance

    async def __init__(self):
        pass


class AgentRTM:
    ''' Main class that gets specific client. '''
    @staticmethod
    def get_client(version: str = '3.3',
                   base_url: str = 'api.livechatinc.com'):
        ''' Returns client for specific Agent RTM version.

            Args:
                version (str): API's version. Defaults to `3.3`.
                base_url (str): API's base url. Defaults to `api.livechatinc.com`.

            Returns:
                AgentRTMInterface: API client object for specified version.

            Raises:
                ValueError: If the specified version does not exist.
        '''
        client = {'3.3': AgentRTM33(version, base_url)}.get(version)
        if not client:
            raise ValueError('Provided version does not exist.')
        return client


class AgentRTMInterface(AsyncMetaClass, metaclass=ABCMeta):
    ''' AgentRTM interface class. '''
    async def __init__(self, version: str, url: str):
        self.ws = AsyncWebsocketClient(
            url=f'wss://{url}/v{version}/agent/rtm/ws')
        await self.open_connection()

    async def open_connection(self) -> None:
        ''' Opens WebSocket connection. '''
        await self.ws.open()

    async def close_connection(self) -> None:
        ''' Closes WebSocket connection. '''
        await self.ws.close()

    async def receive_message(self) -> dict:
        ''' Receive message from WebSocket. '''
        return await self.ws.receive()

    async def login(self,
                    token: str = None,
                    timezone: str = None,
                    reconnect: bool = None,
                    push_notifications: dict = None,
                    application: dict = None,
                    away: bool = None,
                    customer_push_level: str = None,
                    payload: dict = None) -> None:
        ''' Logs in agent.

            Args:
                token (str): OAuth token from the Agent's account.
                timezone (str): Agent's timezone.
                reconnect (bool): Reconnecting sets the status to the
                        last known state instead of the default one.
                push_notifications (dict): Push notifications for the requested token.
                application (dict): Object containing information related to
                        the application's name and version.
                away (bool): When True, the connection is set to the away state.
                        Defaults to False.
                customer_push_level (str): Possible values: my, engaged, online.
                        Defaults to my if login creates the first session;
                        otherwise it preserves the current customer_push_level.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        await self.ws.send({'action': 'login', 'payload': payload})
        '''
        Of course, it's possible to return response and pushes related to the particular request,
        but the question is - do we need this, having async world?
        '''


class AgentRTM33(AgentRTMInterface):
    ''' AgentRTM version 3.3 class. '''


async def main():
    ''' Just main coroutine. '''
    client = await AgentRTM.get_client(base_url='api.labs.livechatinc.com')
    await asyncio.sleep(1)
    await client.login(token='Bearer fra-a:gYKvakQNfRUMaajMiwnFHWeXEpg')
    await asyncio.sleep(1)
    print(await client.receive_message())
    print(await client.receive_message())
    print(await client.receive_message())
    print('The End')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
