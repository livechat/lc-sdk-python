''' Reports API implementation. '''

# pylint: disable=W0613,W0622,C0103,R0913,R0903

from __future__ import annotations

from abc import ABCMeta

import httpx

from livechat.config import CONFIG
from livechat.utils.helpers import prepare_payload
from livechat.utils.httpx_logger import HttpxLogger

stable_version = CONFIG.get('stable')
api_url = CONFIG.get('url')


class ReportsApi:
    ''' Main class that allows retrieval of client for specific Reports
        API version. '''
    @staticmethod
    def get_client(token: str,
                   version: str = stable_version,
                   base_url: str = api_url,
                   http2: bool = False) -> ReportsApiInterface:
        ''' Returns client for specific Reports API version.

            Args:
                token (str): Full token with type (Bearer/Basic) that will be
                             used as `Authorization` header in requests to API.
                version (str): API's version. Defaults to the stable version of API.
                base_url (str): API's base url. Defaults to API's production URL.
                http2 (bool): A boolean indicating if HTTP/2 support should be
                              enabled. Defaults to `False`.

            Returns:
                ReportsAPI: API client object for specified version.

            Raises:
                ValueError: If the specified version does not exist.
        '''
        client = {
            '3.3': ReportsAPI33(token, '3.3', base_url, http2),
            '3.4': ReportsAPI34(token, '3.4', base_url, http2),
            '3.5': ReportsAPI35(token, '3.5', base_url, http2),
        }.get(version)
        if not client:
            raise ValueError('Provided version does not exist.')
        return client


