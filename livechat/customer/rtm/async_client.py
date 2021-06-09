''' Async Customer RTM client implementation. '''

# pylint: disable=W0613,W0622,C0103,R0913,R0903,W0107

import random
from abc import ABCMeta

from livechat.utils.async_ws_client import AsyncWebsocketClient
from livechat.utils.helpers import prepare_payload


class AsyncCustomerRTM:
    ''' Main class that gets specific client. '''
    @staticmethod
    def get_client(license_id: int = None,
                   version: str = '3.3',
                   base_url: str = 'api.livechatinc.com'):
        ''' Returns client for specific Customer RTM version.

            Args:
                license_id (int): License ID.
                version (str): API's version. Defaults to `3.3`.
                base_url (str): API's base url. Defaults to `api.livechatinc.com`.

            Returns:
                CustomerRTMInterface: API client object for specified version.

            Raises:
                ValueError: If the specified version does not exist.
        '''
        client = {
            '3.3': CustomerRTM33(license_id, version, base_url),
            '3.4': CustomerRTM34(license_id, version, base_url)
        }.get(version)
        if not client:
            raise ValueError('Provided version does not exist.')
        return client


class CustomerRTMInterface(metaclass=ABCMeta):
    ''' CustomerRTM interface class. '''
    def __init__(self, license_id, version, url):
        if not license_id or not isinstance(license_id, int):
            raise ValueError(
                'Pipe was not opened. Something`s wrong with your `license_id`.'
            )
        self.ws = AsyncWebsocketClient(
            url=
            f'wss://{url}/v{version}/customer/rtm/ws?license_id={license_id}')

    async def open_connection(self, origin: dict = None) -> None:
        ''' Opens WebSocket connection.

            Args:
                origin (dict): Specifies origin while creating websocket connection.
        '''
        if origin:
            await self.ws.open(origin=origin)
        else:
            await self.ws.open()

    async def close_connection(self) -> None:
        ''' Closes WebSocket connection. '''
        await self.ws.close()

    async def receive_message(self) -> dict:
        ''' Receives message from WebSocket. '''
        return await self.ws.receive()

    async def login(self,
                    request_id: str = str(random.randint(1, 9999999999)),
                    token: str = None,
                    payload: dict = None) -> dict:
        ''' Logs in customer.

            Args:
                request_id (str): unique id of the request.
                    If not provided, a random id will be generated.
                token (str): OAuth token from the Customer's account.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                dict: request that will be sent out.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        request = {
            'action': 'login',
            'payload': payload,
            'request_id': request_id
        }
        await self.ws.send(request)
        return request

    async def start_chat(self,
                         request_id: str = str(random.randint(1, 9999999999)),
                         chat: dict = None,
                         active: bool = None,
                         continuous: bool = None,
                         payload: dict = None) -> dict:
        ''' Starts a chat.

            Args:
                request_id (str): unique id of the request.
                    If not provided, a random id will be generated.
                chat (dict): Chat object.
                active (bool): When set to False, creates an inactive thread; default: True.
                continuous (bool): Starts chat as continuous (online group is not required); default: False.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                dict: request that will be sent out.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        request = {
            'action': 'start_chat',
            'payload': payload,
            'request_id': request_id
        }
        await self.ws.send(request)
        return request

    async def deactivate_chat(self,
                              request_id: str = str(
                                  random.randint(1, 9999999999)),
                              id: str = None,
                              payload: dict = None) -> dict:
        ''' Deactivates a chat by closing the currently open thread.

            Args:
                request_id (str): unique id of the request.
                    If not provided, a random id will be generated.
                id (str): Chat ID to deactivate.
                payload (dict): Custom payload to be used as request's data.
                    It overrides all other parameters provided for the method.

            Returns:
                dict: request that will be sent out.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        request = {
            'action': 'deactivate_chat',
            'payload': payload,
            'request_id': request_id
        }
        await self.ws.send(request)
        return request


class CustomerRTM33(CustomerRTMInterface):
    ''' Customer RTM version 3.3 class. '''


class CustomerRTM34(CustomerRTMInterface):
    ''' Customer RTM version 3.4 class. '''
