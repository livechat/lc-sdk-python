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
        return action_to_data_class_mapping_v_33[self.action]


# Chats


@dataclass
class IncomingChat:
    chat: dict
    transferred_from: dict = None


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
    chat_id: str
    reason: str
    transferred_to: dict
    thread_id: str = None
    requester_id: str = None
    queue: dict = None


# Chat users


@dataclass
class UserAddedToChat:
    chat_id: str
    reason: str
    requester_id: str
    thread_id: str = None
    user_type: str = None
    user: dict = None


@dataclass
class UserRemovedFromChat:
    chat_id: str
    user_id: str
    reason: str
    requester_id: str
    thread_id: str = None
    user_type: str = None


# Events


@dataclass
class IncomingEvent:
    chat_id: str
    thread_id: str
    event: dict = None


@dataclass
class EventUpdated:
    chat_id: str
    thread_id: str
    event: dict


@dataclass
class IncomingRichMessagePostback:
    user_id: str
    chat_id: str
    thread_id: str
    event_id: str
    postback: dict


# Properties


@dataclass
class ChatPropertiesUpdated:
    chat_id: str
    properties: dict


@dataclass
class ChatPropertiesDeleted:
    chat_id: str
    properties: dict


@dataclass
class ThreadPropertiesUpdated:
    chat_id: str
    thread_id: str
    properties: dict


@dataclass
class ThreadPropertiesDeleted:
    chat_id: str
    thread_id: str
    properties: dict


@dataclass
class EventPropertiesUpdated:
    chat_id: str
    thread_id: str
    event_id: str
    properties: dict


@dataclass
class EventPropertiesDeleted:
    chat_id: str
    thread_id: str
    event_id: str
    properties: dict


# Thread tags


@dataclass
class ThreadTagged:
    chat_id: str
    thread_id: str
    tag: str


@dataclass
class ThreadUntagged:
    chat_id: str
    thread_id: str
    tag: str


# Status


@dataclass
class RoutingStatusSet:
    agent_id: str
    status: str


@dataclass
class AgentDeleted:
    id: str


# Customers


@dataclass
class IncomingCustomer:
    customer: dict


@dataclass
class CustomerSessionFieldsUpdated:
    id: str
    session_fields: list
    active_chat: dict = None


# Other


@dataclass
class EventsMarkedAsSeen:
    user_id: str
    chat_id: str
    seen_up_to: str


# Webhook's action mapping to coressponding payload's data class definition
action_to_data_class_mapping_v_33 = {
    'incoming_chat': IncomingChat,
    'chat_deactivated': ChatDeactivated,
    'chat_access_granted': ChatAccessGranted,
    'chat_access_revoked': ChatAccessRevoked,
    'chat_transferred': ChatTransferred,
    'user_added_to_chat': UserAddedToChat,
    'user_removed_from_chat': UserRemovedFromChat,
    'incoming_event': IncomingEvent,
    'event_updated': EventUpdated,
    'incoming_rich_message_postback': IncomingRichMessagePostback,
    'chat_properties_updated': ChatPropertiesUpdated,
    'chat_properties_deleted': ChatPropertiesDeleted,
    'thread_properties_updated': ThreadPropertiesUpdated,
    'thread_properties_deleted': ThreadPropertiesDeleted,
    'event_properties_updated': EventPropertiesUpdated,
    'event_properties_deleted': EventPropertiesDeleted,
    'thread_tagged': ThreadTagged,
    'thread_untagged': ThreadUntagged,
    'routing_status_set': RoutingStatusSet,
    'agent_deleted': AgentDeleted,
    'incoming_customer': IncomingCustomer,
    'customer_session_fields_updated': CustomerSessionFieldsUpdated,
    'events_marked_as_seen': EventsMarkedAsSeen,
}
