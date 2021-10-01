''' Rest API implementation. '''

# pylint: disable=W0613,W0622,C0103,R0913,R0903

from abc import ABCMeta

import httpx

from livechat.utils.helpers import prepare_payload


class ReportsApi:
    ''' Main class that allows retrieval of client for specific Reports
        API version. '''
    @staticmethod
    def get_client(token: str,
                   version: str = '3.3',
                   base_url: str = 'api.livechatinc.com',
                   http2: bool = False):
        ''' Returns client for specific Reports API version.

            Args:
                token (str): Full token with type (Bearer/Basic) that will be
                             used as `Authorization` header in requests to API.
                version (str): API's version. Defaults to `3.3`.
                base_url (str): API's base url. Defaults to `api.livechatinc.com`.
                http2 (bool): A boolean indicating if HTTP/2 support should be
                              enabled. Defaults to `False`.

            Returns:
                ReportsAPI: API client object for specified version.

            Raises:
                ValueError: If the specified version does not exist.
        '''
        client = {
            '3.3': ReportsAPI33(token, '3.3', base_url, http2),
            '3.4': ReportsAPI34(token, '3.4', base_url, http2)
        }.get(version)
        if not client:
            raise ValueError('Provided version does not exist.')
        return client


class ReportsApiInterface(metaclass=ABCMeta):
    ''' Interface class. '''
    def __init__(self, token: str, version: str, base_url: str, http2: bool):
        self.api_url = f'https://{base_url}/v{version}/reports'
        self.session = httpx.Client(http2=http2,
                                    headers={'Authorization': token})

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
       

class ReportsAPI33(ReportsApiInterface):
    ''' Configuration API client in version 3.3 class. '''

#Chats
    def agents_chatting_duration(self,
                                to: str = None,
                                from_param: str = None,
                                agents: str = None,
                                groups: str = None,
                                tags: str = None,
                                customer_client_ids: str = None,
                                distribution: str = None,
                                timezone: str = None,
                                tagged: bool = None,
                                payload: dict = None,
                                headers: dict = None) -> httpx.Response:
        if payload is None:
            payload = prepare_payload(locals())
            if from_param is not None:
                del payload['from_param']
                payload['from'] = from_param
        return self.session.get(f'{self.api_url}/chats/agents_chatting_duration',
                                params=payload,
                                headers=headers)
    

    def tags(self,
            to: str = None,
            from_param: str = None,
            distribution: str = None,
            timezone: str = None,
            agents: str = None,
            groups: str = None,
            names: str = None,
            payload: dict = None,
            headers: dict = None) -> httpx.Response:
        if payload is None:
            payload = prepare_payload(locals())
            if from_param is not None:
                del payload['from_param']
                payload['from'] = from_param
        return self.session.get(f'{self.api_url}/chats/tags',
                                params=payload,
                                headers=headers)
    

    def total_chats(self,
                    from_param: str = None,
                    to: str = None,
                    distribution: str = None,
                    timezone: str = None,
                    agents: str = None,
                    agent_assigned: str = None,
                    groups: str = None,
                    customer_client_ids: str = None,
                    tags: str = None,
                    tagged: str = None,
                    payload: dict = None,
                    headers: dict = None) -> httpx.Response:
        if payload is None:
            payload = prepare_payload(locals())
            if from_param is not None:
                del payload['from_param']
                payload['from'] = from_param
        return self.session.get(f'{self.api_url}/chats/total_chats',
                                params=payload,
                                headers=headers)

class ReportsAPI34(ReportsApiInterface):
    ''' Configuration API client in version 3.4 class. '''

#Chats

    def duration(self,
                        distribution: str = None,
                        timezone: str = None,
                        filteters: dict = None,
                        payload: dict = None,
                        headers: dict = None) -> httpx.Response:

        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/chats/duration',
                                 json=payload,
                                 headers=headers)

    def tags(self,
                        distribution: str = None,
                        timezone: str = None,
                        filteters: dict = None,
                        payload: dict = None,
                        headers: dict = None) -> httpx.Response:

        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/chats/tags',
                                 json=payload,
                                 headers=headers)

    def total_chats(self,
                        distribution: str = 'day',
                        timezone: str = None,
                        filteters: dict = None,
                        payload: dict = None,
                        headers: dict = None) -> httpx.Response:

        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/chats/total_chats',
                                 json=payload,
                                 headers=headers)

    def ratings(self,
                        distribution: str = 'day',
                        timezone: str = None,
                        filteters: dict = None,
                        payload: dict = None,
                        headers: dict = None) -> httpx.Response:

        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/chats/ratings',
                                 json=payload,
                                 headers=headers)

    def ranking(self,
                        distribution: str = 'day',
                        timezone: str = None,
                        filteters: dict = None,
                        payload: dict = None,
                        headers: dict = None) -> httpx.Response:

        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/chats/ranking',
                                 json=payload,
                                 headers=headers)

    def engagement(self,
                        distribution: str = 'day',
                        timezone: str = None,
                        filteters: dict = None,
                        payload: dict = None,
                        headers: dict = None) -> httpx.Response:

        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/chats/engagement',
                                 json=payload,
                                 headers=headers)

#Agents

    def availability(self,
                        distribution: str = 'day',
                        timezone: str = None,
                        filteters: dict = None,
                        payload: dict = None,
                        headers: dict = None) -> httpx.Response:

        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/agents/availability',
                                 json=payload,
                                 headers=headers)
