Module base
===========
Agent RTM client implementation.

Classes
-------

`AgentRTM()`
:   Main class that gets specific client.

    ### Static methods

    `get_client(version: str = '3.4', base_url: str = 'api.livechatinc.com') ‑> Union[livechat.agent.rtm.api.v33.AgentRtmV33, livechat.agent.rtm.api.v34.AgentRtmV34, livechat.agent.rtm.api.v35.AgentRtmV35]`
    :   Returns client for specific Agent RTM version.

        Args:
            version (str): API's version. Defaults to the stable version of API.
            base_url (str): API's base url. Defaults to API's production URL.

        Returns:
            API client object for specified version.

        Raises:
            ValueError: If the specified version does not exist.
