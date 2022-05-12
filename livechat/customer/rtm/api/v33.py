''' Customer RTM API module with client class in version 3.3. '''

# pylint: disable=C0103,R0903,R0913,W0107,W0231,W0613,W0622

from livechat.utils.helpers import prepare_payload
from livechat.utils.structures import RtmResponse
from livechat.utils.ws_client import WebsocketClient


class CustomerRtmV33:
    ''' Customer RTM API client class in version 3.3. '''
    def __init__(self, license_id: str, base_url: str):
        if isinstance(license_id, (int, str)):
            self.ws = WebsocketClient(
                url=
                f'wss://{base_url}/v3.3/customer/rtm/ws?license_id={license_id}'
            )
        else:
            raise ValueError(
                f'Provided `license_id` (`{license_id}`) seems invalid. Websocket connection may not open.'
            )

    def open_connection(self, origin: dict = None) -> None:
        ''' Opens WebSocket connection.
            Args:
                origin (dict): Specifies origin while creating websocket connection.
        '''
        if origin:
            self.ws.open(origin=origin)
        else:
            self.ws.open()

    def close_connection(self) -> None:
        ''' Closes WebSocket connection. '''
        self.ws.close()

# Chats

    def list_chats(self,
                   limit: int = None,
                   sort_order: str = None,
                   page_id: str = None,
                   payload: dict = None) -> RtmResponse:
        ''' It returns summaries of the chats a Customer participated in.

            Args:
                limit (int): Chat limit. Default: 10, maximum: 25.
                sort_order (str): Possible values: asc, desc (default). Chat summaries are sorted by the
                        creation date of its last thread.
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
                     payload: dict = None) -> RtmResponse:
        ''' It returns threads that the current Customer has access to in a given chat.

            Args:
                chat_id (str): Chat ID to get threads from.
                sort_order (str): Possible values: asc - oldest threads first and desc
                        newest threads first (default).
                limit (int): Default: 3, maximum: 100.
                page_id (str): Page ID.
                min_events_count (int):Range: 1-100; Specifies the minimum number of
                        events to be returned in the response.
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
        ''' It returns a thread that the current Customer has access to in a given chat.

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
                active (bool): When set to false, creates an inactive thread; default: true.
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
                        payload: dict = None) -> RtmResponse:
        ''' Deactivates a chat by closing the currently open thread.

            Args:
                id (str): Chat ID to deactivate.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'deactivate_chat', 'payload': payload})

# Events

    def send_event(self,
                   chat_id: str = None,
                   event: dict = None,
                   attach_to_last_thread: bool = None,
                   payload: dict = None) -> RtmResponse:
        ''' Sends an Event object.

            Args:
                chat_id (str): ID of the chat you want to send the message to.
                event (dict): Event object.
                attach_to_last_thread (bool): Flag which states if event object should be added to last thread.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'send_event', 'payload': payload})

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

    def send_sneak_peek(self,
                        chat_id: str = None,
                        sneak_peek_text: str = None,
                        payload: dict = None) -> RtmResponse:
        ''' Sends a sneak peek to a chat.

            Args:
                chat_id (str): ID of the chat to send a sneak peek to.
                sneak_peek_text (str): Sneak peek text.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'send_sneak_peek', 'payload': payload})

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

# Customers

    def update_customer(self,
                        name: str = None,
                        email: str = None,
                        avatar: str = None,
                        session_fields: list = None,
                        payload: dict = None) -> RtmResponse:
        ''' Updates customer's properties.

            Args:
                name (str): Customer`s name.
                email (str): Customer`s email.
                avatar (str): Customer`s avatar.
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

    def update_customer_page(self,
                             url: str = None,
                             title: str = None,
                             payload: dict = None) -> RtmResponse:
        ''' Updates customer's page.

            Args:
                url (str): Customer`s url.
                title (str): Customer`s page title.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({
            'action': 'update_customer_page',
            'payload': payload
        })

    def set_customer_session_fields(self,
                                    session_fields: list = None,
                                    payload: dict = None) -> RtmResponse:
        ''' Sets customer's session fields.

            Args:
                session_fields (list): List of custom object-enclosed key:value pairs.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({
            'action': 'set_customer_session_fields',
            'payload': payload
        })

    def get_customer(self, payload: dict = None) -> RtmResponse:
        ''' Returns the info about the customer requesting it.

            Args:
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        return self.ws.send({
            'action': 'get_customer',
            'payload': {} if payload is None else payload
        })

# Status

    def login(self, token: str = None, payload: dict = None) -> RtmResponse:
        ''' Logs in customer.

            Args:
                token (str) : OAuth token from the Customer's account.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'login', 'payload': payload})

    def list_group_statuses(self,
                            all: bool = None,
                            group_ids: list = None,
                            payload: dict = None) -> RtmResponse:
        ''' Lists statuses of groups.

            Args:
                all (bool): If set to True, you will get statuses of all the groups.
                group_ids (list): A table of a groups' IDs.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({
            'action': 'list_group_statuses',
            'payload': payload
        })


# Other

    def get_form(self,
                 group_id: int = None,
                 type: str = None,
                 payload: dict = None) -> RtmResponse:
        ''' Returns an empty ticket form of a prechat or postchat survey.

            Args:
                group_id (int): ID of the group from which you want the form.
                type (str): Form type. Possible values: prechat or postchat.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'get_form', 'payload': payload})

    def get_predicted_agent(self, payload: dict = None) -> RtmResponse:
        ''' Gets the predicted Agent - the one the Customer will chat with when the chat starts.

            Args:
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        return self.ws.send({
            'action': 'get_predicted_agent',
            'payload': {} if payload is None else payload
        })

    def get_url_info(self,
                     url: str = None,
                     payload: dict = None) -> RtmResponse:
        ''' It returns the info on a given URL.

            Args:
                url (str): URL to get info about.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'get_url_info', 'payload': payload})

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

    def accept_greeting(self,
                        greeting_id: int = None,
                        unique_id: str = None,
                        payload: dict = None) -> RtmResponse:
        ''' Marks an incoming greeting as seen.

            Args:
                greeting_id (int): Number representing type of a greeting.
                unique_id (str): Specific greeting event ID.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'accept_greeting', 'payload': payload})

    def cancel_greeting(self,
                        unique_id: str = None,
                        payload: dict = None) -> RtmResponse:
        ''' Cancels a greeting.

            Args:
                unique_id (str): Specific greeting event ID.
                payload (dict): Custom payload to be used as request's data.
                        It overrides all other parameters provided for the method.

            Returns:
                RtmResponse: RTM response structure (`request_id`, `action`,
                             `type`, `success` and `payload` properties)
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.ws.send({'action': 'cancel_greeting', 'payload': payload})
