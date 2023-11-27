''' Module containing Agent RTM API client implementation for v3.4. '''

from typing import Any, Optional

from livechat.utils.helpers import prepare_payload
from livechat.utils.structures import RtmResponse
from livechat.utils.ws_client import WebsocketClient

# pylint: disable=unused-argument, too-many-arguments, invalid-name, redefined-builtin


class AgentRtmV34:
    ''' Agent RTM API Class containing methods in version 3.4. '''
    def __init__(self, url: str):
        self.ws = WebsocketClient(url=f'wss://{url}/v3.4/agent/rtm/ws')

    def open_connection(self) -> None:
        ''' Opens WebSocket connection. '''
        self.ws.open()

    def close_connection(self) -> None:
        ''' Closes WebSocket connection. '''
        self.ws.close()

    # Chats

    def list_chats(self,
                   filters: dict = None,
                   sort_order: str = None,
                   limit: int = None,
                   page_id: str = None,
                   payload: dict = None) -> RtmResponse:
        ''' Returns summaries of the chats an Agent has access to.

            Args:
                filters (dict): Possible request filters. Mustn't change between requests for subsequent pages.
                        Otherwise, the behavior is undefined.
                sort_order (str): Possible values: asc, desc (default). Chat summaries are sorted by the
                        creation date of its last thread.
                limit (int): Chats limit per page. Default: 10, maximum: 100.
                page_id (str): Page ID.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'list_chats', 'payload': payload})

    def list_threads(self,
                     chat_id: str = None,
                     sort_order: str = None,
                     limit: int = None,
                     page_id: str = None,
                     min_events_count: int = None,
                     filters: dict = None,
                     payload: dict = None) -> RtmResponse:
        ''' Returns threads that the current Agent has access to in a given chat.

            Args:
                chat_id (str): Chat ID to get threads from.
                sort_order (str): Possible values: asc - oldest threads first and desc -
                        newest threads first (default).
                limit (int): Default: 3, maximum: 100.
                page_id (str): Page ID.
                min_events_count (int): Range: 1-100; Specifies the minimum number of
                        events to be returned in the response.
                filters (dict): Filters object.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'list_threads', 'payload': payload})

    def get_chat(self,
                 chat_id: str = None,
                 thread_id: str = None,
                 payload: dict = None) -> RtmResponse:
        ''' Returns a thread that the current Agent has access to in a given chat.

            Args:
                chat_id (str): ID of a chat to get.
                thread_id (str): Thread ID to get. Default: the latest thread (if exists).
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'get_chat', 'payload': payload})

    def list_archives(self,
                      filters: dict = None,
                      page_id: str = None,
                      sort_order: str = None,
                      limit: int = None,
                      highlights: dict = None,
                      payload: dict = None) -> RtmResponse:
        ''' Returns a list of the chats an Agent has access to.

            Args:
                filters (dict): Filters object.
                page_id (str): Page ID.
                sort_order (str): Possible values: asc - oldest threads first and desc -
                        newest threads first (default).
                limit (int): Default: 10, minimum: 1, maximum: 100.
                highlights (dict): Use it to highlight the match of filters.query.
                        To enable highlights with default parameters, pass an empty object.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'list_archives', 'payload': payload})

    def start_chat(self,
                   chat: dict = None,
                   active: bool = None,
                   continuous: bool = None,
                   payload: dict = None) -> RtmResponse:
        ''' Starts a chat.

            Args:
                chat (dict): Chat object.
                active (bool): When set to False, creates an inactive thread; default: True.
                continuous (bool): Starts chat as continuous (online group is not required); default: False.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'start_chat', 'payload': payload})

    def resume_chat(self,
                    chat: dict = None,
                    active: bool = None,
                    continuous: bool = None,
                    payload: dict = None) -> RtmResponse:
        ''' Restarts an archived chat.

            Args:
                chat (dict): Chat object.
                active (bool): When set to False, creates an inactive thread; default: True.
                continuous (bool): Sets a chat to the continuous mode. When unset, leaves the mode unchanged.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'resume_chat', 'payload': payload})

    def deactivate_chat(self,
                        id: str = None,
                        ignore_requester_presence: bool = None,
                        payload: dict = None) -> RtmResponse:
        ''' Deactivates a chat by closing the currently open thread.

            Args:
                id (str): Chat ID to deactivate.
                ignore_requester_presence (bool): If `True`, allows requester to deactivate chat
                                                  without being present in the chat's users list.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'deactivate_chat', 'payload': payload})

    def follow_chat(self, id: str = None, payload: dict = None) -> RtmResponse:
        ''' Marks a chat as followed.

            Args:
                id (str): Chat ID to follow.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'follow_chat', 'payload': payload})

    def unfollow_chat(self,
                      id: str = None,
                      payload: dict = None) -> RtmResponse:
        ''' Removes the requester from the chat followers.

            Args:
                id (str): Chat ID to unfollow.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'unfollow_chat', 'payload': payload})

# Chat access

    def transfer_chat(self,
                      id: str = None,
                      target: dict = None,
                      ignore_agents_availability: bool = None,
                      ignore_requester_presence: bool = None,
                      payload: dict = None) -> RtmResponse:
        ''' Transfers a chat to an agent or a group.

            Args:
                id (str): Chat ID.
                target (dict): Target object. If missing, the chat will be
                        transferred within the current group.
                ignore_agents_availability (bool): If `True`, always transfers chats. Otherwise, fails
                              when unable to assign any agent from the requested groups.
                ignore_requester_presence (bool): If `True`, allows requester to transfer chat
                                                  without being present in the chat's users list.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'transfer_chat', 'payload': payload})

