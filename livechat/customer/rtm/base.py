''' Customer RTM client implementation. '''

# pylint: disable=C0103,R0903,R0913,W0107,W0231,W0613,W0622

from typing import Callable, Union

from livechat.config import CONFIG
from livechat.customer.rtm.api.v34 import CustomerRtmV34
from livechat.customer.rtm.api.v35 import CustomerRtmV35
from livechat.customer.rtm.api.v36 import CustomerRtmV36
from livechat.customer.rtm.api.v37 import CustomerRtmV37

stable_version = CONFIG.get('stable')
api_url = CONFIG.get('url')


class CustomerRTM:
    ''' Main class that gets specific client. '''
    @staticmethod
    def get_client(
        version: str = stable_version,
        base_url: str = api_url,
        organization_id: str = None,
        header: Union[list, dict, Callable, None] = None,
    ) -> Union[CustomerRtmV34, CustomerRtmV35, CustomerRtmV36, CustomerRtmV37]:
        ''' Returns client for specific Customer RTM version.

            Args:
                version (str): API's version. Defaults to the stable version of API.
                base_url (str): API's base url. Defaults to API's production URL.
                organization_id (str): Organization ID, replaced license ID in v3.4.
                header (Union[list, dict, Callable, None]): Custom header for websocket handshake.
                        If the parameter is a callable object, it is called just before the connection attempt.

            Returns:
                API client object for specified version.

            Raises:
                ValueError: If the specified version does not exist.
        '''
        client = {
            '3.4': CustomerRtmV34,
            '3.5': CustomerRtmV35,
            '3.6': CustomerRtmV36,
            '3.7': CustomerRtmV37,
        }.get(version)
        if client:
            client_kwargs = {
                'organization_id': organization_id,
                'base_url': base_url
            }
            return client(**client_kwargs, header=header)
        raise ValueError('Provided version does not exist.')
