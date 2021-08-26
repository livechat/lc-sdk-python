''' Customer Web client implementation. '''

# pylint: disable=W0613,R0913,W0622,C0103

import typing
from abc import ABCMeta

import httpx

from livechat.utils.helpers import prepare_payload


# pylint: disable=R0903
class CustomerWeb:
    ''' Allows retrieval of client for specific Customer Web
        API version. '''
    @staticmethod
    def get_client(license_id: int,
                   access_token: str,
                   version: str = '3.3',
                   base_url: str = 'api.livechatinc.com',
                   http2: bool = False):
        ''' Returns client for specific API version.

            Args:
                token (str): Full token with type (Bearer/Basic) that will be
                                used as `Authorization` header in requests to API.
                version (str): API's version. Defaults to `3.3`.
                base_url (str): API's base url. Defaults to `api.livechatinc.com`.
                http2 (bool): A boolean indicating if HTTP/2 support should be
                              enabled. Defaults to `False`.

            Returns:
                API client object for specified version based on
                `CustomerWebApiInterface`.

            Raises:
                ValueError: If the specified version does not exist.
        '''
        client = {
            '3.3':
            CustomerWeb33(license_id, access_token, version, base_url, http2),
            '3.4':
            CustomerWeb34(license_id, access_token, version, base_url, http2)
        }.get(version)
        if not client:
            raise ValueError('Provided version does not exist.')
        return client


class CustomerWebInterface(metaclass=ABCMeta):
    ''' Main class containing API methods. '''
    def __init__(self, license_id: int, access_token: str, version: str,
                 base_url: str, http2: bool):
        self.api_url = f'https://{base_url}/v{version}/customer/action'
        self.session = httpx.Client(http2=http2,
                                    headers={'Authorization': access_token})
        self.license_id = str(license_id)

    def modify_header(self, header: dict) -> None:
        ''' Modifies provided header in session object.

            Args:
                header (dict): Header which needs to be modified.
        '''
        self.session.headers.update(header)

    def remove_header(self, key: str) -> None:
        ''' Removes provided header from session object.

            Args:
                key (str): Key which needs to be removed from the header.
        '''
        if key in self.session.headers:
            del self.session.headers[key]

    def get_headers(self) -> dict:
        ''' Returns current header values in session object.

            Returns:
                dict: Response which presents current header values in session object.
        '''
        return dict(self.session.headers)