# Chat users

    def add_user_to_chat(self,
                         chat_id: str = None,
                         user_id: str = None,
                         user_type: str = None,
                         visibility: str = None,
                         ignore_requester_presence: bool = None,
                         payload: dict = None) -> RtmResponse:
        ''' Adds a user to the chat. You can't add more than
            one customer user type to the chat.

            Args:
                chat_id (str): Chat ID.
                user_id (str): ID of the user that will be added to the chat.
                user_type (str): Possible values: agent or customer.
                visibility (str): Determines the visibility of events sent by
                                  the agent. Possible values: `all` or `agents`.
                ignore_requester_presence (bool): If `True`, allows requester to add user to chat
                                                  without being present in the chat's users list.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for
                                the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'add_user_to_chat', 'payload': payload})

    def remove_user_from_chat(self,
                              chat_id: str = None,
                              user_id: str = None,
                              user_type: str = None,
                              ignore_requester_presence: bool = None,
                              payload: dict = None) -> RtmResponse:
        ''' Removes a user from chat.

            Args:
                chat_id (str): Chat ID.
                user_id (str): ID of the user that will be added to the chat.
                user_type (str): Possible values: agent or customer.
                ignore_requester_presence (bool): If `True`, allows requester to remove user from chat
                                                  without being present in the chat's users list.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({
            'action': 'remove_user_from_chat',
            'payload': payload
        })

# Events

    def send_event(self,
                   chat_id: str = None,
                   event: dict = None,
                   attach_to_last_thread: bool = None,
                   author_id: Optional[str] = None,
                   payload: dict = None) -> RtmResponse:
        ''' Sends an Event object.

            Args:
                chat_id (str): ID of the chat you want to send the message to.
                event (dict): Event object.
                attach_to_last_thread (bool): Flag which states if event object should be added to last thread.
                        The flag is ignored for active chats.
                author_id (optional str): Provide if the event should be sent on behalf of a bot.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        opts = {}
        if author_id:
            opts['author_id'] = author_id
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'send_event', 'payload': payload, **opts})

    def send_rich_message_postback(self,
                                   chat_id: str = None,
                                   thread_id: str = None,
                                   event_id: str = None,
                                   postback: dict = None,
                                   payload: dict = None) -> RtmResponse:
        ''' Sends rich message postback.

            Args:
                chat_id (str): ID of the chat to send a rich message to.
                thread_id (str): ID of the thread.
                event_id (str): ID of the event.
                postback (dict): Postback object.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({
            'action': 'send_rich_message_postback',
            'payload': payload
        })

