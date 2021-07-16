''' Agent Web client implementation. '''

# pylint: disable=W0613,R0913,W0622,C0103,W0221

import typing
from abc import ABCMeta

import requests

from livechat.utils.helpers import prepare_payload


# pylint: disable=R0903
class AgentWeb:
    ''' Allows retrieval of client for specific Agent Web
        API version. '''
    @staticmethod
    def get_client(access_token: str,
                   version: str = '3.3',
                   base_url: str = 'api.livechatinc.com'):
        ''' Returns client for specific API version.

            Args:
                token (str): Full token with type (Bearer/Basic) that will be
                                used as `Authorization` header in requests to API.
                version (str): API's version. Defaults to `3.3`.
                base_url (str): API's base url. Defaults to `api.livechatinc.com`.

            Returns:
                API client object for specified version based on
                `AgentWebApiInterface`.

            Raises:
                ValueError: If the specified version does not exist.
        '''
        client = {
            '3.3': AgentWeb33(access_token, version, base_url),
            '3.4': AgentWeb34(access_token, version, base_url)
        }.get(version)
        if not client:
            raise ValueError('Provided version does not exist.')
        return client


class AgentWebInterface(metaclass=ABCMeta):
    ''' Main class containing API methods. '''
    def __init__(self, access_token: str, version: str, base_url: str):
        self.api_url = f'https://{base_url}/v{version}/agent/action'
        self.session = requests.Session()
        self.session.headers.update({'Authorization': access_token})

    def modify_header(self, header: dict) -> None:
        ''' Modifies provided header in session object.

            Args:
                header (dict): Header which needs to be modified.
        '''
        self.session.headers.update(header)

    def remove_header(self, key) -> None:
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

    def add_user_to_chat(self,
                         chat_id: str = None,
                         user_id: str = None,
                         user_type: str = None,
                         require_active_thread: bool = None,
                         payload: dict = None) -> requests.Response:
        ''' Adds a user to the chat. You can't add more than one customer user type to the chat.

            Args:
                chat_id (str): chat ID.
                user_id (str): user ID.
                user_type (str): Possible values: agent or customer.
                require_active_thread (bool): If true, it adds a user to a chat
                                              only if that chat has an active
                                              thread; default false.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/add_user_to_chat',
                                 json=payload)

    def list_chats(self,
                   filters: dict = None,
                   sort_order: str = None,
                   limit: int = None,
                   page_id: str = None,
                   payload: dict = None) -> requests.Response:
        ''' Returns summaries of the chats an Agent has access to.

            Args:
                filters (dict): Possible request filters. Mustn't change between
                                requests for subsequent pages. Otherwise,
                                the behavior is undefined.
                sort_order (str): Possible values: asc, desc (default).
                                  Chat summaries are sorted by the creation
                                  date of its last thread.
                limit (int): Limit of results per page. Default: 10, maximum: 100.
                page_id (str): ID of the page with paginated results.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided
                                for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/list_chats', json=payload)

    def list_threads(self,
                     chat_id: str = None,
                     sort_order: str = None,
                     limit: str = None,
                     page_id: str = None,
                     min_events_count: int = None,
                     filters: dict = None,
                     payload: dict = None) -> requests.Response:
        ''' Returns threads that the current Agent has access to in a given chat.

            Args:
                chat_id (str): ID of the chat for which threads are to be listed.
                sort_order (str): Possible values: asc, desc (default).
                limit (str): Limit of results per page. Default: 3, maximum: 100.
                page_id (str): ID of the page with paginated results.
                min_events_count (int): Range: 1-100;
                                        Specifies the minimum number of events
                                        to be returned in the response.
                filters (dict): Possible request filters.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/list_threads', json=payload)

    def get_chat(self,
                 chat_id: str = None,
                 thread_id: str = None,
                 payload: dict = None) -> requests.Response:
        ''' Returns a thread that the current Agent has access to in a given chat

            Args:
                chat_id (str): ID of the chat for which thread is to be returned.
                thread_id (str): ID of the thread to show. Default: the latest thread (if exists)
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/get_chat', json=payload)

    def list_archives(self,
                      filters: dict = None,
                      page_id: str = None,
                      sort_order: str = None,
                      limit: str = None,
                      highlights: dict = None,
                      payload: dict = None) -> requests.Response:
        ''' Returns a list of the chats an Agent has access to.
            Together with a chat, the events of one thread from this chat are returned.

            Args:
                filters (dict): Possible request filters.
                page_id (str): ID of the page with paginated results.
                sort_order (str): Possible values: asc, desc (default).
                                  Chat summaries are sorted by the creation date
                                  of its last thread.
                limit (str): Limit of results per page. Default: 10, maximum: 100.
                highlights (dict): Use it to highlight the match of filters.query.
                                   To enable highlights with default parameters,
                                   pass an empty object.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/list_archives', json=payload)

    def start_chat(self,
                   chat: dict = None,
                   active: bool = None,
                   continuous: bool = None,
                   payload: dict = None) -> requests.Response:
        ''' Starts a chat.

            Args:
                chat (dict): Dict containing chat properties, access and thread.
                active (bool): When set to False, creates an inactive thread; default: True.
                continuous (bool): Starts chat as continuous (online group is not required); default: False.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/start_chat', json=payload)

    def resume_chat(self,
                    chat: dict = None,
                    active: bool = None,
                    continuous: bool = None,
                    payload: dict = None) -> requests.Response:
        ''' Restarts an archived chat.

            Args:
                chat (dict): Dict containing chat properties, access and thread.
                active (bool): When set to False, creates an inactive thread; default: True.
                continuous (bool): Starts chat as continuous (online group is not required); default: False.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/resume_chat', json=payload)

    def deactivate_chat(self,
                        id: str = None,
                        payload: dict = None) -> requests.Response:
        ''' Deactivates a chat by closing the currently open thread.
            Sending messages to this thread will no longer be possible.

            Args:
                id (str): Chat ID to deactivate.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/deactivate_chat',
                                 json=payload)

    def follow_chat(self,
                    id: str = None,
                    payload: dict = None) -> requests.Response:
        ''' Marks a chat as followed. All changes to the chat will be sent to the requester
            until the chat is reactivated or unfollowed. Chat members don't need to follow
            their chats. They receive all chat pushes regardless of their follower status.

            Args:
                id (str): ID of chat to be followed.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/follow_chat', json=payload)

    def unfollow_chat(self,
                      id: str = None,
                      payload: dict = None) -> requests.Response:
        ''' Removes the requester from the chat followers. After that, only key changes
            to the chat (like transfer_chat or close_active_thread) will be sent
            to the requester. Chat members cannot unfollow the chat.

            Args:
                id (str): ID of chat to be unfollowed.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/unfollow_chat', json=payload)

