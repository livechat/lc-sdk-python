''' Module containing structures. '''

from dataclasses import dataclass
from enum import Enum


class RtmResponse:
    ''' RTM response structure class. '''
    def __init__(self, rtm_response: dict):
        self.rtm_response = rtm_response

    @property
    def request_id(self) -> str:
        ''' `request_id` from the RTM response. '''
        return self.rtm_response.get('request_id')

    @property
    def action(self) -> str:
        ''' `action` from the RTM response. '''
        return self.rtm_response.get('action')

    @property
    def type(self) -> str:
        ''' Response `type` from the RTM response. '''
        return self.rtm_response.get('type')

    @property
    def success(self) -> bool:
        ''' Response `success` state from the RTM response. '''
        return self.rtm_response.get('success')

    @property
    def payload(self) -> dict:
        ''' `payload` from the RTM response. '''
        return self.rtm_response.get('payload')


class TokenType(Enum):
    ''' Token type enum class. '''
    BEARER = 'Bearer'
    BASIC = 'Basic'


@dataclass
class AccessToken:
    ''' Access token structure class. '''
    token: str
    scheme: TokenType

    def __str__(self) -> str:
        return f'{self.scheme.value} {self.token}'