# Chats

    def list_chats(self,
                   limit: int = None,
                   sort_order: str = None,
                   page_id: str = None,
                   payload: dict = None,
                   headers: dict = None) -> httpx.Response:
        ''' Returns summaries of the chats a Customer participated in.

            Args:
                limit (int): Limit of results per page. Default: 10, maximum: 25.
                sort_order (str): Possible values: asc, desc (default).
                                  Chat summaries are sorted by the creation date of its last thread.
                page_id (str): ID of the page with paginated results.
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
        return self.session.post(
            f'{self.api_url}/list_chats?license_id={self.license_id}',
            json=payload,
            headers=headers)

    def list_threads(self,
                     chat_id: str = None,
                     limit: str = None,
                     sort_order: str = None,
                     page_id: str = None,
                     min_events_count: int = None,
                     payload: dict = None,
                     headers: dict = None) -> httpx.Response:
        ''' Returns threads that the current Customer has access to in a given chat.

            Args:
                chat_id (str): ID of the chat for which threads are to be listed.
                limit (str): Limit of results per page. Default: 10, maximum: 25.
                sort_order (str): Possible values: asc, desc (default).
                                  Chat summaries are sorted by the creation date of its last thread.
                page_id (str): ID of the page with paginated results.
                min_events_count (int): Range: 1-100;
                    Specifies the minimum number of events to be returned in the response.
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
        return self.session.post(
            f'{self.api_url}/list_threads?license_id={self.license_id}',
            json=payload,
            headers=headers)

    def get_chat(self,
                 chat_id: str = None,
                 thread_id: str = None,
                 payload: dict = None,
                 headers: dict = None) -> httpx.Response:
        ''' Returns a thread that the current Customer has access to in a given chat.

            Args:
                chat_id (str): ID of the chat for which thread is to be returned.
                thread_id (str): ID of the thread to show. Default: the latest thread (if exists)
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
        return self.session.post(
            f'{self.api_url}/get_chat?license_id={self.license_id}',
            json=payload,
            headers=headers)

    def start_chat(self,
                   chat: dict = None,
                   active: bool = None,
                   continuous: bool = None,
                   payload: dict = None,
                   headers: dict = None) -> httpx.Response:
        ''' Starts a chat.

            Args:
                chat (dict): Dict containing chat properties, access and thread.
                active (bool): When set to False, creates an inactive thread; default: True.
                continuous (bool): Starts chat as continuous (online group is not required); default: False.
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
        return self.session.post(
            f'{self.api_url}/start_chat?license_id={self.license_id}',
            json=payload,
            headers=headers)

    def resume_chat(self,
                    chat: dict = None,
                    active: bool = None,
                    continuous: bool = None,
                    payload: dict = None,
                    headers: dict = None) -> httpx.Response:
        ''' Restarts an archived chat.

            Args:
                chat (dict): Dict containing chat properties, access and thread.
                active (bool): When set to False, creates an inactive thread; default: True.
                continuous (bool): Starts chat as continuous (online group is not required); default: False.
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
        return self.session.post(
            f'{self.api_url}/resume_chat?license_id={self.license_id}',
            json=payload,
            headers=headers)

    def deactivate_chat(self,
                        id: str = None,
                        payload: dict = None,
                        headers: dict = None) -> httpx.Response:
        ''' Deactivates a chat by closing the currently open thread.
            Sending messages to this thread will no longer be possible.

            Args:
                id (str): ID of chat to be deactivated.
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
        return self.session.post(
            f'{self.api_url}/deactivate_chat?license_id={self.license_id}',
            json=payload,
            headers=headers)

# Configuration

    def get_dynamic_configuration(self,
                                  group_id: int = None,
                                  url: str = None,
                                  channel_type: str = None,
                                  test: bool = None,
                                  payload: dict = None,
                                  headers: dict = None) -> httpx.Response:
        ''' Returns the dynamic configuration of a given group.
            It provides data to call Get Configuration and Get Localization.

            Args:
                group_id (int): The ID of the group that you want to get a dynamic configuration for. ID of the default group is used if not provided.
                url (str): The URL that you want to get a dynamic configuration for.
                channel_type (str): The channel type that you want to get a dynamic configuration for.
                test (bool): Treats a dynamic configuration request as a test.
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
        return self.session.post(
            f'{self.api_url}/get_dynamic_configuration?license_id={self.license_id}',
            json=payload,
            headers=headers)

    def get_configuration(self,
                          group_id: int = None,
                          version: str = None,
                          payload: dict = None,
                          headers: dict = None) -> httpx.Response:
        ''' Returns the configuration of a given group in a given version. Contains data based on which the Chat Widget can be built.

            Args:
                group_id (int): The ID of the group that you want to get a configuration for.
                version (str): The version that you want to get a configuration for.
                               Returned from Get Dynamic Configuration as the config_version parameter.
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
        return self.session.post(
            f'{self.api_url}/get_configuration?license_id={self.license_id}',
            json=payload,
            headers=headers)

