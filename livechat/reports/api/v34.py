''' Reports API module with client class in version 3.4. '''

import httpx

from livechat.utils.helpers import prepare_payload
from livechat.utils.http_client import HttpClient


class ReportsApiV34(HttpClient):
    ''' Reports API client class in version 3.4. '''
    def __init__(self,
                 token: str,
                 base_url: str,
                 http2: bool,
                 proxies=None,
                 verify: bool = True,
                 disable_logging: bool = False):
        super().__init__(token, base_url, http2, proxies, verify,
                         disable_logging)
        self.api_url = f'https://{base_url}/v3.4/reports'

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
        return self.session.post(f'{self.api_url}/chats/response_time',
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
        return self.session.post(f'{self.api_url}/chats/first_response_time',
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
