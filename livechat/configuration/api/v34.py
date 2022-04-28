''' Configuration API module with client class in version 3.4. '''

import httpx

from livechat.utils.helpers import prepare_payload
from livechat.utils.http_client import HttpClient


class ConfigurationApiV34(HttpClient):
    ''' Configuration API client class in version 3.4. '''
    def __init__(self,
                 token: str,
                 base_url: str,
                 http2: bool,
                 proxies=None,
                 verify: bool = True):
        super().__init__(token, base_url, http2, proxies, verify)
        self.api_url = f'https://{base_url}/v3.4/configuration/action'

# Agents

    def create_agent(self,
                     id: str = None,
                     name: str = None,
                     role: str = None,
                     avatar_path: str = None,
                     job_title: str = None,
                     mobile: str = None,
                     max_chats_count: int = None,
                     awaiting_approval: bool = None,
                     groups: list = None,
                     notifications: list = None,
                     email_subscriptions: list = None,
                     work_scheduler: dict = None,
                     payload: dict = None,
                     headers: dict = None) -> httpx.Response:
        ''' Creates a new Agent with specified parameters within a license.

            Args:
                id (str): Agent's ID.
                name (str): Agent's name.
                role (str): Agent role, should be one of the following:
                            `viceowner`, `administrator`, `normal` (default).
                avatar_path (str): URL path of the Agent's avatar.
                job_title (str): Agent's job title.
                mobile (str): Agent's mobile number.
                max_chats_count (int): Agent's maximum number of concurrent chats.
                awaiting_approval (bool): Determines if the Agent will be awaiting
                                          approval after creation.
                groups (list): Groups an Agent belongs to.
                notifications (list): Represents which Agent notifications are turned on.
                email_subscriptions (list): Represents which subscriptions will be send to
                                           the Agent via email.
                work_scheduler (dict): Work scheduler options to set for the new Agent.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/create_agent',
                                 json=payload,
                                 headers=headers)

    def get_agent(self,
                  id: str = None,
                  fields: list = None,
                  payload: dict = None,
                  headers: dict = None) -> httpx.Response:
        ''' Returns the info about an Agent specified by `id`.

            Args:
                id (str): Agent's ID.
                fields (list): Additional fields to include.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/get_agent',
                                 json=payload,
                                 headers=headers)

    def list_agents(self,
                    filters: dict = None,
                    fields: list = None,
                    payload: dict = None,
                    headers: dict = None) -> httpx.Response:
        ''' Returns all Agents within a license.

            Args:
                filters (dict): Possible request filters.
                fields (list): Additional fields to include.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/list_agents',
                                 json=payload,
                                 headers=headers)

    def update_agent(self,
                     id: str = None,
                     name: str = None,
                     role: str = None,
                     avatar_path: str = None,
                     job_title: str = None,
                     mobile: str = None,
                     max_chats_count: int = None,
                     groups: list = None,
                     notifications: list = None,
                     email_subscriptions: list = None,
                     work_scheduler: dict = None,
                     payload: dict = None,
                     headers: dict = None) -> httpx.Response:
        ''' Updates the properties of an Agent specified by `id`.

            Args:
                id (str): Agent's ID.
                name (str): Agent's name.
                role (str): Agent role, should be one of the following:
                            `viceowner`, `administrator`, `normal` (default).
                avatar_path (str): URL path of the Agent's avatar.
                job_title (str): Agent's job title.
                mobile (str): Agent's mobile number.
                max_chats_count (int): Agent's maximum number of concurrent chats.
                groups (list): Groups an Agent belongs to.
                notifications (list): Represents which Agent notifications are turned on.
                email_subscriptions (list): Represents which subscriptions will be send to
                                           the Agent via email.
                work_scheduler (dict): Work scheduler options to set for the new Agent.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/update_agent',
                                 json=payload,
                                 headers=headers)

    def delete_agent(self,
                     id: str = None,
                     payload: dict = None,
                     headers: dict = None) -> httpx.Response:
        ''' Deletes an Agent specified by `id`.

            Args:
                id (str): Agent's ID.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/delete_agent',
                                 json=payload,
                                 headers=headers)

    def suspend_agent(self,
                      id: str = None,
                      payload: dict = None,
                      headers: dict = None) -> httpx.Response:
        ''' Suspends an Agent specified by `id`.

            Args:
                id (str): Agent's ID.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/suspend_agent',
                                 json=payload,
                                 headers=headers)

    def unsuspend_agent(self,
                        id: str = None,
                        payload: dict = None,
                        headers: dict = None) -> httpx.Response:
        ''' Unsuspends an Agent specified by `id`.

            Args:
                id (str): Agent's ID.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/unsuspend_agent',
                                 json=payload,
                                 headers=headers)

    def request_agent_unsuspension(self,
                                   payload: dict = None,
                                   headers: dict = None) -> httpx.Response:
        ''' A suspended Agent can send emails to license owners and vice owners
            with an unsuspension request.

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/request_agent_unsuspension',
                                 json=payload,
                                 headers=headers)

    def approve_agent(self,
                      id: str = None,
                      payload: dict = None,
                      headers: dict = None) -> httpx.Response:
        ''' Approves an Agent thus allowing the Agent to use the application.

            Args:
                id (str): Agent's ID.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/approve_agent',
                                 json=payload,
                                 headers=headers)

# Auto access

    def add_auto_access(self,
                        access: dict = None,
                        conditions: dict = None,
                        description: str = None,
                        next_id: str = None,
                        payload: dict = None,
                        headers: dict = None) -> httpx.Response:
        ''' Creates an auto access data structure, which is a set of conditions
            for the tracking URL and geolocation of a customer.

        Args:
            access (dict): Destination access.
            conditions (dict): Conditions to check.
            description (str): 	Description of the auto access.
            next_id (str): ID of an existing auto access.
            payload (dict): Custom payload to be used as request's data.
                            It overrides all other parameters provided for the method.
            headers (dict): Custom headers to be used with session headers.
                            They will be merged with session-level values that are set,
                            however, these method-level parameters will not be persisted across requests.

        Returns:
            httpx.Response: The Response object from `httpx` library,
                            which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/add_auto_access',
                                 json=payload,
                                 headers=headers)

    def list_auto_accesses(self,
                           payload: dict = None,
                           headers: dict = None) -> httpx.Response:
        ''' Returns all existing auto access data structures.

        Args:
            payload (dict): Custom payload to be used as request's data.
                            It overrides all other parameters provided for the method.
            headers (dict): Custom headers to be used with session headers.
                            They will be merged with session-level values that are set,
                            however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/list_auto_accesses',
                                 json=payload,
                                 headers=headers)

    def delete_auto_access(self,
                           id: str = None,
                           payload: dict = None,
                           headers: dict = None) -> httpx.Response:
        ''' Deletes an existing auto access data structure specified by its ID.

            Args:
                id (str): Auto access ID.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/delete_auto_access',
                                 json=payload,
                                 headers=headers)

    def update_auto_access(self,
                           id: str = None,
                           next_id: str = None,
                           payload: dict = None,
                           headers: dict = None) -> httpx.Response:
        ''' Moves an existing auto access data structure, specified by id,
            before another one, specified by next_id.

            Args:
                id (str): ID of the auto access to move.
                next_id (str): ID of the auto access that should follow the moved auto access.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/update_auto_access',
                                 json=payload,
                                 headers=headers)

# Bots

    def create_bot(self,
                   name: str = None,
                   avatar: str = None,
                   max_chats_count: int = None,
                   groups: list = None,
                   webhooks: dict = None,
                   work_scheduler: dict = None,
                   timezone: str = None,
                   owner_client_id: str = None,
                   payload: dict = None,
                   headers: dict = None) -> httpx.Response:
        ''' Creates a new Bot.

            Args:
                name (str): Display name.
                avatar (str): Avatar URL.
                max_chats_count (int): Max. number of incoming chats that can be routed to the Bot; default: 6.
                groups (list): Groups the Bot belongs to.
                webhooks (dict): Webhooks sent to the Bot.
                work_scheduler (dict): Work scheduler options to set for the new Bot.
                timezone (str): The time zone in which the Bot's work scheduler should operate.
                owner_client_id (str): Required only when authorizing via PATs.
                                The request will be rejected if you provide owner_client_id when authorizing with a Bearer Token.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/create_bot',
                                 json=payload,
                                 headers=headers)

    def delete_bot(self,
                   id: str = None,
                   payload: dict = None,
                   headers: dict = None) -> httpx.Response:
        ''' Deletes a Bot.

            Args:
                id (str): Bot's ID.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/delete_bot',
                                 json=payload,
                                 headers=headers)

    def update_bot(self,
                   id: str = None,
                   name: str = None,
                   avatar: str = None,
                   max_chats_count: int = None,
                   groups: list = None,
                   webhooks: dict = None,
                   work_scheduler: dict = None,
                   timezone: str = None,
                   payload: dict = None,
                   headers: dict = None) -> httpx.Response:
        ''' Updates an existing Bot.

            Args:
                id (str): Bot's ID.
                name (str): Display name.
                avatar (str): Avatar URL.
                max_chats_count (int): Max. number of incoming chats that can be routed to the Bot.
                groups (list): Groups the Bot belongs to.
                webhooks (dict): Webhooks sent to the Bot.
                work_scheduler (dict): Work scheduler options to set for the new Bot.
                timezone (str): The time zone in which the Bot's work scheduler should operate.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/update_bot',
                                 json=payload,
                                 headers=headers)

    def list_bots(self,
                  all: bool = None,
                  fields: list = None,
                  payload: dict = None,
                  headers: dict = None) -> httpx.Response:
        ''' Returns the list of Bots created within a license.

            Args:
                all (bool): `True` gets all Bots within a license. `False` (default) returns only the requester's Bots.
                fields (list): Additional Bot fields to include.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/list_bots',
                                 json=payload,
                                 headers=headers)

    def get_bot(self,
                id: str = None,
                fields: list = None,
                payload: dict = None,
                headers: dict = None) -> httpx.Response:
        ''' Gets a Bot specified by `id`.

            Args:
                id (str): Bot's ID.
                fields (list): Additional Bot fields to include.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/get_bot',
                                 json=payload,
                                 headers=headers)