# Chat access

    def transfer_chat(self,
                      id: str = None,
                      target: dict = None,
                      force: bool = None,
                      payload: dict = None) -> requests.Response:
        ''' Transfers a chat to an agent or a group.

            Args:
                id (str): chat ID
                target (dict): If missing, chat will be transferred within the current group.
                force (bool): If true, always transfers chats. Otherwise, fails
                              when unable to assign any agent from the requested groups; default false.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/transfer_chat', json=payload)
# Chat users

    def remove_user_from_chat(self,
                              chat_id: str = None,
                              user_id: str = None,
                              user_type: str = None,
                              payload: dict = None) -> requests.Response:
        ''' Removes a user from chat.

            Args:
                chat_id (str): chat ID.
                user_id (str): user ID.
                user_type (str): Possible values: agent or customer.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/remove_user_from_chat',
                                 json=payload)

# Events

    def send_event(self,
                   chat_id: str = None,
                   event: dict = None,
                   attach_to_last_thread: bool = None,
                   payload: dict = None) -> requests.Response:
        ''' Sends an Event object. Use this method to send a message by specifying the Message event type in the request.
            The method updates the requester's `events_seen_up_to` as if they've seen all chat events.

            Args:
                chat_id (int): ID of the chat that you to send a message to.
                event (dict): Event object.
                attach_to_last_thread (bool): The flag is ignored for active chats.
                                              For inactive chats:
                                              True – the event will be added to the last thread;
                                              False – the request will fail. Default: False.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/send_event', json=payload)

    def upload_file(self,
                    file: typing.BinaryIO = None,
                    payload: dict = None) -> requests.Response:
        ''' Uploads a file to the server as a temporary file. It returns a URL that expires
            after 24 hours unless the URL is used in `send_event`.

            Args:
                file (typing.BinaryIO): File-like object with file to upload (Maximum size: 10MB).
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/upload_file', json=payload)

    def send_rich_message_postback(self,
                                   chat_id: str = None,
                                   thread_id: str = None,
                                   event_id: str = None,
                                   postback: dict = None,
                                   payload: dict = None) -> requests.Response:
        ''' Sends a rich message postback.

            Args:
                chat_id (str): ID of the chat to send rich message postback to.
                thread_id (str): ID of the thread to send rich message postback to.
                event_id (str): ID of the event related to the rich message postback.
                postback (dict): Object containing postback data (id, toggled).
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/send_rich_message_postback',
                                 json=payload)

# Properties

    def update_chat_properties(self,
                               id: str = None,
                               properties: dict = None,
                               payload: dict = None) -> requests.Response:
        ''' Updates chat properties.

            Args:
                id (str): ID of the chat you to set a property for.
                properties (dict): Chat properties to set.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/update_chat_properties',
                                 json=payload)

    def delete_chat_properties(self,
                               id: str = None,
                               properties: dict = None,
                               payload: dict = None) -> requests.Response:
        ''' Deletes chat properties.

            Args:
                id (str): ID of the chat you want to delete properties of.
                properties (dict): Chat properties to delete.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/delete_chat_properties',
                                 json=payload)

    def update_thread_properties(self,
                                 chat_id: str = None,
                                 thread_id: str = None,
                                 properties: dict = None,
                                 payload: dict = None) -> requests.Response:
        ''' Updates chat thread properties.

            Args:
                chat_id (str): ID of the chat you to set properties for.
                thread_id (str): ID of the thread you want to set properties for.
                properties (dict): Thread properties to set.
                                   You should stick to the general properties format and include namespace, property name and value.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/update_thread_properties',
                                 bjson=payload)

    def delete_thread_properties(self,
                                 chat_id: str = None,
                                 thread_id: str = None,
                                 properties: dict = None,
                                 payload: dict = None) -> requests.Response:
        ''' Deletes chat thread properties.

            Args:
                chat_id (str): ID of the chat you want to delete the properties of.
                thread_id (str): ID of the thread you want to delete the properties of.
                properties (dict): Thread properties to delete.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/delete_thread_properties',
                                 json=payload)

    def update_event_properties(self,
                                chat_id: str = None,
                                thread_id: str = None,
                                event_id: str = None,
                                properties: dict = None,
                                payload: dict = None) -> requests.Response:
        ''' Updates event properties.

            Args:
                chat_id (str): ID of the chat you to set properties for.
                thread_id (str): ID of the thread you want to set properties for.
                event_id (str): ID of the event you want to set properties for.
                properties (dict): Thread properties to set.
                                   You should stick to the general properties format and include namespace, property name and value.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/update_event_properties',
                                 json=payload)

    def delete_event_properties(self,
                                chat_id: str = None,
                                thread_id: str = None,
                                event_id: str = None,
                                properties: dict = None,
                                payload: dict = None) -> requests.Response:
        ''' Deletes event properties.

            Args:
                chat_id (str): ID of the chat you to delete the properties for.
                thread_id (str): ID of the thread you want to delete the properties for.
                event_id (str): ID of the event you want to delete the properties for.
                properties (dict): Event properties to delete.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/delete_event_properties',
                                 json=payload)

# Thread tags

    def tag_thread(self,
                   chat_id: str = None,
                   thread_id: str = None,
                   tag: str = None,
                   payload: dict = None) -> requests.Response:
        ''' Tags thread.

            Args:
                chat_id (str): ID of the chat you want to add a tag to.
                thread_id (str): ID of the thread you want to add a tag to.
                tag (str): Tag name.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/tag_thread', json=payload)

    def untag_thread(self,
                     chat_id: str = None,
                     thread_id: str = None,
                     tag: str = None,
                     payload: dict = None) -> requests.Response:
        ''' Untags thread.

            Args:
                chat_id (str): ID of the chat you want to remove a tag from.
                thread_id (str): ID of the thread you want to remove a tag from.
                tag (str): Tag name.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/untag_thread', json=payload)

# Customers

    def get_customer(self,
                     id: str = None,
                     payload: dict = None) -> requests.Response:
        ''' Returns the info about the Customer with a given id.

            Args:
                id (str): customer id
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/get_customer', json=payload)

    def list_customers(self,
                       page_id: str = None,
                       limit: str = None,
                       sort_order: str = None,
                       sort_by: str = None,
                       filters: dict = None,
                       payload: dict = None) -> requests.Response:
        ''' Returns the list of Customers.

            Args:
                page_id (str): ID of the page with paginated results.
                limit (str): Limit of results per page. Default: 10, maximum: 100.
                sort_order (str): Possible values: asc, desc (default).
                sort_by (str): When sorting by fields other than created_at, the entries
                               with identical values will be additionally sorted by their
                               creation time. Possible values: created_at (default),
                               threads_count, visits_count, agent_last_event, customer_last_event.
                filters (dict): Possible request filters.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/list_customers',
                                 json=payload)

    def create_customer(self,
                        name: str = None,
                        email: str = None,
                        avatar: str = None,
                        session_fields: list = None,
                        payload: dict = None) -> requests.Response:
        ''' Creates a new Customer user type.

            Args:
                name (str): Customer's name.
                email (str): Customer's email.
                avatar (str): URL of the Customer's avatar
                session_fields (list): An array of custom object-enclosed key:value pairs.
                                       Respects the order of items.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/create_customer',
                                 json=payload)

    def update_customer(self,
                        id: str = None,
                        name: str = None,
                        email: str = None,
                        avatar: str = None,
                        session_fields: list = None,
                        payload: dict = None) -> requests.Response:
        ''' Updates Customer's properties.

            Args:
                id (str): ID of the Customer.
                name (str): Customer's name.
                email (str): Customer's email.
                avatar (str): URL of the Customer's avatar.
                session_fields (list): An array of custom object-enclosed key:value pairs.
                                       Respects the order of items.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/update_customer',
                                 json=payload)

    def ban_customer(self,
                     id: str = None,
                     ban: dict = None,
                     payload: dict = None) -> requests.Response:
        ''' Bans the customer for a specific period of time. It immediately
            disconnects all active sessions of this customer and does not accept
            new ones during the ban lifespan.

            Args:
                id (str): ID of the Customer.
                ban (dict): Ban object containing the number of days that
                        the Customer will be banned.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/ban_customer', json=payload)

    def follow_customer(self,
                        id: str = None,
                        payload: dict = None) -> requests.Response:
        ''' Marks a customer as followed. As a result, the requester (an agent)
            will receive the info about all the changes related to that customer
            via pushes. Once the customer leaves the website or is unfollowed,
            the agent will no longer receive that information.

            Args:
                id (str): ID of the Customer.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/follow_customer',
                                 json=payload)

    def unfollow_customer(self,
                          id: str = None,
                          payload: dict = None) -> requests.Response:
        ''' Removes the agent from the list of customer's followers. Calling this
            method on a customer the agent's chatting with will result in success,
            however, the agent will still receive pushes about the customer's data
            updates. The unfollowing will take effect once the chat ends.

            Args:
                id (str): ID of the Customer.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/unfollow_customer',
                                 json=payload)

