''' Module with base class that allows retrieval of client for specific Configuration
    API version. '''

# pylint: disable=W0613,W0622,C0103,R0913,R0903
from __future__ import annotations

from typing import Union

import httpx

from livechat.config import CONFIG
from livechat.configuration.api.v33 import ConfigurationApiV33
from livechat.configuration.api.v34 import ConfigurationApiV34
from livechat.configuration.api.v35 import ConfigurationApiV35
from livechat.configuration.api.v36 import ConfigurationApiV36
from livechat.utils.structures import AccessToken

stable_version = CONFIG.get('stable')
api_url = CONFIG.get('url')


class ConfigurationApi:
    ''' Base class that allows retrieval of client for specific Configuration
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
    ) -> Union[ConfigurationApiV33, ConfigurationApiV34, ConfigurationApiV35,
               ConfigurationApiV36]:
        ''' Returns client for specific Configuration API version.

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
                ConfigurationApi: API client object for specified version.

            Raises:
                ValueError: If the specified version does not exist.
        '''
        client = {
            '3.3':
            ConfigurationApiV33(token, base_url, http2, proxies, verify,
                                disable_logging, timeout),
            '3.4':
            ConfigurationApiV34(token, base_url, http2, proxies, verify,
                                disable_logging, timeout),
            '3.5':
            ConfigurationApiV35(token, base_url, http2, proxies, verify,
                                disable_logging, timeout),
            '3.6':
            ConfigurationApiV36(token, base_url, http2, proxies, verify,
                                disable_logging, timeout),
        }.get(version)
        if not client:
            raise ValueError('Provided version does not exist.')
        return client
