

from abc import ABCMeta, abstractmethod
import requests
import typing

from utils.helpers import prepare_payload


class CustomerWebApi:
    ''' Main class that allows specific client retrieval. '''

    @staticmethod
    def get_api_client(token: str, version: str, env: str = 'production'):
        ''' Returns client for specific API version. 

            Args:
                token (str): Full token with type (Bearer/Basic) that will be
                                used as `Authorization` header in requests to API.
                version (str): API's version.
                env (str): API's environment.

            Returns:
                API client object for specified version based on
                `CustomerWebApiInterface`.

            Raises:
                ValueError: If the specified version does not exist.
        '''
        versions = {
            '3.3': Version33(token, version, env)
        }
        client = versions.get(version)
        if not client:
            raise ValueError('Provided version does not exist.')
        return client


class CustomerWebApiInterface(metaclass=ABCMeta):
    ''' Abstract interface class. '''

    def __init__(self, token: str, version: str, env: str = 'production'):
        env = f'{env}.' if env in ['labs', 'staging'] else ''
        self.api_url = f'https://api.{env}livechatinc.com/v{version}/customer/action'
        self.session = requests.Session()
        self.session.headers.update({'Authorization': token})

# Chats

    def list_chats(self, payload: dict = None, limit: int = None, sort_order: str = None, page_id: str = None) -> requests.Response:
        ''' Returns summaries of the chats a Customer participated in.

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                limit (int): Limit of results per page. Default: 10, maximum: 25.
                sort_order (str): Possible values: asc, desc (default). 
                                  Chat summaries are sorted by the creation date of its last thread.
                page_id (str): ID of the page with paginated results.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/list_chats', json=payload)

    def list_threads(self, payload: dict = None, chat_id: str = None, sort_order: str = None, page_id: str = None, min_events_count: int = None) -> requests.Response:
        ''' Returns threads that the current Customer has access to in a given chat.

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                chat_id (str): ID of the chat for which threads are to be listed.
                limit (str): Limit of results per page. Default: 10, maximum: 25.
                sort_order (str): Possible values: asc, desc (default). 
                                  Chat summaries are sorted by the creation date of its last thread.
                page_id (str): ID of the page with paginated results.
                min_events_count (int): Range: 1-100; 
                    Specifies the minimum number of events to be returned in the response. 

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/list_threads', json=payload)

    def get_chat(self, payload: dict = None, chat_id: str = None, thread_id: str = None) -> requests.Response:
        ''' Returns a thread that the current Customer has access to in a given chat. 

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                chat_id (str): ID of the chat for which thread is to be returned.
                thread_id (str): ID of the thread to show. Default: the latest thread (if exists)

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/get_chat', json=payload)

    def start_chat(self, payload: dict = None, chat: dict = None, active: bool = None, continuous: bool = None) -> requests.Response:
        ''' Starts a chat.

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                chat (dict): Dict containing chat properties, access and thread.
                active (bool): When set to False, creates an inactive thread; default: True.
                continuous (bool): Starts chat as continuous (online group is not required); default: False.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/start_chat', json=payload)

    def resume_chat(self, payload: dict = None, chat: dict = None, active: bool = None, continuous: bool = None) -> requests.Response:
        ''' Restarts an archived chat.

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                chat (dict): Dict containing chat properties, access and thread.
                active (bool): When set to False, creates an inactive thread; default: True.
                continuous (bool): Starts chat as continuous (online group is not required); default: False.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/resume_chat', json=payload)

    def deactivate_chat(self, payload: dict = None, id: str = None) -> requests.Response:
        ''' Deactivates a chat by closing the currently open thread.
            Sending messages to this thread will no longer be possible.

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                id (str): ID of chat to be deactivated.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/deactivate_chat', json=payload)

# Configuration

    def get_dynamic_configuration(self, payload: dict = None, group_id: int = None, url: str = None, channel_type: str = None, test: bool = None) -> requests.Response:
        ''' Returns the dynamic configuration of a given group.
            It provides data to call Get Configuration and Get Localization. 

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                group_id (int): The ID of the group that you want to get a dynamic configuration for. ID of the default group is used if not provided.
                url (str): The URL that you want to get a dynamic configuration for.
                channel_type (str): The channel type that you want to get a dynamic configuration for.
                test (bool): Treats a dynamic configuration request as a test.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
           '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/get_dynamic_configuration', json=payload)

    def get_configuration(self, payload: dict = None, group_id: int = None, version: str = None) -> requests.Response:
        ''' Returns the configuration of a given group in a given version. Contains data based on which the Chat Widget can be built.

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                group_id (int): The ID of the group that you want to get a configuration for.
                version (str): The version that you want to get a configuration for. 
                               Returned from Get Dynamic Configuration as the config_version parameter.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
         '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/get_configuration', json=payload)

