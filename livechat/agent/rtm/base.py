''' Agent RTM client implementation. '''

# pylint: disable=W0613,W0622,C0103,R0913,R0903,W0107,W0221
from __future__ import annotations

from livechat.agent.rtm.api.v33 import AgentRTMV33
from livechat.agent.rtm.api.v34 import AgentRTMV34
from livechat.agent.rtm.api.v35 import AgentRTMV35
from livechat.config import CONFIG

stable_version = CONFIG.get('stable')
api_url = CONFIG.get('url')


class AgentRTM:
    ''' Main class that gets specific client. '''
    @staticmethod
    def get_client(version: str = stable_version,
                   base_url: str = api_url) -> AgentRTMInterface:
        ''' Returns client for specific Agent RTM version.

            Args:
                version (str): API's version. Defaults to the stable version of API.
                base_url (str): API's base url. Defaults to API's production URL.

            Returns:
                AgentRTMInterface: API client object for specified version.

            Raises:
                ValueError: If the specified version does not exist.
        '''
        client = {
            '3.3': AgentRTMV33(base_url),
            '3.4': AgentRTMV34(base_url),
            '3.5': AgentRTMV35(base_url),
        }.get(version)
        if not client:
            raise ValueError('Provided version does not exist.')
        return client
