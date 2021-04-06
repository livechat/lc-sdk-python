''' Tests for helper methods from livechat.utils. '''

import pytest

from livechat.utils import helpers


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