# Events

    def send_event(self, payload: dict = None, chat_id: str = None, event: dict = None, attach_to_last_thread: bool = None) -> requests.Response:
        ''' Sends an Event object. Use this method to send a message by specifying the Message event type in the request.
            The method updates the requester's `events_seen_up_to` as if they've seen all chat events.

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                chat_id (int): ID of the chat that you to send a message to.
                event (dict): The event object.
                attach_to_last_thread (bool): The flag is ignored for active chats. 
                                              For inactive chats:
                                              True – the event will be added to the last thread;
                                              False – the request will fail. Default: False.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/send_event', json=payload)

    def upload_file(self, payload: dict = None, file: typing.BinaryIO = None) -> requests.Response:
        ''' Uploads a file to the server as a temporary file. It returns a URL that expires after 24 hours unless the URL is used in `send_event`.

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                file (typing.BinaryIO): File-like object with file to upload (Maximum size: 10MB).

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/upload_file', json=payload)

    def send_rich_message_postback(self, payload: dict = None, chat_id: str = None, event_id: str = None, postback: dict = None, thread_id: str = None) -> requests.Response:
        ''' Sends a rich message postback. 

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                chat_id (str): ID of the chat to send rich message postback to.
                event_id (str): ID of the event related to the rich message postback.
                postback (dict): Object containing postback data (id, toggled).
                thread_id (str): ID of the thread to send rich message postback to.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/send_rich_message_postback', json=payload)

    def send_sneak_peek(self, payload: dict = None, chat_id: str = None, sneak_peek_text: str = None) -> requests.Response:
        ''' Sends a sneak peek to a chat. 

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                chat_id (str): ID of the chat to send a sneak peek to.
                sneak_peek_text (str): Sneak peek text.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/send_sneak_peek', json=payload)

# Localization

    def get_localization(self, payload: dict = None, group_id: int = None, language: str = None, version: str = None) -> requests.Response:
        ''' Returns the localization of a given language and group in a given version. Contains translated phrases for the Chat Widget.

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                group_id (int): ID of the group that you want to get a localization for.
                language (str): The language that you want to get a localization for.
                version (str): The version that you want to get a localization for. 
                               Returned from `get_dynamic_configuration` as the `localization_version` parameter.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/get_localization', json=payload)

# Properties

    def update_chat_properties(self, payload: dict = None, id: str = None, properties: dict = None) -> requests.Response:
        ''' Updates chat properties.

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                id (str): ID of the chat you to set a property for.
                properties (dict): Chat properties to set. 
                                   You should stick to the general properties format and include namespace, property name and value.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/update_chat_properties', json=payload)

    def delete_chat_properties(self, payload: dict = None, id: str = None, properties: dict = None) -> requests.Response:
        ''' Deletes chat properties.

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                id (str): ID of the chat you want to delete properties of.
                properties (dict): Chat properties to delete.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/delete_chat_properties', json=payload)

    def update_thread_properties(self, payload: dict = None, chat_id: str = None, thread_id: str = None, properties: dict = None) -> requests.Response:
        ''' Updates chat thread properties.

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                chat_id (str): ID of the chat you to set properties for.
                thread_id (str): ID of the thread you want to set properties for.
                properties (dict): Thread properties to set. 
                                   You should stick to the general properties format and include namespace, property name and value.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/update_thread_properties', json=payload)

    def delete_thread_properties(self, payload: dict = None, chat_id: str = None, thread_id: str = None, properties: dict = None) -> requests.Response:
        ''' Deletes chat thread properties.

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                chat_id (str): ID of the chat you want to delete the properties of.
                thread_id (str): ID of the thread you want to delete the properties of.
                properties (dict): Thread properties to delete.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/delete_thread_properties', json=payload)

    def update_event_properties(self, payload: dict = None, chat_id: str = None, thread_id: str = None, event_id: str = None, properties: dict = None) -> requests.Response:
        ''' Updates event properties.

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                chat_id (str): ID of the chat you to set properties for.
                thread_id (str): ID of the thread you want to set properties for.
                event_id (str): ID of the event you want to set properties for.
                properties (dict): Thread properties to set. 
                                   You should stick to the general properties format and include namespace, property name and value.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/update_event_properties', json=payload)

    def delete_event_properties(self, payload: dict = None, chat_id: str = None, thread_id: str = None, event_id: str = None, properties: dict = None) -> requests.Response:
        ''' Deletes event properties.

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                chat_id (str): ID of the chat you to delete the properties for.
                thread_id (str): ID of the thread you want to delete the properties for.
                event_id (str): ID of the event you want to delete the properties for.
                properties (dict): Event properties to delete. 

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/delete_event_properties', json=payload)

    def list_license_properties(self, payload: dict = None, namespace: str = None, name: str = None) -> requests.Response:
        ''' Returns the properties of a given license. It only returns the properties a Customer has access to. 

            Args:
                payload (dict): Custom payload to be used as request's data.
                namespace (str): Property namespace to retrieve.
                name (str): Property name.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = {}
        params = {}
        if namespace:
            params['namespace'] = namespace
        if name:
            params['name'] = name
        return self.session.post(f'{self.api_url}/list_license_properties', json=payload, params=params)

    def list_group_properties(self, payload: dict = None, group_id: int = None, namespace: str = None, name: str = None) -> requests.Response:
        ''' Returns the properties of a given group. It only returns the properties a Customer has access to. 
            Args:
                payload (dict): Custom payload to be used as request's data.
                group_id (int): ID of the group you want to return the properties of.
                namespace (str): Property namespace to retrieve.
                name (str): Property name.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = {}
        params = {}
        if namespace:
            params['namespace'] = namespace
        if name:
            params['name'] = name
        if group_id:
            params['id'] = group_id
        return self.session.post(f'{self.api_url}/list_group_properties', json=payload, params=params)

# Customers

    def get_customer(self, payload: dict = None) -> requests.Response:
        ''' Returns the info about the Customer requesting it.  

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. 
        '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/get_customer', json=payload)

    def update_customer(self, payload: dict = None, name: str = None, email: str = None, avatar: str = None, session_fields: list = None) -> requests.Response:
        ''' Updates Customer's properties. 

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                name (str): Name of the customer.
                email (str): Email of the customer.
                avatar (str): The URL of the Customer's avatar.
                session_fields (list): An array of custom object-enclosed key:value pairs. 
                                       Respects the order of items.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. 
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/update_customer', json=payload)

    def set_customer_session_fields(self, payload: dict = None, session_fields: list = None) -> requests.Response:
        ''' Updates Customer's session fields. 

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                session_fields (list): An array of custom object-enclosed key:value pairs. 
                                       Respects the order of items. Max keys: 100.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. 
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/set_customer_session_fields', json=payload)

