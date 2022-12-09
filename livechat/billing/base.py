''' Module with base class that allows retrieval of client for specific
    Billing API version. '''

# pylint: disable=W0613,W0622,C0103,R0913,R0903

from __future__ import annotations

from .api import BillingApiV1


class BillingApi:
    ''' Base class that allows retrieval of client for specific
        Billing API version. '''
    @staticmethod
    def get_client(token: str,
                   version: str = 'v1',
                   base_url: str = 'billing.livechatinc.com',
                   http2: bool = False,
                   proxies: dict = None,
                   verify: bool = True) -> BillingApiV1:
        ''' Returns client for specific Billing API version.

            Args:
                token (str): Full token with type Bearer that will be
                    used as `Authorization` header in requests to API.
                version (str): API's version. Defaults to the v2 version of API.
                base_url (str): API's base url. Defaults to API's production URL.
                http2 (bool): A boolean indicating if HTTP/2 support should be
                              enabled. Defaults to `False`.
                proxies (dict): A dictionary mapping proxy keys to proxy URLs.
                verify (bool): SSL certificates (a.k.a CA bundle) used to
                               verify the identity of requested hosts. Either `True` (default CA bundle),
                               a path to an SSL certificate file, an `ssl.SSLContext`, or `False`
                               (which will disable verification). Defaults to `True`.

            Returns:
                BillingApi: API client object for specified version.

            Raises:
                ValueError: If the specified version does not exist.
        '''
        client = {
            'v1': BillingApiV1(token, base_url, http2, proxies, verify),
        }.get(version)
        if not client:
            raise ValueError('Provided version does not exist.')
        return client
