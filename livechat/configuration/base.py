''' Module with base class that allows retrieval of client for specific Configuration
    API version. '''

# pylint: disable=W0613,W0622,C0103,R0913,R0903
from __future__ import annotations

from typing import Union

from livechat.config import CONFIG
from livechat.configuration.api.v33 import ConfigurationApiV33
from livechat.configuration.api.v34 import ConfigurationApiV34
from livechat.configuration.api.v35 import ConfigurationApiV35

stable_version = CONFIG.get('stable')
api_url = CONFIG.get('url')


class ConfigurationApi:
    ''' Base class that allows retrieval of client for specific Configuration
        API version. '''
    @staticmethod
    def get_client(
        token: str,
        version: str = stable_version,
        base_url: str = api_url,
        http2: bool = False
    ) -> Union[ConfigurationApiV33, ConfigurationApiV34, ConfigurationApiV35]:
        ''' Returns client for specific Configuration API version.

            Args:
                token (str): Full token with type (Bearer/Basic) that will be
                             used as `Authorization` header in requests to API.
                version (str): API's version. Defaults to the stable version of API.
                base_url (str): API's base url. Defaults to API's production URL.
                http2 (bool): A boolean indicating if HTTP/2 support should be
                              enabled. Defaults to `False`.

            Returns:
                ConfigurationApi: API client object for specified version.

            Raises:
                ValueError: If the specified version does not exist.
        '''
        client = {
            '3.3': ConfigurationApiV33(token, base_url, http2),
            '3.4': ConfigurationApiV34(token, base_url, http2),
            '3.5': ConfigurationApiV35(token, base_url, http2),
        }.get(version)
        if not client:
            raise ValueError('Provided version does not exist.')
        return client