# Status

    def set_routing_status(self,
                           status: str = None,
                           agent_id: str = None,
                           payload: dict = None) -> requests.Response:
        ''' Changes the status of an Agent or a Bot Agent.

            Args:
                status (str): For Agents: accepting_chats or not_accepting_chats;
                              for Bot Agents: accepting_chats, not_accepting_chats, or offline
                agent_id (str): If not specified, the requester's status will be updated.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/set_routing_status',
                                 json=payload)

    def list_routing_statuses(self,
                              filters: dict = None,
                              payload: dict = None) -> requests.Response:
        ''' Returns the current routing status of each agent selected by the provided filters.

            Args:
                filters (dict): Possible request filters.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/list_routing_statuses',
                                 json=payload)


# Other

    def mark_events_as_seen(self,
                            chat_id: str = None,
                            seen_up_to: str = None,
                            payload: dict = None) -> requests.Response:
        ''' Updates `seen_up_to` value for a given chat.

            Args:
                chat_id (str): Chat to mark events.
                seen_up_to (str): Date up to which mark events - RFC 3339 date-time format
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/mark_events_as_seen',
                                 json=payload)

    def send_typing_indicator(self,
                              chat_id: str = None,
                              recipients: str = None,
                              is_typing: bool = None,
                              payload: dict = None) -> requests.Response:
        ''' Sends typing indicator.

            Args:
                chat_id (str): ID of the chat that to send the typing indicator to.
                recipients (str): Default: all; agents.
                is_typing (bool): A flag that indicates if you are typing.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/send_typing_indicator',
                                 json=payload)

    def multicast(self,
                  recipients: dict = None,
                  content: typing.Any = None,
                  type: str = None,
                  payload: dict = None) -> requests.Response:
        ''' Sends a multicast (chat-unrelated communication).

            Args:
                recipients (dict): Object containing filters related to multicast recipients.
                content (typing.Any): A JSON message to be sent.
                type (str): Multicast message type.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/multicast', json=payload)

    def list_agents_for_transfer(self,
                                 chat_id: str = None,
                                 payload: dict = None) -> requests.Response:
        ''' Returns the list of Agents you can transfer a chat to.

            Args:
                chat_id (str): ID of the chat you want to transfer.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/list_agents_for_transfer',
                                 json=payload)


