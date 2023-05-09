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
                 verify: bool = True,
                 disable_logging: bool = False):
        super().__init__(token, base_url, http2, proxies, verify,
                         disable_logging)
        self.api_url = f'https://{base_url}/v1'

    # direct_charge

    def create_direct_charge(self,
                             name: str = None,
                             price: int = None,
                             quantity: int = None,
                             return_url: str = None,
                             per_account: bool = None,
                             test: bool = None,
                             payload: dict = None,
                             headers: dict = None) -> httpx.Response:
        ''' Creates a new direct charge for the user (one time fee).
            Args:
                name (str): Name of the direct charge.
                price (int): Price of the charge defined in cents.
                quantity (int): Number of the accounts within the organization.
                return_url (str): Redirection url for the client.
                per_account (bool): Whether or not the app is sold in ppa account model. Default: False.
                test (str): Whether or not the direct charge is for test. Default: False.
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
                            order_client_id: str = None,
                            params: dict = None,
                            headers: dict = None) -> httpx.Response:
        ''' Lists all direct charges.
            Args:
                page (int): Navigate to page number. Default: 1.
                status (str): Filter charges by status. One of pending, accepted, active, declined, processed, failed or success.
                order_client_id (str): Filter by specific `order_client_id`.
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
        return self.session.put(
            f'{self.api_url}/direct_charge/{charge_id}/activate',
            json=payload,
            headers=headers)

# ledger

    def get_ledger(self,
                   page: int = None,
                   params: dict = None,
                   headers: dict = None) -> httpx.Response:
        ''' Returns current ledger.
            Args:
                page (int): Navigate to page number. Default: 1.
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
        ''' Returns current ledger balance in cents.
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
                                test: bool = True,
                                payload: dict = None,
                                headers: dict = None) -> httpx.Response:
        ''' Creates a new recurrent charge for the user (periodic payment).
            Args:
                name (str): Name of the recurrent charge.
                price (int): Price of the charge defined in cents.
                return_url (str): Redirection url for the client.
                per_account (bool): Whether or not the app is sold in ppa account model. Default: False.
                trial_days (int): Number of granted trial days. Default: 0.
                months (int): Charge frequency expressed in months. Default: 1.
                test (str): Whether or not the direct charge is for test. Default: False.
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
        ''' Gets specific recurrent charge.
            Args:
                charge_id (str): ID of the recurrent charge.
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

    def list_recurrent_charges(self,
                               page: int = None,
                               status: str = None,
                               order_client_id: str = None,
                               params: dict = None,
                               headers: dict = None) -> httpx.Response:
        ''' Lists all recurrent charges.
            Args:
                page (int): Navigate to specific page number. Default: 1.
                status (str): Filter charges by status. One of pending, accepted, active, declined, processed, failed or success.
                order_client_id (str): Filter by specific `order_client_id`.
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
        return self.session.get(f'{self.api_url}/recurrent_charge',
                                params=params,
                                headers=headers)

    def accept_recurrent_charge(self,
                                charge_id: str,
                                payload: dict = None,
                                headers: dict = None) -> httpx.Response:
        ''' Accepts specific recurrent charge.
            Args:
                charge_id (str): ID of the recurrent charge.
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
        ''' Declines specific recurrent charge.
            Args:
                charge_id (str): ID of the recurrent charge.
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
        ''' Activates specific recurrent charge.
            Args:
                charge_id (str): ID of the recurrent charge.
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
        ''' Cancels specific recurrent charge.
            Args:
                charge_id (str): ID of the recurrent charge.
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
