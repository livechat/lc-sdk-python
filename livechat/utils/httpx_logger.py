'''
Logger for httpx requests.
'''

import json
import logging
from datetime import datetime


class HttpxLogger:
    ''' Logger for httpx requests. '''
    def __init__(self):
        logging.basicConfig()
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

    def log_request(self, request):
        ''' Log request details. '''
        request_send_time = datetime.now().strftime('%Y-%m-%d, %H:%M:%S.%f')
        self.logger.info(
            f'\nREQUEST:\n {request.method} {request.url}\n SEND TIME: {request_send_time}\n PARAMS:\n {request.content.decode("utf-8")}'
        )
        self.logger.debug(f'\nHEADERS:\n {dict(request.headers.items())}')

    def log_response(self, response):
        ''' Log repsonse details. '''
        request = response.request
        response.read()
        self.logger.info(
            f'\nRESPONSE:\n {request.method} {request.url} - Status {response.status_code}\n Duration: {response.elapsed.total_seconds()} s \n {json.dumps(response.json(), indent=4)}'
        )
