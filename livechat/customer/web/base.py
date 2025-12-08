''' Customer Web client implementation. '''

# pylint: disable=W0613,R0913,W0622,C0103
from __future__ import annotations

from typing import Optional, Union

import httpx

from livechat.config import CONFIG
from livechat.customer.web.api.v34 import CustomerWebV34
from livechat.customer.web.api.v35 import CustomerWebV35
from livechat.customer.web.api.v36 import CustomerWebV36
from livechat.customer.web.api.v37 import CustomerWebV37
from livechat.utils.structures import AccessToken

stable_version = CONFIG.get('stable')
api_url = CONFIG.get('url')


# pylint: disable=R0903
class CustomerWeb:
    ''' Allows retrieval of client for specific Customer Web
        API version. '''
    @staticmethod
    def get_client(
        access_token: Optional[Union[AccessToken, str]] = None,
        version: str = stable_version,
        base_url: str = api_url,
        http2: bool = False,
        proxies: dict = None,
        verify: bool = True,
        organization_id: str = None,
        disable_logging: bool = False,
        timeout: float = httpx.Timeout(15)
    ) -> Union[CustomerWebV34, CustomerWebV35, CustomerWebV36, CustomerWebV37]:
        ''' Returns client for specific API version.

            Args:
                access_token (str): Full token with type (Bearer/Basic) that will be
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
                organization_id (str): Organization ID, replaced license ID in v3.4.
                disable_logging (bool): indicates if logging should be disabled.
                timeout (float): The timeout configuration to use when sending requests.
                                 Defaults to 15 seconds.

            Returns:
                API client object for specified version based on
                `CustomerWebApiInterface`.

            Raises:
                ValueError: If the specified version does not exist.
        '''
        client = {
            '3.4': CustomerWebV34,
            '3.5': CustomerWebV35,
            '3.6': CustomerWebV36,
            '3.7': CustomerWebV37,
        }.get(version)
        if client:
            client_kwargs = {
                'organization_id': organization_id,
                'access_token': access_token,
                'base_url': base_url,
                'http2': http2,
                'proxies': proxies,
                'verify': verify,
                'disable_logging': disable_logging,
                'timeout': timeout
            }
            return client(**client_kwargs)
        raise ValueError('Provided version does not exist.')
