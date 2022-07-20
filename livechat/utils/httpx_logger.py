'''
Logger for httpx requests.
'''

import json
import logging
from datetime import datetime

import httpx


class HttpxLogger:
    ''' Logger for httpx requests. '''
    def __init__(self):
        logging.basicConfig()
        self.logger = logging.getLogger()

    def log_request(self, request: httpx.Request):
        ''' Log request details. '''
        request_send_time = datetime.now().strftime('%Y-%m-%d, %H:%M:%S.%f')
        self.logger.info(
            f'\nREQUEST:\n {request.method} {request.url}\n PARAMS:\n {request.stream.read().decode("utf-8")}'
        )
        self.logger.debug(
            f'\n SEND TIME: {request_send_time}\n HEADERS:\n {json.dumps(dict(request.headers.items()), indent=4)}'
        )

    def log_response(self, response: httpx.Response):
        ''' Log repsonse details. '''
        response.read()
        self.logger.info(
            f'\nRESPONSE:\n STATUS {response.status_code}\n{json.dumps(response.json(), indent=4)}'
        )
        self.logger.debug(f'\n DURATION: {response.elapsed.total_seconds()} s')