# Events

    def send_event(self,
                   chat_id: str = None,
                   event: dict = None,
                   attach_to_last_thread: bool = None,
                   payload: dict = None,
                   headers: dict = None) -> httpx.Response:
        ''' Sends an Event object. Use this method to send a message by specifying the Message event type in the request.
            The method updates the requester's `events_seen_up_to` as if they've seen all chat events.

            Args:
                chat_id (int): ID of the chat that you to send a message to.
                event (dict): The event object.
                attach_to_last_thread (bool): The flag is ignored for active chats.
                                              For inactive chats:
                                              True – the event will be added to the last thread;
                                              False – the request will fail. Default: False.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(
            f'{self.api_url}/send_event?license_id={self.license_id}',
            json=payload,
            headers=headers)

    def upload_file(self,
                    file: typing.BinaryIO = None,
                    payload: dict = None,
                    headers: dict = None) -> httpx.Response:
        ''' Uploads a file to the server as a temporary file. It returns a URL that expires after 24 hours unless the URL is used in `send_event`.

            Args:
                file (typing.BinaryIO): File-like object with file to upload (Maximum size: 10MB).
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(
            f'{self.api_url}/upload_file?license_id={self.license_id}',
            json=payload,
            headers=headers)

    def send_rich_message_postback(self,
                                   chat_id: str = None,
                                   event_id: str = None,
                                   postback: dict = None,
                                   thread_id: str = None,
                                   payload: dict = None,
                                   headers: dict = None) -> httpx.Response:
        ''' Sends a rich message postback.

            Args:
                chat_id (str): ID of the chat to send rich message postback to.
                event_id (str): ID of the event related to the rich message postback.
                postback (dict): Object containing postback data (id, toggled).
                thread_id (str): ID of the thread to send rich message postback to.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(
            f'{self.api_url}/send_rich_message_postback?license_id={self.license_id}',
            json=payload,
            headers=headers)

    def send_sneak_peek(self,
                        chat_id: str = None,
                        sneak_peek_text: str = None,
                        payload: dict = None,
                        headers: dict = None) -> httpx.Response:
        ''' Sends a sneak peek to a chat.

            Args:
                chat_id (str): ID of the chat to send a sneak peek to.
                sneak_peek_text (str): Sneak peek text.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(
            f'{self.api_url}/send_sneak_peek?license_id={self.license_id}',
            json=payload,
            headers=headers)

