''' Reports API module with client class in version 3.3. '''

import httpx

from livechat.utils.helpers import prepare_payload
from livechat.utils.http_client import HttpClient


class ReportsApiV33(HttpClient):
    ''' Reports API client class in version 3.3. '''
    def __init__(self,
                 token: str,
                 base_url: str,
                 http2: bool,
                 proxies=None,
                 verify: bool = True):
        super().__init__(token, base_url, http2, proxies, verify)
        self.api_url = f'https://{base_url}/v3.3/reports'

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
                            which contains a server's response to an HTTP request.
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
                                which contains a server's response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.get(f'{self.api_url}/chats/tags',
                                params=payload,
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
                                which contains a server's response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.get(f'{self.api_url}/chats/total_chats',
                                params=payload,
                                headers=headers)
