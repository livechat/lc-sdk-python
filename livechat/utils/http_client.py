''' Base module with HTTP client class for session, sending requests and headers
    manipulation. '''

from typing import Union

import httpx

from livechat.utils.httpx_logger import HttpxLogger
from livechat.utils.structures import AccessToken


class HttpClient:
    ''' HTTP client class for session, sending requests and headers manipulation. '''
    def __init__(self,
                 token: Union[AccessToken, str],
                 base_url: str,
                 http2: bool,
                 proxies=None,
                 verify: bool = True):
        logger = HttpxLogger()
        self.base_url = base_url
        self.session = httpx.Client(http2=http2,
                                    headers={'Authorization': str(token)},
                                    event_hooks={
                                        'request': [logger.log_request],
                                        'response': [logger.log_response]
                                    },
                                    proxies=proxies,
                                    verify=verify)

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