# Localization

    def get_localization(self,
                         group_id: int = None,
                         language: str = None,
                         version: str = None,
                         payload: dict = None,
                         headers: dict = None) -> httpx.Response:
        ''' Returns the localization of a given language and group in a given version. Contains translated phrases for the Chat Widget.

            Args:
                group_id (int): ID of the group that you want to get a localization for.
                language (str): The language that you want to get a localization for.
                version (str): The version that you want to get a localization for.
                               Returned from `get_dynamic_configuration` as the `localization_version` parameter.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(
            f'{self.api_url}/get_localization?license_id={self.license_id}',
            json=payload,
            headers=headers)

# Properties

    def update_chat_properties(self,
                               id: str = None,
                               properties: dict = None,
                               payload: dict = None,
                               headers: dict = None) -> httpx.Response:
        ''' Updates chat properties.

            Args:
                id (str): ID of the chat you to set a property for.
                properties (dict): Chat properties to set.
                                   You should stick to the general properties format and include namespace, property name and value.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(
            f'{self.api_url}/update_chat_properties?license_id={self.license_id}',
            json=payload,
            headers=headers)

    def delete_chat_properties(self,
                               id: str = None,
                               properties: dict = None,
                               payload: dict = None,
                               headers: dict = None) -> httpx.Response:
        ''' Deletes chat properties.

            Args:
                id (str): ID of the chat you want to delete properties of.
                properties (dict): Chat properties to delete.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(
            f'{self.api_url}/delete_chat_properties?license_id={self.license_id}',
            json=payload,
            headers=headers)

    def update_thread_properties(self,
                                 chat_id: str = None,
                                 thread_id: str = None,
                                 properties: dict = None,
                                 payload: dict = None,
                                 headers: dict = None) -> httpx.Response:
        ''' Updates chat thread properties.

            Args:
                chat_id (str): ID of the chat you to set properties for.
                thread_id (str): ID of the thread you want to set properties for.
                properties (dict): Thread properties to set.
                                   You should stick to the general properties format and include namespace, property name and value.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(
            f'{self.api_url}/update_thread_properties?license_id={self.license_id}',
            json=payload,
            headers=headers)

    def delete_thread_properties(self,
                                 chat_id: str = None,
                                 thread_id: str = None,
                                 properties: dict = None,
                                 payload: dict = None,
                                 headers: dict = None) -> httpx.Response:
        ''' Deletes chat thread properties.

            Args:
                chat_id (str): ID of the chat you want to delete the properties of.
                thread_id (str): ID of the thread you want to delete the properties of.
                properties (dict): Thread properties to delete.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(
            f'{self.api_url}/delete_thread_properties?license_id={self.license_id}',
            json=payload,
            headers=headers)

    def update_event_properties(self,
                                chat_id: str = None,
                                thread_id: str = None,
                                event_id: str = None,
                                properties: dict = None,
                                payload: dict = None,
                                headers: dict = None) -> httpx.Response:
        ''' Updates event properties.

            Args:
                chat_id (str): ID of the chat you to set properties for.
                thread_id (str): ID of the thread you want to set properties for.
                event_id (str): ID of the event you want to set properties for.
                properties (dict): Thread properties to set.
                                   You should stick to the general properties format and include namespace, property name and value.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(
            f'{self.api_url}/update_event_properties?license_id={self.license_id}',
            json=payload,
            headers=headers)

    def delete_event_properties(self,
                                chat_id: str = None,
                                thread_id: str = None,
                                event_id: str = None,
                                properties: dict = None,
                                payload: dict = None,
                                headers: dict = None) -> httpx.Response:
        ''' Deletes event properties.

            Args:
                chat_id (str): ID of the chat you to delete the properties for.
                thread_id (str): ID of the thread you want to delete the properties for.
                event_id (str): ID of the event you want to delete the properties for.
                properties (dict): Event properties to delete.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(
            f'{self.api_url}/delete_event_properties?license_id={self.license_id}',
            json=payload,
            headers=headers)

    def list_license_properties(self,
                                namespace: str = None,
                                name: str = None,
                                payload: dict = None,
                                headers: dict = None) -> httpx.Response:
        ''' Returns the properties of a given license. It only returns the properties a Customer has access to.

            Args:
                namespace (str): Property namespace to retrieve.
                name (str): Property name.
                payload (dict): Custom payload to be used as request's data.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = {}
        params = {}
        if namespace:
            params['namespace'] = namespace
        if name:
            params['name'] = name
        params['license_id'] = self.license_id
        return self.session.post(f'{self.api_url}/list_license_properties',
                                 json=payload,
                                 params=params,
                                 headers=headers)

    def list_group_properties(self,
                              group_id: int = None,
                              namespace: str = None,
                              name: str = None,
                              payload: dict = None,
                              headers: dict = None) -> httpx.Response:
        ''' Returns the properties of a given group. It only returns the properties a Customer has access to.
            Args:
                group_id (int): ID of the group you want to return the properties of.
                namespace (str): Property namespace to retrieve.
                name (str): Property name.
                payload (dict): Custom payload to be used as request's data.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = {}
        params = {}
        if namespace:
            params['namespace'] = namespace
        if name:
            params['name'] = name
        if group_id:
            params['id'] = str(group_id)
        params['license_id'] = self.license_id
        return self.session.post(f'{self.api_url}/list_group_properties',
                                 json=payload,
                                 params=params,
                                 headers=headers)

# Customers

    def get_customer(self,
                     payload: dict = None,
                     headers: dict = None) -> httpx.Response:
        ''' Returns the info about the Customer requesting it.

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
        return self.session.post(
            f'{self.api_url}/get_customer?license_id={self.license_id}',
            json={} if payload is None else payload,
            headers=headers)

    def update_customer(self,
                        name: str = None,
                        email: str = None,
                        avatar: str = None,
                        session_fields: list = None,
                        payload: dict = None,
                        headers: dict = None) -> httpx.Response:
        ''' Updates Customer's properties.

            Args:
                name (str): Name of the customer.
                email (str): Email of the customer.
                avatar (str): The URL of the Customer's avatar.
                session_fields (list): An array of custom object-enclosed key:value pairs.
                                       Respects the order of items.
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
        return self.session.post(
            f'{self.api_url}/update_customer?license_id={self.license_id}',
            json=payload,
            headers=headers)

    def set_customer_session_fields(self,
                                    session_fields: list = None,
                                    payload: dict = None,
                                    headers: dict = None) -> httpx.Response:
        ''' Updates Customer's session fields.

            Args:
                session_fields (list): An array of custom object-enclosed key:value pairs.
                                       Respects the order of items. Max keys: 100.
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
        return self.session.post(
            f'{self.api_url}/set_customer_session_fields?license_id={self.license_id}',
            json=payload,
            headers=headers)

