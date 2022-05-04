''' Customer Web client implementation. '''

# pylint: disable=W0613,R0913,W0622,C0103
from __future__ import annotations

from typing import Union

from livechat.config import CONFIG
from livechat.customer.web.api.v33 import CustomerWebV33
from livechat.customer.web.api.v34 import CustomerWebV34
from livechat.customer.web.api.v35 import CustomerWebV35

stable_version = CONFIG.get('stable')
api_url = CONFIG.get('url')


# pylint: disable=R0903
class CustomerWeb:
    ''' Allows retrieval of client for specific Customer Web
        API version. '''
    @staticmethod
    def get_client(
        license_id: int = None,
        access_token: str = None,
        version: str = stable_version,
        base_url: str = api_url,
        http2: bool = False,
        organization_id: str = None
    ) -> Union[CustomerWebV33, CustomerWebV34, CustomerWebV35]:
        ''' Returns client for specific API version.

            Args:
                license_id (int): License ID. Required to use for API version <= 3.3.
                token (str): Full token with type (Bearer/Basic) that will be
                             used as `Authorization` header in requests to API.
                version (str): API's version. Defaults to the stable version of API.
                base_url (str): API's base url. Defaults to API's production URL.
                http2 (bool): A boolean indicating if HTTP/2 support should be
                              enabled. Defaults to `False`.
                organization_id (str): Organization ID, replaced license ID in v3.4.

            Returns:
                API client object for specified version based on
                `CustomerWebApiInterface`.

            Raises:
                ValueError: If the specified version does not exist.
        '''
        client = {
            '3.3': CustomerWebV33,
            '3.4': CustomerWebV34,
            '3.5': CustomerWebV35,
        }.get(version)
        client_kwargs = {
            '3.3': {
                'license_id': license_id,
                'access_token': access_token,
                'base_url': base_url,
                'http2': http2
            },
            '3.4': {
                'organization_id': organization_id,
                'access_token': access_token,
                'base_url': base_url,
                'http2': http2
            },
            '3.5': {
                'organization_id': organization_id,
                'access_token': access_token,
                'base_url': base_url,
                'http2': http2
            },
        }.get(version)
        if client:
            return client(**client_kwargs)
        raise ValueError('Provided version does not exist.')