class ReportsApiInterface(metaclass=ABCMeta):
    ''' Interface class. '''
    def __init__(self,
                 token: str,
                 version: str,
                 base_url: str,
                 http2: bool,
                 proxies=None,
                 verify: bool = True) -> ReportsApiInterface:
        logger = HttpxLogger()
        self.api_url = f'https://{base_url}/v{version}/reports'
        self.session = httpx.Client(http2=http2,
                                    headers={'Authorization': token},
                                    event_hooks={
                                        'request': [logger.log_request],
                                        'response': [logger.log_response]
                                    },
                                    proxies=proxies,
                                    verify=verify)

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

    # Chats

    def duration(self,
                 distribution: str = None,
                 timezone: str = None,
                 filters: dict = None,
                 payload: dict = None,
                 headers: dict = None) -> httpx.Response:
        ''' Shows the average chatting duration of agents within a license.

        Args:
            distribution (str): Allowed values: `hour`, `day`, `day-hours`, `month` or `year`. Defaults to `day`.
            timezone (str): IANA Time Zone (e.g. America/Phoenix).
                            Defaults to the requester's timezone.
                            When the requester's timezone isn't present, then `filters.from` is parsed to get the timezone.
            filters (dict): If none provided, your report will span the last seven days.
            payload (dict): Custom payload to be used as request's data.
                            It overrides all other parameters provided for the method.
            headers (dict): Custom headers to be used with session headers.
                            They will be merged with session-level values that are set,
                            however, these method-level parameters will not be persisted across requests.

        Returns:
            httpx.Response: The Response object from `httpx` library,
                            which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/chats/duration',
                                 json=payload,
                                 headers=headers)

    def tags(self,
             distribution: str = None,
             timezone: str = None,
             filters: dict = None,
             payload: dict = None,
             headers: dict = None) -> httpx.Response:
        ''' Shows the distribution of tags for chats.

        Args:
            distribution (str): Allowed values: `hour`, `day`, `day-hours`, `month` or `year`. Defaults to `day`.
            timezone (str): IANA Time Zone (e.g. America/Phoenix).
                            Defaults to the requester's timezone.
                            When the requester's timezone isn't present, then `filters.from` is parsed to get the timezone.
            filters (dict): If none provided, your report will span the last seven days.
            payload (dict): Custom payload to be used as request's data.
                            It overrides all other parameters provided for the method.
            headers (dict): Custom headers to be used with session headers.
                            They will be merged with session-level values that are set,
                            however, these method-level parameters will not be persisted across requests.

        Returns:
            httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/chats/tags',
                                 json=payload,
                                 headers=headers)

    def total_chats(self,
                    distribution: str = None,
                    timezone: str = None,
                    filters: dict = None,
                    payload: dict = None,
                    headers: dict = None) -> httpx.Response:
        ''' Shows how many chats occurred during the specified period.

        Args:
            distribution (str): Allowed values: `hour`, `day`, `day-hours`, `month` or `year`. Defaults to `day`.
            timezone (str): IANA Time Zone (e.g. America/Phoenix).
                            Defaults to the requester's timezone.
                            When the requester's timezone isn't present, then `filters.from` is parsed to get the timezone.
            filters (dict): If none provided, your report will span the last seven days.
            payload (dict): Custom payload to be used as request's data.
                            It overrides all other parameters provided for the method.
            headers (dict): Custom headers to be used with session headers.
                            They will be merged with session-level values that are set,
                            however, these method-level parameters will not be persisted across requests.

        Returns:
            httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/chats/total_chats',
                                 json=payload,
                                 headers=headers)

    def ratings(self,
                distribution: str = None,
                timezone: str = None,
                filters: dict = None,
                payload: dict = None,
                headers: dict = None) -> httpx.Response:
        ''' Shows the number of rated chats along with their ratings during a specified period of time.

        Args:
            distribution (str): Allowed values: `hour`, `day`, `day-hours`, `month` or `year`. Defaults to `day`.
            timezone (str): IANA Time Zone (e.g. America/Phoenix).
                            Defaults to the requester's timezone.
                            When the requester's timezone isn't present, then `filters.from` is parsed to get the timezone.
            filters (dict): If none provided, your report will span the last seven days.
            payload (dict): Custom payload to be used as request's data.
                            It overrides all other parameters provided for the method.
            headers (dict): Custom headers to be used with session headers.
                            They will be merged with session-level values that are set,
                            however, these method-level parameters will not be persisted across requests.

        Returns:
            httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/chats/ratings',
                                 json=payload,
                                 headers=headers)

    def ranking(self,
                distribution: str = None,
                timezone: str = None,
                filters: dict = None,
                payload: dict = None,
                headers: dict = None) -> httpx.Response:
        ''' Shows the ratio of good to bad ratings for each operator.

        Args:
            distribution (str): Allowed values: `hour`, `day`, `day-hours`, `month` or `year`. Defaults to `day`.
            timezone (str): IANA Time Zone (e.g. America/Phoenix).
                            Defaults to the requester's timezone.
                            When the requester's timezone isn't present, then `filters.from` is parsed to get the timezone.
            filters (dict): If none provided, your report will span the last seven days.
            payload (dict): Custom payload to be used as request's data.
                            It overrides all other parameters provided for the method.
            headers (dict): Custom headers to be used with session headers.
                            They will be merged with session-level values that are set,
                            however, these method-level parameters will not be persisted across requests.

        Returns:
            httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/chats/ranking',
                                 json=payload,
                                 headers=headers)

    def engagement(self,
                   distribution: str = None,
                   timezone: str = None,
                   filters: dict = None,
                   payload: dict = None,
                   headers: dict = None) -> httpx.Response:
        ''' Shows the distribution of chats based on engagement during the specified period.

        Args:
            distribution (str): Allowed values: `hour`, `day`, `day-hours`, `month` or `year`. Defaults to `day`.
            timezone (str): IANA Time Zone (e.g. America/Phoenix).
                            Defaults to the requester's timezone.
                            When the requester's timezone isn't present, then `filters.from` is parsed to get the timezone.
            filters (dict): If none provided, your report will span the last seven days.
            payload (dict): Custom payload to be used as request's data.
                            It overrides all other parameters provided for the method.
            headers (dict): Custom headers to be used with session headers.
                            They will be merged with session-level values that are set,
                            however, these method-level parameters will not be persisted across requests.

        Returns:
            httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/chats/engagement',
                                 json=payload,
                                 headers=headers)

    def greetings_conversion(self,
                             distribution: str = None,
                             timezone: str = None,
                             filters: dict = None,
                             payload: dict = None,
                             headers: dict = None) -> httpx.Response:
        ''' Shows the number of greetings sent to the customers and how many of those resulted in a chat or a goal.

        Args:
            distribution (str): Allowed values: `hour`, `day`, `day-hours`, `month` or `year`. Defaults to `day`.
            timezone (str): IANA Time Zone (e.g. America/Phoenix).
                            Defaults to the requester's timezone.
                            When the requester's timezone isn't present, then `filters.from` is parsed to get the timezone.
            filters (dict): If none provided, your report will span the last seven days.
            payload (dict): Custom payload to be used as request's data.
                            It overrides all other parameters provided for the method.
            headers (dict): Custom headers to be used with session headers.
                            They will be merged with session-level values that are set,
                            however, these method-level parameters will not be persisted across requests.

        Returns:
            httpx.Response: The Response object from `httpx` library,
                            which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/chats/greetings_conversion',
                                 json=payload,
                                 headers=headers)

    def surveys(self,
                timezone: str = None,
                filters: dict = None,
                payload: dict = None,
                headers: dict = None) -> httpx.Response:
        ''' Returns the number of submitted chat surveys along with the count of specific answers.

        Args:
            timezone (str): IANA Time Zone (e.g. America/Phoenix).
                            Defaults to the requester's timezone.
                            When the requester's timezone isn't present, then `filters.from` is parsed to get the timezone.
            filters (dict): If none provided, your report will span the last seven days.
            payload (dict): Custom payload to be used as request's data.
                            It overrides all other parameters provided for the method.
            headers (dict): Custom headers to be used with session headers.
                            They will be merged with session-level values that are set,
                            however, these method-level parameters will not be persisted across requests.

        Returns:
            httpx.Response: The Response object from `httpx` library,
                            which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/chats/surveys',
                                 json=payload,
                                 headers=headers)

    # Agents

    def availability(self,
                     distribution: str = None,
                     timezone: str = None,
                     filters: dict = None,
                     payload: dict = None,
                     headers: dict = None) -> httpx.Response:
        ''' Shows for how long an agent, group, or the whole account was available for chatting during a specified period of time.

        Args:
            distribution (str): Allowed values: `hour`, `day`, `day-hours`, `month` or `year`. Defaults to `day`.
            timezone (str): IANA Time Zone (e.g. America/Phoenix).
                            Defaults to the requester's timezone.
                            When the requester's timezone isn't present, then `filters.from` is parsed to get the timezone.
            filters (dict): If none provided, your report will span the last seven days.
            payload (dict): Custom payload to be used as request's data.
                            It overrides all other parameters provided for the method.
            headers (dict): Custom headers to be used with session headers.
                            They will be merged with session-level values that are set,
                            however, these method-level parameters will not be persisted across requests.

        Returns:
            httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/agents/availability',
                                 json=payload,
                                 headers=headers)

    def performance(self,
                    distribution: str = None,
                    timezone: str = None,
                    filters: dict = None,
                    payload: dict = None,
                    headers: dict = None) -> httpx.Response:
        ''' Shows for how long an agent, group, or the whole account was available for chatting during a specified period of time.

        Args:
            distribution (str): Allowed values: `hour`, `day`, `day-hours`, `month` or `year`. Defaults to `day`.
            timezone (str): IANA Time Zone (e.g. America/Phoenix).
                            Defaults to the requester's timezone.
                            When the requester's timezone isn't present, then `filters.from` is parsed to get the timezone.
            filters (dict): If none provided, your report will span the last seven days.
            payload (dict): Custom payload to be used as request's data.
                            It overrides all other parameters provided for the method.
            headers (dict): Custom headers to be used with session headers.
                            They will be merged with session-level values that are set,
                            however, these method-level parameters will not be persisted across requests.

        Returns:
            httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/agents/performance',
                                 json=payload,
                                 headers=headers)

    def response_time(self,
                      distribution: str = None,
                      timezone: str = None,
                      filters: dict = None,
                      payload: dict = None,
                      headers: dict = None) -> httpx.Response:
        ''' Shows the average agents' response time within a licence.

        Args:
            distribution (str): Allowed values: `hour`, `day`, `day-hours`, `month` or `year`. Defaults to `day`.
            timezone (str): IANA Time Zone (e.g. America/Phoenix).
                            Defaults to the requester's timezone.
                            When the requester's timezone isn't present, then `filters.from` is parsed to get the timezone.
            filters (dict): If none provided, your report will span the last seven days.
            payload (dict): Custom payload to be used as request's data.
                            It overrides all other parameters provided for the method.
            headers (dict): Custom headers to be used with session headers.
                            They will be merged with session-level values that are set,
                            however, these method-level parameters will not be persisted across requests.

        Returns:
            httpx.Response: The Response object from `httpx` library,
                            which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/agents/response_time',
                                 json=payload,
                                 headers=headers)

    def first_response_time(self,
                            distribution: str = None,
                            timezone: str = None,
                            filters: dict = None,
                            payload: dict = None,
                            headers: dict = None) -> httpx.Response:
        ''' Shows the average agents' first response time within a licence.

        Args:
            distribution (str): Allowed values: `hour`, `day`, `day-hours`, `month` or `year`. Defaults to `day`.
            timezone (str): IANA Time Zone (e.g. America/Phoenix).
                            Defaults to the requester's timezone.
                            When the requester's timezone isn't present, then `filters.from` is parsed to get the timezone.
            filters (dict): If none provided, your report will span the last seven days.
            payload (dict): Custom payload to be used as request's data.
                            It overrides all other parameters provided for the method.
            headers (dict): Custom headers to be used with session headers.
                            They will be merged with session-level values that are set,
                            however, these method-level parameters will not be persisted across requests.

        Returns:
            httpx.Response: The Response object from `httpx` library,
                            which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/agents/first_response_time',
                                 json=payload,
                                 headers=headers)


