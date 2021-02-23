''' Configuration API client implementation. '''

from abc import ABCMeta

import requests


class ConfigurationApi:
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
                `ConfigurationApiInterface`.

            Raises:
                ValueError: If the specified version does not exist.
        '''
        versions = {'3.3': Version33(token, version, env)}
        client = versions.get(version)
        if not client:
            raise ValueError('Provided version does not exist.')
        return client


class ConfigurationApiInterface(metaclass=ABCMeta):
    ''' Abstract interface class. '''
    def __init__(self, token: str, version: str, env: str = 'production'):
        env = f'{env}.' if env in ['labs', 'staging'] else ''
        self.api_url = f'https://api.{env}livechatinc.com/v{version}/configuration/action'
        self.session = requests.Session()
        self.session.headers.update({'Authorization': token})

# Agents

    def create_agent(self, payload: dict = None) -> requests.Response:
        ''' Creates a new Agent with specified parameters within a license. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/create_agent', json=payload)

    def get_agent(self, payload: dict = None) -> requests.Response:
        ''' Returns the info about an Agent specified by id. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/get_agent', json=payload)

    def list_agents(self, payload: dict = None) -> requests.Response:
        ''' Returns all Agents within a license. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/list_agents', json=payload)

    def update_agent(self, payload: dict = None) -> requests.Response:
        ''' Updates the properties of an Agent specified by id. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/update_agent', json=payload)

    def delete_agent(self, payload: dict = None) -> requests.Response:
        ''' Deletes an Agent specified by id. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/delete_agent', json=payload)

    def suspend_agent(self, payload: dict = None) -> requests.Response:
        ''' Suspends an Agent specified by id. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/suspend_agent', json=payload)

    def unsuspend_agent(self, payload: dict = None) -> requests.Response:
        ''' Unsuspends an Agent specified by id. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/unsuspend_agent',
                                 json=payload)

    def request_agent_unsuspension(self,
                                   payload: dict = None) -> requests.Response:
        ''' A suspended Agent can send emails to license owners and vice owners
            with an unsuspension request. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/request_agent_unsuspension',
                                 json=payload)

    def approve_agent(self, payload: dict = None) -> requests.Response:
        ''' Approves an Agent thus allowing the Agent to use the application. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/approve_agent', json=payload)

# Auto access

    def add_auto_access(self, payload: dict = None) -> requests.Response:
        ''' Creates an auto access data structure, which is a set of conditions
            for the tracking URL and geolocation of a customer. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/add_auto_access',
                                 json=payload)

    def list_auto_accesses(self, payload: dict = None) -> requests.Response:
        ''' Returns all existing auto access data structures. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/list_auto_accesses',
                                 json=payload)

    def delete_auto_access(self, payload: dict = None) -> requests.Response:
        ''' Deletes an existing auto access data structure specified by its ID. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/delete_auto_access',
                                 json=payload)

    def reorder_auto_access(self, payload: dict = None) -> requests.Response:
        ''' Moves an existing auto access data structure, specified by id,
            before another one, specified by next_id. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/reorder_auto_access',
                                 json=payload)

# Bots

    def create_bot(self, payload: dict = None) -> requests.Response:
        ''' Creates a new Bot. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/create_bot', json=payload)

    def delete_bot(self, payload: dict = None) -> requests.Response:
        ''' Deletes a Bot. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/delete_bot', json=payload)

    def update_bot(self, payload: dict = None) -> requests.Response:
        ''' Updates an existing Bot. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/update_bot', json=payload)

    def list_bots(self, payload: dict = None) -> requests.Response:
        ''' Returns the list of Bots created within a license. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/list_bots', json=payload)

    def get_bot(self, payload: dict = None) -> requests.Response:
        ''' Gets a Bot specified by id. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/get_bot', json=payload)

# Groups

    def create_group(self, payload: dict = None) -> requests.Response:
        ''' Creates a new group. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/create_group', json=payload)

    def update_group(self, payload: dict = None) -> requests.Response:
        ''' Updates an existing group. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/update_group', json=payload)

    def delete_group(self, payload: dict = None) -> requests.Response:
        ''' Deletes an existing group. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/delete_group', json=payload)

    def list_groups(self, payload: dict = None) -> requests.Response:
        ''' Lists all the exisiting groups. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/list_groups', json=payload)

    def get_group(self, payload: dict = None) -> requests.Response:
        ''' Returns details about a group specified by its id. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/get_group', json=payload)


# Properties

    def register_properties(self, payload: dict = None) -> requests.Response:
        ''' Registers a property. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/get_group', json=payload)

    def list_registered_properties(self,
                                   payload: dict = None) -> requests.Response:
        ''' Returns registered properties. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/list_registered_properties',
                                 json=payload)

    def update_license_properties(self,
                                  payload: dict = None) -> requests.Response:
        ''' Updates a property value within a license. This operation doesn't
            overwrite the existing values. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/update_license_properties',
                                 json=payload)

    def list_license_properties(self,
                                payload: dict = None) -> requests.Response:
        ''' Returns the properties set within a license. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/list_license_properties',
                                 json=payload)

    def delete_license_properties(self,
                                  payload: dict = None) -> requests.Response:
        ''' Deletes the properties set within a license. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/delete_license_properties',
                                 json=payload)

    def update_group_properties(self,
                                payload: dict = None) -> requests.Response:
        ''' Updates a property value within a group as the property location.
            This operation doesn't overwrite the existing values. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/update_group_properties',
                                 json=payload)

    def list_group_properties(self, payload: dict = None) -> requests.Response:
        ''' Returns the properties set within a group. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/list_group_properties',
                                 json=payload)

    def delete_group_properties(self,
                                payload: dict = None) -> requests.Response:
        ''' Deletes the properties set within a group. '''
        payload = {} if payload is None else payload
        return self.session.post(f'{self.api_url}/delete_group_properties',
                                 json=payload)


class Version33(ConfigurationApiInterface):
    ''' Configuration API version 3.3 class. '''
    pass
