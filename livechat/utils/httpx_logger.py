'''
Logger for httpx requests.
'''

import json

import httpx
from loguru import logger


class HttpxLogger:
    ''' Logger for httpx requests. '''
    MAX_CONTENT_LENGTH_TO_LOG = 1000

    def __init__(self, disable_logging: bool = False):
        self.disable_logging = disable_logging

    def log_request(self, request: httpx.Request) -> None:
        ''' Logs request details. '''
        if not self.disable_logging:
            request.read()
            try:
                request_params = json.dumps(
                    json.loads(request.content),
                    indent=4,
                )
            except json.decoder.JSONDecodeError:
                request_params = request.content.decode('utf-8')
            except ValueError:
                request_params = request.content  # to avoid error when request contains binary data
            request_headers = json.dumps(
                dict(request.headers.items()),
                indent=4,
            )
            if len(request_params) > self.MAX_CONTENT_LENGTH_TO_LOG:
                request_params = f'{request_params[:self.MAX_CONTENT_LENGTH_TO_LOG]}... (Truncated)'

            request_debug = f'Request params:\n{request_params}\n' \
                            f'Request headers:\n{request_headers}'

            logger.info(f'{request.method} request to: {request.url}')
            logger.debug(request_debug)

    def log_response(self, response: httpx.Response) -> None:
        ''' Logs response details. '''
        if not self.disable_logging:
            response.read()
            try:
                response_content = json.dumps(response.json(), indent=4)
            except ValueError:
                response_content = response.text  # to avoid error when response contains binary data
            response_debug = f'Response duration: {response.elapsed.total_seconds()} second(s)\n' \
                            f'Response content:\n{response_content}'

            logger.info(f'Response status code: {response.status_code}')
            logger.debug(response_debug)