# Properties

    def update_chat_properties(self,
                               id: str = None,
                               properties: dict = None,
                               payload: dict = None) -> RtmResponse:
        ''' Updates chat properties.

            Args:
                id (str): ID of the chat you to set a property for.
                properties (dict): Chat properties to set.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({
            'action': 'update_chat_properties',
            'payload': payload
        })

    def delete_chat_properties(self,
                               id: str = None,
                               properties: dict = None,
                               payload: dict = None) -> RtmResponse:
        ''' Deletes chat properties.

            Args:
                id (str): ID of the chat you want to delete properties of.
                properties (dict): Chat properties to delete.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({
            'action': 'delete_chat_properties',
            'payload': payload
        })

    def update_thread_properties(self,
                                 chat_id: str = None,
                                 thread_id: str = None,
                                 properties: dict = None,
                                 payload: dict = None) -> RtmResponse:
        ''' Updates thread properties.

            Args:
                chat_id (str): ID of the chat you want to set properties for.
                thread_id (str): ID of the thread you want to set properties for.
                properties (dict): Chat properties to set.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({
            'action': 'update_thread_properties',
            'payload': payload
        })

    def delete_thread_properties(self,
                                 chat_id: str = None,
                                 thread_id: str = None,
                                 properties: dict = None,
                                 payload: dict = None) -> RtmResponse:
        ''' Deletes thread properties.

            Args:
                chat_id (str): ID of the chat you want to delete the properties of.
                thread_id (str): ID of the thread you want to delete the properties of.
                properties (dict): Thread properties to delete.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({
            'action': 'delete_thread_properties',
            'payload': payload
        })

    def update_event_properties(self,
                                chat_id: str = None,
                                thread_id: str = None,
                                event_id: str = None,
                                properties: dict = None,
                                payload: dict = None) -> RtmResponse:
        ''' Updates event properties.

            Args:
                chat_id (str): ID of the chat you want to set properties for.
                thread_id (str): ID of the thread you want to set properties for.
                event_id (str): ID of the event you want to set properties for.
                properties (dict): Chat properties to set.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({
            'action': 'update_event_properties',
            'payload': payload
        })

    def delete_event_properties(self,
                                chat_id: str = None,
                                thread_id: str = None,
                                event_id: str = None,
                                properties: dict = None,
                                payload: dict = None) -> RtmResponse:
        ''' Deletes event properties.

            Args:
                chat_id (str): ID of the chat you want to delete the properties of.
                thread_id (str): ID of the thread you want to delete the properties of.
                event_id (str): ID of the event you want to delete the properties of.
                properties (dict): Event properties to delete.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({
            'action': 'delete_event_properties',
            'payload': payload
        })

# Thread tags

    def tag_thread(self,
                   chat_id: str = None,
                   thread_id: str = None,
                   tag: str = None,
                   payload: dict = None) -> RtmResponse:
        ''' Tags thread.

            Args:
                chat_id (str): ID of the chat you want to add a tag to.
                thread_id (str): ID of the thread you want to add a tag to.
                tag (str): Tag name.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'tag_thread', 'payload': payload})

    def untag_thread(self,
                     chat_id: str = None,
                     thread_id: str = None,
                     tag: str = None,
                     payload: dict = None) -> RtmResponse:
        ''' Untags thread.

            Args:
                chat_id (str): ID of the chat you want to remove a tag from.
                thread_id (str): ID of the thread you want to remove a tag from.
                tag (str): Tag name.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'untag_thread', 'payload': payload})

