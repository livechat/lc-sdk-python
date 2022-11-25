''' Module with class allowing retrieval of client for specific version of Agent Web API. '''

# pylint: disable=W0613,R0913,W0622,C0103,W0221
from __future__ import annotations

from typing import Union

from livechat.agent.web.api.v33 import AgentWebV33
from livechat.agent.web.api.v34 import AgentWebV34
from livechat.agent.web.api.v35 import AgentWebV35
from livechat.agent.web.api.v36 import AgentWebV36
from livechat.config import CONFIG

stable_version = CONFIG.get('stable')
api_url = CONFIG.get('url')


class AgentWeb:
    ''' Allows retrieval of client for specific Agent Web
        API version. '''
    @staticmethod
    def get_client(
            access_token: str,
            version: str = stable_version,
            base_url: str = api_url,
            http2: bool = False,
            proxies: dict = None,
            verify: bool = True
    ) -> Union[AgentWebV33, AgentWebV34, AgentWebV35]:
        ''' Returns client for specific API version.

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

            Returns:
                API client object for specified version.

            Raises:
                ValueError: If the specified version does not exist.
        '''
        client = {
            '3.3': AgentWebV33(access_token, base_url, http2, proxies, verify),
            '3.4': AgentWebV34(access_token, base_url, http2, proxies, verify),
            '3.5': AgentWebV35(access_token, base_url, http2, proxies, verify),
            '3.6': AgentWebV36(access_token, base_url, http2, proxies, verify),
        }.get(version)
        if not client:
            raise ValueError('Provided version does not exist.')
        return client
