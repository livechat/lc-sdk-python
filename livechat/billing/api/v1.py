''' Billing API module with client class in version 1. '''

import httpx

from livechat.utils.helpers import prepare_payload
from livechat.utils.http_client import HttpClient


class BillingApiV1(HttpClient):
    ''' Billing API client class in version 1. '''
    def __init__(self,
                 token: str,
                 base_url: str,
                 http2: bool,
                 proxies=None,
                 verify: bool = True):
        super().__init__(token, base_url, http2, proxies, verify)
        self.api_url = f'https://{base_url}/v1'

    # direct_charge

    def create_direct_charge(self,
                             name: str = None,
                             price: int = None,
                             quantity: int = None,
                             return_url: str = None,
                             per_account: bool = None,
                             test: str = None,
                             payload: dict = None,
                             headers: dict = None) -> httpx.Response:
        ''' Creates a new direct charge for the user (one time fee).
            Args:
                name (str): Name of the direct charge.
                price (int): Price of the charge defined in cents.
                quantity (int): Number of the accounts within the organization.
                return_url (str): Redirection url for the client.
                per_account (bool): Whether or not the app is sold in ppa account model.
                test (str): Whether or not the direct charge is for test.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.
            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server's response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/direct_charge',
                                 json=payload,
                                 headers=headers)

    def get_direct_charge(self,
                          charge_id: str,
                          params: dict = None,
                          headers: dict = None) -> httpx.Response:
        ''' Returns specific direct charge.
            Args:
                charge_id (str): ID of the direct charge.
                params (dict): Custom params to be used in request's query string.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.
            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server's response to an HTTP request.
        '''
        if params is None:
            params = prepare_payload(locals())
            del params['charge_id']
        return self.session.get(f'{self.api_url}/direct_charge/{charge_id}',
                                params=params,
                                headers=headers)

    def list_direct_charges(self,
                            page: int = None,
                            status: str = None,
                            params: dict = None,
                            headers: dict = None) -> httpx.Response:
        ''' Lists all direct charges.
            Args:
                page (int):
                status (str):
                params (dict): Custom params to be used in request's query string.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.
            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server's response to an HTTP request.
        '''
        if params is None:
            params = prepare_payload(locals())
        return self.session.get(f'{self.api_url}/direct_charge',
                                params=params,
                                headers=headers)

    def activate_direct_charge(self,
                               charge_id: str,
                               payload: dict = None,
                               headers: dict = None) -> httpx.Response:
        ''' Activates specific direct charge.
            Args:
                charge_id (str): ID of the direct charge.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.
            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server's response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
            del payload['charge_id']
        return self.session.put(f'{self.api_url}/direct_charge/{charge_id}',
                                json=payload,
                                headers=headers)

# ledger

    def get_ledger(self,
                   params: dict = None,
                   headers: dict = None) -> httpx.Response:
        ''' Returns current ledger.
            Args:
                params (dict): Custom params to be used in request's query string.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.
            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server's response to an HTTP request.
        '''
        if params is None:
            params = prepare_payload(locals())
        return self.session.get(f'{self.api_url}/ledger',
                                params=params,
                                headers=headers)

    def get_ledger_balance(self,
                           params: dict = None,
                           headers: dict = None) -> httpx.Response:
        ''' Returns current ledger balance.
            Args:
                params (dict): Custom params to be used in request's query string.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.
            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server's response to an HTTP request.
        '''
        if params is None:
            params = prepare_payload(locals())
        return self.session.get(f'{self.api_url}/ledger/balance',
                                params=params,
                                headers=headers)


# recurent_charge

    def create_recurrent_charge(self,
                                name: str = None,
                                price: int = None,
                                return_url: str = None,
                                per_account: bool = None,
                                trial_days: int = None,
                                months: int = None,
                                test: str = True,
                                payload: dict = None,
                                headers: dict = None) -> httpx.Response:
        ''' Creates a new reccurent charge for the user (periodic payment).
            Args:
                name (str): Name of the reccurent charge.
                price (int): Price of the charge defined in cents.
                return_url (str): Redirection url for the client.
                per_account (bool): Whether or not the app is sold in ppa account model.
                trial_days (int): Number of granted trial days.
                months (int): Charge frequency expressed in months.
                test (str): Whether or not the direct charge is for test.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.
            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server's response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
        return self.session.post(f'{self.api_url}/recurrent_charge',
                                 json=payload,
                                 headers=headers)

    def get_recurrent_charge(self,
                             charge_id: str,
                             params: dict = None,
                             headers: dict = None) -> httpx.Response:
        ''' Gets specific reccurent charge.
            Args:
                charge_id (str): ID of the direct charge.
                params (dict): Custom params to be used in request's query string.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.
            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server's response to an HTTP request.
        '''
        if params is None:
            params = prepare_payload(locals())
            del params['charge_id']
        return self.session.get(f'{self.api_url}/recurrent_charge/{charge_id}',
                                params=params,
                                headers=headers)

    def accept_recurrent_charge(self,
                                charge_id: str,
                                payload: dict = None,
                                headers: dict = None) -> httpx.Response:
        ''' Accpets specific reccurent charge.
            Args:
                charge_id (str): ID of the direct charge.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.
            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server's response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
            del payload['charge_id']
        return self.session.put(
            f'{self.api_url}/recurrent_charge/{charge_id}/accept',
            json=payload,
            headers=headers)

    def decline_recurrent_charge(self,
                                 charge_id: str,
                                 payload: dict = None,
                                 headers: dict = None) -> httpx.Response:
        ''' Declines specific reccurent charge.
            Args:
                charge_id (str): ID of the direct charge.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.
            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server's response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
            del payload['charge_id']
        return self.session.put(
            f'{self.api_url}/recurrent_charge/{charge_id}/decline',
            json=payload,
            headers=headers)

    def activate_recurrent_charge(self,
                                  charge_id: str,
                                  payload: dict = None,
                                  headers: dict = None) -> httpx.Response:
        ''' Activates specific reccurent charge.
            Args:
                charge_id (str): ID of the direct charge.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.
            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server's response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
            del payload['charge_id']
        return self.session.put(
            f'{self.api_url}/recurrent_charge/{charge_id}/activate',
            json=payload,
            headers=headers)

    def cancel_recurrent_charge(self,
                                charge_id: str,
                                payload: dict = None,
                                headers: dict = None) -> httpx.Response:
        ''' Cancels specific reccurent charge.
            Args:
                charge_id (str): ID of the direct charge.
                payload (dict): Custom payload to be used as request's data.
                                It overrides all other parameters provided for the method.
                headers (dict): Custom headers to be used with session headers.
                                They will be merged with session-level values that are set,
                                however, these method-level parameters will not be persisted across requests.
            Returns:
                httpx.Response: The Response object from `httpx` library,
                                which contains a server's response to an HTTP request.
        '''
        if payload is None:
            payload = prepare_payload(locals())
            del payload['charge_id']
        return self.session.put(
            f'{self.api_url}/recurrent_charge/{charge_id}/cancel',
            json=payload,
            headers=headers)
