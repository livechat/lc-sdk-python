''' Tests for helper methods from utils. '''

import pytest

from utils import helpers


@pytest.mark.parametrize(
    'url,origin', [('wss://api.labs.livechatinc.com/v3.3/agent/rtm/ws',
                    'https://secure.labs.livechatinc.com'),
                   ('wss://api.staging.livechatinc.com/v3.3/agent/rtm/ws',
                    'https://secure-lc.livechatinc.com'),
                   ('wss://api.livechatinc.com/v3.3/agent/rtm/ws',
                    'https://secure.livechatinc.com')])
def test_parse_url_and_return_origin(url, origin):
    ''' Test if `parse_url_and_return_origin` method returns correct origin
        basing on provided URL. '''
    assert helpers.parse_url_and_return_origin(url) == origin


@pytest.mark.parametrize('parameters,payload', [({
    'test': 'test',
    'test1': 'test1'
}, {
    'test': 'test',
    'test1': 'test1'
}),
                                                ({
                                                    'test': 'test',
                                                    'test1': 'test1',
                                                    'self': 1
                                                }, {
                                                    'test': 'test',
                                                    'test1': 'test1'
                                                }),
                                                ({
                                                    'test': 'test',
                                                    'test1': 'test1',
                                                    'payload': 0
                                                }, {
                                                    'test': 'test',
                                                    'test1': 'test1'
                                                }),
                                                ({
                                                    'test': 'test',
                                                    'test1': 'test1',
                                                    'self': 1,
                                                    'payload': 0
                                                }, {
                                                    'test': 'test',
                                                    'test1': 'test1'
                                                }),
                                                ({
                                                    'test': 'test',
                                                    'test1': None,
                                                    'self': 1,
                                                    'payload': 0
                                                }, {
                                                    'test': 'test'
                                                }),
                                                ({
                                                    'test': None,
                                                    'test1': None
                                                }, {}),
                                                ({
                                                    'test': None,
                                                    'self': 'test'
                                                }, {})])
def test_prepare_payload(parameters, payload):
    ''' Test if `prepare_payload` method returns proper payload basing on
        provided parameters. '''
    assert helpers.prepare_payload(parameters) == payload