# Status

    def list_group_statuses(self, payload: dict = None, all: bool = None, group_ids: list = None) -> requests.Response:
        ''' Returns object with info about current routing statuses of agent groups.
            One of the optional parameters needs to be included in the request.

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                all (bool): If set to True, you will get statuses of all the groups.
                group_ids (list): A table of groups' IDs

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.  
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/list_group_statuses', json=payload)

# Other

    def check_goals(self, payload: dict = None, session_fields: list = None, group_id: int = None, page_url: str = None) -> requests.Response:
        ''' Customer can use this method to trigger checking if goals were achieved.
            Then, Agents receive the information. You should call this method to provide goals parameters for the server
            when the customers limit is reached. Works only for offline Customers. 

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                session_fields (list): An array of custom object-enclosed key:value pairs.
                group_id (int): Group ID to check the goals for.
                page_url (str): URL of the page to check the goals for.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.   
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/check_goals', json=payload)

    def get_form(self, payload: dict = None, group_id: int = None, type: str = None) -> requests.Response:
        ''' Returns an empty ticket form of a prechat or postchat survey.

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                group_id (int): ID of the group from which you want the form.
                type (str): Form type; possible values: prechat or postchat.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.   
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/get_form', json=payload)

    def get_predicted_agent(self, payload: dict = None) -> requests.Response:
        ''' Gets the predicted Agent - the one the Customer will chat with when the chat starts.
            To use this method, the Customer needs to be logged in, which can be done via the `login` method.

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. 
        '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/get_predicted_agent', json=payload)

    def get_url_info(self, payload: dict = None, url: str = None) -> requests.Response:
        ''' Returns the info on a given URL. 

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                url (str): Valid website URL.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/get_url_info', json=payload)

    def mark_events_as_seen(self, payload: dict = None, chat_id: str = None, seen_up_to: str = None) -> requests.Response:
        ''' Updates `seen_up_to` value for a given chat. 

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                chat_id (str): ID of the chat to update `seen_up_to`.
                seen_up_to (str): RFC 3339 date-time format.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/mark_events_as_seen', json=payload)

    def accept_greeting(self, payload: dict = None, greeting_id: int = None, unique_id: str = None) -> requests.Response:
        ''' Marks an incoming greeting as seen.

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                greeting_id (int): ID of the greeting configured within the license to accept.
                unique_id (str): ID of the greeting to accept. You can get it from the `incoming_greeting` push.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/accept_greeting', json=payload)

    def cancel_greeting(self, payload: dict = None, unique_id: str = None) -> requests.Response:
        ''' Cancels a greeting (an invitation to the chat). 
            For example, Customers could cancel greetings by minimalizing the chat widget with a greeting.

            Args:
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                unique_id (str): ID of the greeting to cancel. You can get it from the `incoming_greeting` push.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/cancel_greeting', json=payload)


class Version33(CustomerWebApiInterface):
    pass