# Groups

    def create_group(self,
                     name: str = None,
                     language_code: str = None,
                     agent_priorities: dict = None,
                     payload: dict = None,
                     headers: dict = None) -> httpx.Response:
        ''' Creates a new group.

            Args:
                name (str): Group name (up to 180 chars).
                language_code (str): The code of the group languange.
                agent_priorities (dict): Agents' priorities in a group as a map in the "<id>": "<priority>" format.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/create_group',
                                 json=payload,
                                 headers=headers)

    def update_group(self,
                     id: int = None,
                     name: str = None,
                     language_code: str = None,
                     agent_priorities: dict = None,
                     payload: dict = None,
                     headers: dict = None) -> httpx.Response:
        ''' Updates an existing group.

            Args:
                id (int): Groups' ID.
                name (str): Group name (up to 180 chars).
                language_code (str): The code of the group languange.
                agent_priorities (dict): Agents' priorities in a group as a map in the "<id>": "<priority>" format.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/update_group',
                                 json=payload,
                                 headers=headers)

    def delete_group(self,
                     id: int = None,
                     payload: dict = None,
                     headers: dict = None) -> httpx.Response:
        ''' Deletes an existing group.

            Args:
                id (int): Groups' ID.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/delete_group',
                                 json=payload,
                                 headers=headers)

    def list_groups(self,
                    fields: list = None,
                    payload: dict = None,
                    headers: dict = None) -> httpx.Response:
        ''' Lists all the exisiting groups.

            Args:
                fields (list): Additional fields to include.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/list_groups',
                                 json=payload,
                                 headers=headers)

    def get_group(self,
                  id: int = None,
                  fields: list = None,
                  payload: dict = None,
                  headers: dict = None) -> httpx.Response:
        ''' Returns details about a group specified by its id.

            Args:
                id (int): Groups' ID.
                fields (list): Additional fields to include.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/get_group',
                                 json=payload,
                                 headers=headers)

# Properties

    def register_property(self,
                          name: str = None,
                          owner_client_id: str = None,
                          type: str = None,
                          access: dict = None,
                          description: str = None,
                          domain: list = None,
                          range: dict = None,
                          default_value: str = None,
                          payload: dict = None,
                          headers: dict = None) -> httpx.Response:
        ''' Registers a new private property for a given Client ID.

            Args:
                name (str): Property name.
                owner_client_id (str): Client ID that will own the property; must be owned by your organization.
                type (str):  Possible values: `int`, `string`, `bool`, and `tokenized_string`.
                access (dict): Destination access.
                description (str): Property description.
                domain (list): Array of values that properties can be set to.
                range (dict): Range of values that properties can be set to.
                default_value (str): Default value of property; validated by domain or range, if one exists.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/register_property',
                                 json=payload,
                                 headers=headers)

    def unregister_property(self,
                            name: str = None,
                            owner_client_id: str = None,
                            payload: dict = None,
                            headers: dict = None) -> httpx.Response:
        ''' Unregisters a private property.

            Args:
                name (str): Property name.
                owner_client_id (str): Client ID that will own the property; must be owned by your organization.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/unregister_property',
                                 json=payload,
                                 headers=headers)

    def publish_property(self,
                         name: str = None,
                         owner_client_id: str = None,
                         access_type: list = None,
                         payload: dict = None,
                         headers: dict = None) -> httpx.Response:
        ''' Publishes a private property.

            Args:
                name (str): Property name.
                owner_client_id (str): Client ID that will own the property; must be owned by your organization.
                access_type (list): Possible values: `read`, `write`.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/publish_property',
                                 json=payload,
                                 headers=headers)

    def list_properties(self,
                        owner_client_id: str = None,
                        payload: dict = None,
                        headers: dict = None) -> httpx.Response:
        ''' Lists private and public properties owned by a given Client ID.

            Args:
                owner_client_id (str): Client ID that will own the property; must be owned by your organization.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/list_properties',
                                 json=payload,
                                 headers=headers)

    def update_license_properties(self,
                                  properties: dict = None,
                                  payload: dict = None,
                                  headers: dict = None) -> httpx.Response:
        ''' Updates a property value within a license. This operation doesn't
            overwrite the existing values.

            Args:
                properties (dict): An object with namespaces as keys and properties (grouped in objects) as values.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/update_license_properties',
                                 json=payload,
                                 headers=headers)

    def list_license_properties(self,
                                namespace: str = None,
                                name_prefix: str = None,
                                payload: dict = None,
                                headers: dict = None) -> httpx.Response:
        ''' Returns the properties set within a license.

            Args:
                namespace (str): Properties namespace.
                name_prefix (str): Properties name prefix.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/list_license_properties',
                                 json=payload,
                                 headers=headers)

    def delete_license_properties(self,
                                  properties: dict = None,
                                  payload: dict = None,
                                  headers: dict = None) -> httpx.Response:
        ''' Deletes the properties set within a license.

            Args:
                properties (dict): An object with namespaces as keys and property_names (in an array) as values.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/delete_license_properties',
                                 json=payload,
                                 headers=headers)

    def update_group_properties(self,
                                group_id: int = None,
                                properties: dict = None,
                                payload: dict = None,
                                headers: dict = None) -> httpx.Response:
        ''' Updates a property value within a group as the property location.
            This operation doesn't overwrite the existing values.

            Args:
                group_id (int): ID of the group you set the properties for.
                properties (dict): An object with namespaces as keys and properties (grouped in objects) as values.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/update_group_properties',
                                 json=payload,
                                 headers=headers)

    def list_group_properties(self,
                              id: int = None,
                              namespace: str = None,
                              name_prefix: str = None,
                              payload: dict = None,
                              headers: dict = None) -> httpx.Response:
        ''' Returns the properties set within a group.

            Args:
                id (int): ID of the group you retrieve properties from.
                namespace (str): Properties namespace.
                name_prefix (str): Properties name prefix.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/list_group_properties',
                                 json=payload,
                                 headers=headers)

    def delete_group_properties(self,
                                id: int = None,
                                properties: dict = None,
                                payload: dict = None,
                                headers: dict = None) -> httpx.Response:
        ''' Deletes the properties set within a group.

            Args:
                id (int): ID of the group you delete properties from.
                properties (dict): An object with namespaces as keys and property_names (in an array) as values.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/delete_group_properties',
                                 json=payload,
                                 headers=headers)

# Webhooks

    def register_webhook(self,
                         action: str = None,
                         secret_key: str = None,
                         url: str = None,
                         additional_data: list = None,
                         description: str = None,
                         filters: dict = None,
                         owner_client_id: str = None,
                         type: str = None,
                         payload: dict = None,
                         headers: dict = None) -> httpx.Response:
        ''' Registers a webhook for the Client ID (application) provided in the request.

            Args:
                action (str): The action that triggers sending a webhook.
                secret_key (str): The secret key sent in webhooks to verify the source of a webhook.
                url (str): Destination URL for the webhook.
                additional_data (list): Additional data arriving with the webhook.
                description (str): 	Webhook description.
                filters (dict): Filters to check if a webhook should be triggered.
                owner_client_id (str): The Client ID for which the webhook will be registered.
                type (str): `bot` or `license`.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/register_webhook',
                                 json=payload,
                                 headers=headers)

    def list_webhooks(self,
                      owner_client_id: str = None,
                      payload: dict = None,
                      headers: dict = None) -> httpx.Response:
        ''' Lists all webhooks registered for the given Client ID.

            Args:
                owner_client_id (str): The webhook owner (the Client ID for which the webhook is registered).
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/list_webhooks',
                                 json=payload,
                                 headers=headers)

    def unregister_webhook(self,
                           id: str = None,
                           owner_client_id: str = None,
                           payload: dict = None,
                           headers: dict = None) -> httpx.Response:
        ''' Unregisters a webhook previously registered for a Client ID (application).

            Args:
                id (str): Webhook's ID.
                owner_client_id (str): The webhook owner (the Client ID for which the webhook is registered).
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/unregister_webhook',
                                 json=payload,
                                 headers=headers)

    def list_webhook_names(self,
                           version: str = None,
                           payload: dict = None,
                           headers: dict = None) -> httpx.Response:
        ''' Lists all webhooks that are supported in a given API version. This method requires no authorization.

            Args:
                version (str): API's version. Defaults to the current stable API version.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/list_webhook_names',
                                 json=payload,
                                 headers=headers)

    def enable_license_webhooks(self,
                                owner_client_id: str = None,
                                payload: dict = None,
                                headers: dict = None) -> httpx.Response:
        ''' Enables the webhooks registered for a given Client ID (application)
            for the license associated with the access token used in the request.

            Args:
                owner_client_id (str): The webhook owner (the Client ID for which the webhook is registered).
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/enable_license_webhooks',
                                 json=payload,
                                 headers=headers)

    def disable_license_webhooks(self,
                                 owner_client_id: str = None,
                                 payload: dict = None,
                                 headers: dict = None) -> httpx.Response:
        ''' Disables the enabled webhooks.

            Args:
                owner_client_id (str): Required when authorizing via PATs; ignored otherwise.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/disable_license_webhooks',
                                 json=payload,
                                 headers=headers)

    def get_license_webhooks_state(self,
                                   owner_client_id: str = None,
                                   payload: dict = None,
                                   headers: dict = None) -> httpx.Response:
        ''' Gets the state of the webhooks registered for a given Client ID (application)
            on the license associated with the access token used in the request.

            Args:
                owner_client_id (str): Required when authorizing via PATs; ignored otherwise.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/get_license_webhooks_state',
                                 json=payload,
                                 headers=headers)


# Other

    def get_license_id(self,
                       organization_id: str = None,
                       params: dict = None,
                       headers: dict = None) -> httpx.Response:
        ''' Returns license ID by given organization ID.

            Args:
                organization_id (str): Organization ID to get license ID for.
                params (dict): Custom params to be used in request's query string.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if params is None:
            params = prepare_payload(locals())
        return self.session.get(f'{self.api_url}/get_license_id',
                                params=params,
                                headers=headers)

    def get_organization_id(self,
                            license_id: int = None,
                            params: dict = None,
                            headers: dict = None) -> httpx.Response:
        ''' Returns organization ID by given license ID.

            Args:
                license_id (int): License ID to get organization ID for.
                params (dict): Custom params to be used in request's query string.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request.
        '''
        if params is None:
            params = prepare_payload(locals())
        return self.session.get(f'{self.api_url}/get_organization_id',
                                params=params,
                                headers=headers)