class AgentWeb33(AgentWebInterface):
    ''' Agent API version 3.3 class. '''

    # Chat access

    def grant_chat_access(self,
                          id: str = None,
                          access: dict = None,
                          payload: dict = None) -> requests.Response:
        ''' Grants access to a new chat without overwriting the existing ones.

            Args:
                id (str): chat ID
                access (dict): Dict containing chat access (type and id)
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/grant_chat_access',
                                 json=payload)

    def revoke_chat_access(self,
                           id: str = None,
                           access: dict = None,
                           payload: dict = None) -> requests.Response:
        ''' Revoke access to a chat.

            Args:
                id (str): chat ID
                access (dict): Dict containing chat access (type and id)
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/revoke_chat_access',
                                 json=payload)


class AgentWeb34(AgentWebInterface):
    ''' Agent API version 3.4 class. '''

    # Chats

    def add_user_to_chat(self,
                         chat_id: str = None,
                         user_id: str = None,
                         user_type: str = None,
                         visibility: str = None,
                         payload: dict = None) -> requests.Response:
        ''' Adds a user to the chat. You can't add more than one customer user
            type to the chat.

            Args:
                chat_id (str): chat ID.
                user_id (str): user ID.
                user_type (str): Possible values: agent or customer.
                visibility (str): Determines the visibility of events sent by
                                  the agent. Possible values: `all` or `agents`.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/add_user_to_chat',
                                 json=payload)


# Other

    def send_typing_indicator(self,
                              chat_id: str = None,
                              visibility: str = None,
                              is_typing: bool = None,
                              payload: dict = None) -> requests.Response:
        ''' Sends typing indicator.

            Args:
                chat_id (str): ID of the chat that to send the typing indicator to.
                visibility (str): Possible values: `all`, `agents`.
                is_typing (bool): A flag that indicates if you are typing.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.

            Returns:
                requests.Response: The Response object from `requests` library,
                                   which contains a server’s response to an HTTP request. '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/send_typing_indicator',
                                 json=payload)