class ReportsAPI33(ReportsApiInterface):
    ''' Configuration API client in version 3.3 class. '''

    # Chats
    def agents_chatting_duration(self,
                                 date_to: str = None,
                                 date_from: str = None,
                                 agents: str = None,
                                 groups: str = None,
                                 tags: str = None,
                                 customer_client_ids: str = None,
                                 distribution: str = None,
                                 timezone: str = None,
                                 tagged: bool = None,
                                 payload: dict = None,
                                 headers: dict = None) -> httpx.Response:
        ''' Shows the average chatting duration of agents within a license.

        Args:
            date_to (str): Date in the RFC3339 format, which also contains a timezone.
                      This timezone will be used if no `timezone` is provided.
            date_from (str): Date in the RFC3339 format, which also contains a timezone.
                              This timezone will be used if no `timezone` is provided.
            agents (str): Agent emails separated by a comma.
                          If not specified, returns the data for all agents within the license.
            groups (str): Group IDs separated by a comma.
            tags (str): Names of tags separated by a comma.
            customer_client_ids (str): Client IDs separated by a comma.
            distribution (str): Possible values: `hour`, `day-hours`, `day`, `month`; defaults to `day`.
            timezone (str): Timezone in the TZ format (e.g. America/Phoenix).
                            Defaults to the requester's timezone.
                            If not present, `from` is parsed to get the requester's timezone.
            tagged (bool): Possible values: `true`, `1`, `false`, `0`
            payload (dict): Custom payload to be used as request's data.
                            It overrides all other parameters provided for the method.
            headers (dict): Custom headers to be used with session headers.
                            They will be merged with session-level values that are set,
                            however, these method-level parameters will not be persisted across requests.

        Returns:
            httpx.Response: The Response object from `httpx` library,
                            which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
            if date_from is not None:
                payload['from'] = date_from
            if date_to is not None:
                payload['to'] = date_to
        return self.session.get(
            f'{self.api_url}/chats/agents_chatting_duration',
            params=payload,
            headers=headers)


class ReportsAPI34(ReportsApiInterface):
    ''' Configuration API client in version 3.4 class. '''


class ReportsAPI35(ReportsApiInterface):
    ''' Configuration API client in version 3.5 class. '''
