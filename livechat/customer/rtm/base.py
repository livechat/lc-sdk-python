''' Customer RTM client implementation. '''

# pylint: disable=C0103,R0903,R0913,W0107,W0231,W0613,W0622

from typing import Union

from livechat.config import CONFIG
from livechat.customer.rtm.api.v33 import CustomerRtmV33
from livechat.customer.rtm.api.v34 import CustomerRtmV34
from livechat.customer.rtm.api.v35 import CustomerRtmV35

stable_version = CONFIG.get('stable')
api_url = CONFIG.get('url')


class CustomerRTM:
    ''' Main class that gets specific client. '''
    @staticmethod
    def get_client(
        version: str = stable_version,
        base_url: str = api_url,
        license_id: int = None,
        organization_id: str = None
    ) -> Union[CustomerRtmV33, CustomerRtmV34, CustomerRtmV35]:
        ''' Returns client for specific Customer RTM version.

            Args:
                license_id (int): License ID. Required to use for API version <= 3.3.
                version (str): API's version. Defaults to the stable version of API.
                base_url (str): API's base url. Defaults to API's production URL.
                organization_id (str): Organization ID, replaced license ID in v3.4.

            Returns:
                CustomerRTM: API client object for specified version.

            Raises:
                ValueError: If the specified version does not exist.
        '''
        client = {
            '3.3': CustomerRtmV33(base_url, license_id),
            '3.4': CustomerRtmV34(base_url, organization_id),
            '3.5': CustomerRtmV35(base_url, organization_id),
        }.get(version)
        if not client:
            raise ValueError('Provided version does not exist.')
        return client
