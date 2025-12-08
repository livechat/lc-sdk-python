''' Agent RTM client implementation. '''

# pylint: disable=W0613,W0622,C0103,R0913,R0903,W0107,W0221
from __future__ import annotations

from typing import Callable, Union

from livechat.agent.rtm.api.v34 import AgentRtmV34
from livechat.agent.rtm.api.v35 import AgentRtmV35
from livechat.agent.rtm.api.v36 import AgentRtmV36
from livechat.agent.rtm.api.v37 import AgentRtmV37
from livechat.config import CONFIG

stable_version = CONFIG.get('stable')
api_url = CONFIG.get('url')


class AgentRTM:
    ''' Main class that gets specific client. '''
    @staticmethod
    def get_client(
        version: str = stable_version,
        base_url: str = api_url,
        header: Union[list, dict, Callable, None] = None,
    ) -> Union[AgentRtmV34, AgentRtmV35, AgentRtmV36, AgentRtmV37]:
        ''' Returns client for specific Agent RTM version.

            Args:
                version (str): API's version. Defaults to the stable version of API.
                base_url (str): API's base url. Defaults to API's production URL.
                header (Union[list, dict, Callable, None]): Custom header for websocket handshake.
                        If the parameter is a callable object, it is called just before the connection attempt.

            Returns:
                API client object for specified version.

            Raises:
                ValueError: If the specified version does not exist.
        '''
        client = {
            '3.4': AgentRtmV34,
            '3.5': AgentRtmV35,
            '3.6': AgentRtmV36,
            '3.7': AgentRtmV37,
        }.get(version)
        if not client:
            raise ValueError('Provided version does not exist.')
        return client(base_url, header)