# Customers

    def get_customer(self,
                     id: str = None,
                     payload: dict = None) -> RtmResponse:
        ''' Returns the info about the Customer with a given ID.

            Args:
                id (str): ID of the Customer.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'get_customer', 'payload': payload})

    def list_customers(self,
                       page_id: str = None,
                       limit: int = None,
                       sort_order: str = None,
                       sort_by: str = None,
                       filters: dict = None,
                       payload: dict = None) -> RtmResponse:
        ''' Returns the list of Customers.

            Args:
                page_id (str): Page ID.
                limit (int): Customers limit. Default: 10, maximum: 100.
                sort_order (str): Possible values: asc, desc (default). Customers are sorted
                        by the creation date.
                sort_by (str): Possible values: created_at (default), threads_count, visits_count,
                        agent_last_event or customer_last_event.
                filters (dict): Filters object.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'list_customers', 'payload': payload})

    def create_customer(self,
                        name: str = None,
                        email: str = None,
                        avatar: str = None,
                        session_fields: list = None,
                        payload: dict = None) -> RtmResponse:
        ''' Creates a new Customer user type.

            Args:
                name (str): Customer's name.
                email (str): Customer's email.
                avatar (str): URL of the Customer's avatar.
                session_fields (list): An array of custom object-enclosed key:value pairs.
                        Respects the order of items.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'create_customer', 'payload': payload})

    def update_customer(self,
                        id: str = None,
                        name: str = None,
                        email: str = None,
                        avatar: str = None,
                        session_fields: list = None,
                        payload: dict = None) -> RtmResponse:
        ''' Updates Customer's properties.

            Args:
                id (str): ID of the Customer. UUID v4 format is required.
                name (str): Customer's name.
                email (str): Customer's email.
                avatar (str): URL of the Customer's avatar.
                session_fields (list): An array of custom object-enclosed key:value pairs.
                        Respects the order of items.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'update_customer', 'payload': payload})

    def ban_customer(self,
                     id: str = None,
                     ban: dict = None,
                     payload: dict = None) -> RtmResponse:
        ''' Bans the customer for a specific period of time.

            Args:
                id (str): ID of the Customer. UUID v4 format is required.
                ban (dict): Ban object containing the number of days that
                        the Customer will be banned.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'ban_customer', 'payload': payload})

    def follow_customer(self,
                        id: str = None,
                        payload: dict = None) -> RtmResponse:
        ''' Marks a customer as followed.

            Args:
                id (str): ID of the Customer. UUID v4 format is required.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'follow_customer', 'payload': payload})

    def unfollow_customer(self,
                          id: str = None,
                          payload: dict = None) -> RtmResponse:
        ''' Removes the agent from the list of customer's followers.

            Args:
                id (str): ID of the Customer. UUID v4 format is required.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({
            'action': 'unfollow_customer',
            'payload': payload
        })

# Status

    def login(self,
              token: str = None,
              timezone: str = None,
              reconnect: bool = None,
              push_notifications: dict = None,
              application: dict = None,
              away: bool = None,
              customer_monitoring_level: str = None,
              pushes: dict = None,
              payload: dict = None) -> RtmResponse:
        ''' Logs in agent.

            Args:
                token (str): OAuth token from the Agent's account.
                timezone (str): Agent's timezone.
                reconnect (bool): Reconnecting sets the status to the
                        last known state instead of the default one.
                push_notifications (dict): Push notifications for the requested token.
                application (dict): Object containing information related to
                        the application's name and version.
                away (bool): When True, the connection is set to the away state.
                        Defaults to False.
                customer_monitoring_level (str): Possible values are: `my`, `chatting`, `invited`, `online` and `highest_available`.
                        Defaults to my if login creates the first session;
                        otherwise it preserves the current customer_monitoring_level.
                pushes (dict): Use case: when you want to receive only specific pushes.
                By default, it's set to all for the version of your currently established RTM connection.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'login', 'payload': payload})

    def change_push_notifications(self,
                                  firebase_token: str = None,
                                  platform: str = None,
                                  enabled: bool = None,
                                  payload: dict = None) -> RtmResponse:
        ''' Changes the firebase push notifications properties.

            Args:
                firebase_token (str): Firebase device token.
                platform (str): OS platform. Possible values: ios, android.
                enabled (bool): Enable or disable push notifications for the requested token.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({
            'action': 'change_push_notifications',
            'payload': payload
        })

    def set_routing_status(self,
                           status: str = None,
                           agent_id: str = None,
                           payload: dict = None) -> RtmResponse:
        ''' Changes the status of an Agent or a Bot Agent.

            Args:
                status (str): For Agents: accepting_chats or not_accepting_chats.
                        For Bot Agents: accepting_chats, not_accepting_chats, or offline.
                agent_id (str): If not specified, the requester's status will be updated.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({
            'action': 'set_routing_status',
            'payload': payload
        })

    def set_away_status(self,
                        away: bool = None,
                        payload: dict = None) -> RtmResponse:
        ''' Sets an Agent's connection to the away state.

            Args:
                away (bool): A flag.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'set_away_status', 'payload': payload})

    def logout(self, payload: dict = None) -> RtmResponse:
        ''' Logs out agent.

            Args:
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        return self.ws.send({
            'action': 'logout',
            'payload': {} if payload is None else payload
        })

    def list_routing_statuses(self,
                              filters: dict = None,
                              payload: dict = None) -> RtmResponse:
        ''' Returns the current routing status of each agent selected by the provided filters.

            Args:
                filters (dict): Filters object.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({
            'action': 'list_routing_statuses',
            'payload': payload
        })


# Other

    def mark_events_as_seen(self,
                            chat_id: str = None,
                            seen_up_to: str = None,
                            payload: dict = None) -> RtmResponse:
        ''' Marks events as seen by agent.

            Args:
                chat_id (str): Chat to mark events.
                seen_up_to (str): Date up to which mark events - RFC 3339 date-time format.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({
            'action': 'mark_events_as_seen',
            'payload': payload
        })

    def send_typing_indicator(self,
                              chat_id: str = None,
                              visibility: str = None,
                              is_typing: bool = None,
                              payload: dict = None) -> RtmResponse:
        ''' Sends a typing indicator.

            Args:
                chat_id (str): ID of the chat you want to send the typing indicator to.
                visibility (str): Possible values: `all`, `agents`.
                is_typing (bool): A flag that indicates if you are typing.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({
            'action': 'send_typing_indicator',
            'payload': payload
        })

    def multicast(self,
                  recipients: dict = None,
                  content: Any = None,
                  type: str = None,
                  payload: dict = None) -> RtmResponse:
        ''' Sends a multicast (chat-unrelated communication).

            Args:
                recipients (object): Object containing filters related to multicast recipients.
                content (typing.Any): A JSON message to be sent.
                type (str): Multicast message type.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'multicast', 'payload': payload})

    def list_agents_for_transfer(self,
                                 chat_id: str = None,
                                 payload: dict = None) -> RtmResponse:
        ''' Returns the list of Agents you can transfer a chat to.

            Args:
                chat_id (str): ID of the chat you want to transfer.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({
            'action': 'list_agents_for_transfer',
            'payload': payload
        })
