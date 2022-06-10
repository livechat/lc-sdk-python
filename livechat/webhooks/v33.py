''' API v3.3 webhooks data classes. '''

from dataclasses import dataclass

# pylint: disable=missing-class-docstring


@dataclass
class WebhookV33:
    webhook_id: str
    secret_key: str
    action: str
    license_id: int
    additional_data: dict
    payload: dict

    def payload_data_class(self):
        ''' Returns payload's data class for webhook's action. '''
        return {
            'incoming_chat': IncomingChat,
            'chat_deactivated': ChatDeactivated,
            'chat_access_granted': ChatAccessGranted,
            'chat_access_revoked': ChatAccessRevoked,
            'chat_transferred': ChatTransferred,
            'routing_status_set': RoutingStatusSet,
        }[self.action]


# Chats


@dataclass
class IncomingChat:
    chat: dict


@dataclass
class ChatDeactivated:
    chat_id: str
    thread_id: str
    user_id: str = None


# Chat access


@dataclass
class ChatAccessGranted:
    id: str
    access: dict


@dataclass
class ChatAccessRevoked:
    id: str
    access: dict


@dataclass
class ChatTransferred:
    id: str
    access: dict


# Status


@dataclass
class RoutingStatusSet:
    agent_id: str
    status: str
