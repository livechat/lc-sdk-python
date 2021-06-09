''' Async Customer Web client implementation. '''

# pylint: disable=W0613,R0913,W0622,C0103

from abc import ABCMeta

import aiohttp

from livechat.utils.helpers import prepare_payload


# pylint: disable=R0903
class AsyncCustomerWeb:
    ''' Allows retrieval of client for specific Customer Web
        API version. '''
    @staticmethod
    def get_client(license_id: int,
                   access_token: str,
                   version: str = '3.3',
                   base_url: str = 'api.livechatinc.com'):
        ''' Returns client for specific API version.

            Args:
                token (str): Full token with type (Bearer/Basic) that will be
                                used as `Authorization` header in requests to API.
                version (str): API's version. Defaults to `3.3`.
                base_url (str): API's base url. Defaults to `api.livechatinc.com`.

            Returns:
                API client object for specified version based on
                `CustomerWebApiInterface`.

            Raises:
                ValueError: If the specified version does not exist.
        '''
        client = {
            '3.3': CustomerWeb33(license_id, access_token, version, base_url),
            '3.4': CustomerWeb34(license_id, access_token, version, base_url)
        }.get(version)
        if not client:
            raise ValueError('Provided version does not exist.')
        return client


class CustomerWebInterface(metaclass=ABCMeta):
    ''' Main class containing API methods. '''
    def __init__(self, license_id: int, access_token: str, version: str,
                 base_url: str):
        self.api_url = f'https://{base_url}/v{version}/customer/action'
        self.session = aiohttp.ClientSession()
        self.session.headers.update({'Authorization': access_token})
        self.license_id = str(license_id)

    def modify_header(self, header: dict) -> None:
        ''' Modifies provided header in session object.

            Args:
                header (dict): Header which needs to be modified.
        '''
        self.session.headers.update(header)

    def remove_header(self, key: str) -> None:
        ''' Removes provided header from session object.

            Args:
                key (str): Key which needs to be removed from the header.
        '''
        if key in self.session.headers:
            del self.session.headers[key]

    def get_headers(self) -> dict:
        ''' Returns current header values in session object.

            Returns:
                dict: Response which presents current header values in session object.
        '''
        return dict(self.session.headers)

    async def close_session(self) -> None:
        ''' Closes active session. '''
        if not self.session.closed:
            await self.session.close()

    async def start_chat(self,
                         chat: dict = None,
                         active: bool = None,
                         continuous: bool = None,
                         payload: dict = None) -> aiohttp.ClientResponse:
        ''' Starts a chat.

            Args:
                chat (dict): Dict containing chat properties, access and thread.
                active (bool): When set to False, creates an inactive thread; default: True.
                continuous (bool): Starts chat as continuous (online group is not required); default: False.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                aiohttp.ClientResponse: The Response object from `aiohttp` library,
                    which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return await self.session.post(
            f'{self.api_url}/start_chat?license_id={self.license_id}',
            json=payload)

    async def get_chat(self,
                       chat_id: str = None,
                       thread_id: str = None,
                       payload: dict = None) -> aiohttp.ClientResponse:
        ''' Returns a thread that the current Customer has access to in a given chat.

            Args:
                chat_id (str): ID of the chat for which thread is to be returned.
                thread_id (str): ID of the thread to show. Default: the latest thread (if exists)
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
            Returns:
                aiohttp.ClientResponse: The Response object from `aiohttp` library,
                    which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return await self.session.post(
            f'{self.api_url}/get_chat?license_id={self.license_id}',
            json=payload)

    async def deactivate_chat(self,
                              id: str = None,
                              payload: dict = None) -> aiohttp.ClientResponse:
        ''' Deactivates a chat by closing the currently open thread.
            Sending messages to this thread will no longer be possible.

            Args:
                id (str): ID of chat to be deactivated.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                aiohttp.ClientResponse: The Response object from `aiohttp` library,
                    which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return await self.session.post(
            f'{self.api_url}/deactivate_chat?license_id={self.license_id}',
            json=payload)


class CustomerWeb33(CustomerWebInterface):
    ''' Customer API version 3.3 class. '''


class CustomerWeb34(CustomerWebInterface):
    ''' Customer API version 3.4 class. '''
