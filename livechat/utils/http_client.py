''' Base module with HTTP client class for session, sending requests and headers
    manipulation. '''

import httpx

from livechat.utils.httpx_logger import HttpxLogger


class HttpClient:
    ''' HTTP client class for session, sending requests and headers manipulation. '''
    def __init__(self,
                 token: str,
                 base_url: str,
                 http2: bool,
                 proxies=None,
                 verify: bool = True,
                 disable_logging: bool = False,
                 timeout: float = httpx.Timeout(15)):
        logger = HttpxLogger(disable_logging=disable_logging)
        self.base_url = base_url
        self.session = httpx.Client(http2=http2,
                                    headers={'Authorization': token},
                                    event_hooks={
                                        'request': [logger.log_request],
                                        'response': [logger.log_response]
                                    },
                                    proxies=proxies,
                                    verify=verify,
                                    timeout=timeout)

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