# Status

    def list_group_statuses(self,
                            all: bool = None,
                            group_ids: list = None,
                            payload: dict = None,
                            headers: dict = None) -> httpx.Response:
        ''' Returns object with info about current routing statuses of agent groups.
            One of the optional parameters needs to be included in the request.

            Args:
                all (bool): If set to True, you will get statuses of all the groups.
                group_ids (list): A table of groups' IDs
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
        return self.session.post(
            f'{self.api_url}/list_group_statuses?license_id={self.license_id}',
            json=payload,
            headers=headers)


# Other

    def check_goals(self,
                    session_fields: list = None,
                    group_id: int = None,
                    page_url: str = None,
                    payload: dict = None,
                    headers: dict = None) -> httpx.Response:
        ''' Customer can use this method to trigger checking if goals were achieved.
            Then, Agents receive the information. You should call this method to provide goals parameters for the server
            when the customers limit is reached. Works only for offline Customers.

            Args:
                session_fields (list): An array of custom object-enclosed key:value pairs.
                group_id (int): Group ID to check the goals for.
                page_url (str): URL of the page to check the goals for.
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
        return self.session.post(
            f'{self.api_url}/check_goals?license_id={self.license_id}',
            json=payload,
            headers=headers)

    def get_form(self,
                 group_id: int = None,
                 type: str = None,
                 payload: dict = None,
                 headers: dict = None) -> httpx.Response:
        ''' Returns an empty ticket form of a prechat or postchat survey.

            Args:
                group_id (int): ID of the group from which you want the form.
                type (str): Form type; possible values: prechat or postchat.
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
        return self.session.post(
            f'{self.api_url}/get_form?license_id={self.license_id}',
            json=payload,
            headers=headers)

    def get_predicted_agent(self,
                            payload: dict = None,
                            headers: dict = None) -> httpx.Response:
        ''' Gets the predicted Agent - the one the Customer will chat with when the chat starts.
            To use this method, the Customer needs to be logged in, which can be done via the `login` method.

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
        return self.session.post(
            f'{self.api_url}/get_predicted_agent?license_id={self.license_id}',
            json={} if payload is None else payload,
            headers=headers)

    def get_url_info(self,
                     url: str = None,
                     payload: dict = None,
                     headers: dict = None) -> httpx.Response:
        ''' Returns the info on a given URL.

            Args:
                url (str): Valid website URL.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(
            f'{self.api_url}/get_url_info?license_id={self.license_id}',
            json=payload,
            headers=headers)

    def mark_events_as_seen(self,
                            chat_id: str = None,
                            seen_up_to: str = None,
                            payload: dict = None,
                            headers: dict = None) -> httpx.Response:
        ''' Updates `seen_up_to` value for a given chat.

            Args:
                chat_id (str): ID of the chat to update `seen_up_to`.
                seen_up_to (str): RFC 3339 date-time format.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(
            f'{self.api_url}/mark_events_as_seen?license_id={self.license_id}',
            json=payload,
            headers=headers)

    def accept_greeting(self,
                        greeting_id: int = None,
                        unique_id: str = None,
                        payload: dict = None,
                        headers: dict = None) -> httpx.Response:
        ''' Marks an incoming greeting as seen.

            Args:
                greeting_id (int): ID of the greeting configured within the license to accept.
                unique_id (str): ID of the greeting to accept. You can get it from the `incoming_greeting` push.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(
            f'{self.api_url}/accept_greeting?license_id={self.license_id}',
            json=payload,
            headers=headers)

    def cancel_greeting(self,
                        unique_id: str = None,
                        payload: dict = None,
                        headers: dict = None) -> httpx.Response:
        ''' Cancels a greeting (an invitation to the chat).
            For example, Customers could cancel greetings by minimalizing the chat widget with a greeting.

            Args:
                unique_id (str): ID of the greeting to cancel. You can get it from the `incoming_greeting` push.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.

            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(
            f'{self.api_url}/cancel_greeting?license_id={self.license_id}',
            json=payload,
            headers=headers)


class CustomerWeb33(CustomerWebInterface):
    ''' Customer API version 3.3 class. '''


class CustomerWeb34(CustomerWebInterface):
    ''' Customer API version 3.4 class. '''
