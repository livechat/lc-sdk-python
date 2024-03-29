''' Module with base class that allows retrieval of client for specific Reports
    API version. '''

# pylint: disable=W0613,W0622,C0103,R0913,R0903

from __future__ import annotations

from typing import Union

import httpx

from livechat.config import CONFIG
from livechat.reports.api.v33 import ReportsApiV33
from livechat.reports.api.v34 import ReportsApiV34
from livechat.reports.api.v35 import ReportsApiV35
from livechat.reports.api.v36 import ReportsApiV36
from livechat.utils.structures import AccessToken

stable_version = CONFIG.get('stable')
api_url = CONFIG.get('url')


class ReportsApi:
    ''' Base class that allows retrieval of client for specific Reports
        API version. '''
    @staticmethod
    def get_client(
        token: Union[AccessToken, str],
        version: str = stable_version,
        base_url: str = api_url,
        http2: bool = False,
        proxies: dict = None,
        verify: bool = True,
        disable_logging: bool = False,
        timeout: float = httpx.Timeout(15)
    ) -> Union[ReportsApiV33, ReportsApiV34, ReportsApiV35, ReportsApiV36]:
        ''' Returns client for specific Reports API version.

            Args:
                token (str): Full token with type (Bearer/Basic) that will be
                             used as `Authorization` header in requests to API.
                version (str): API's version. Defaults to the stable version of API.
                base_url (str): API's base url. Defaults to API's production URL.
                http2 (bool): A boolean indicating if HTTP/2 support should be
                              enabled. Defaults to `False`.
                proxies (dict): A dictionary mapping proxy keys to proxy URLs.
                verify (bool): SSL certificates (a.k.a CA bundle) used to
                               verify the identity of requested hosts. Either `True` (default CA bundle),
                               a path to an SSL certificate file, an `ssl.SSLContext`, or `False`
                               (which will disable verification). Defaults to `True`.
                disable_logging (bool): indicates if logging should be disabled.
                timeout (float): The timeout configuration to use when sending requests.
                                 Defaults to 15 seconds.

            Returns:
                ReportsApi: API client object for specified version.

            Raises:
                ValueError: If the specified version does not exist.
        '''
        client = {
            '3.3':
            ReportsApiV33(token, base_url, http2, proxies, verify,
                          disable_logging, timeout),
            '3.4':
            ReportsApiV34(token, base_url, http2, proxies, verify,
                          disable_logging, timeout),
            '3.5':
            ReportsApiV35(token, base_url, http2, proxies, verify,
                          disable_logging, timeout),
            '3.6':
            ReportsApiV36(token, base_url, http2, proxies, verify,
                          disable_logging, timeout),
        }.get(version)
        if not client:
            raise ValueError('Provided version does not exist.')
        return client
