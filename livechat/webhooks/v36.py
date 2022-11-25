''' API v3.6 webhooks data classes. '''

from dataclasses import dataclass

# pylint: disable=missing-class-docstring


@dataclass
class WebhookV36:
    webhook_id: str
    secret_key: str
    action: str
    organization_id: str
    additional_data: dict
    payload: dict

    def payload_data_class(self):
        ''' Returns payload's data class for webhook's action. '''
        return action_to_data_class_mapping_v_36[self.action]


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
class ChatAccessUpdated:
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


# Customers


@dataclass
class IncomingCustomer:
    customer: dict


@dataclass
class CustomerSessionFieldsUpdated:
    id: str
    session_fields: list
    active_chat: dict = None


# Configuration


@dataclass
class AgentCreated:
    id: str
    name: str
    awaiting_approval: bool
    role: str = None
    avatar: str = None
    job_title: str = None
    mobile: str = None
    max_chats_count: int = None
    groups: list = None
    notifications: list = None
    email_subscriptions: list = None
    work_scheduler: dict = None


@dataclass
class AgentApproved:
    id: str


@dataclass
class AgentUpdated:
    id: str
    name: str = None
    role: str = None
    avatar: str = None
    job_title: str = None
    mobile: str = None
    max_chats_count: int = None
    groups: list = None
    notifications: list = None
    email_subscriptions: list = None
    work_scheduler: dict = None


@dataclass
class AgentSuspended:
    id: str


@dataclass
class AgentUnsuspended:
    id: str


@dataclass
class AgentDeleted:
    id: str


@dataclass
class AutoAccessAdded:
    id: str
    description: str
    access: dict
    conditions: dict
    next_id: str = None


@dataclass
class AutoAccessUpdated:
    id: str
    description: str = None
    access: dict = None
    conditions: dict = None
    next_id: str = None


@dataclass
class AutoAccessDeleted:
    id: str


@dataclass
class BotCreated:
    id: str
    name: str
    default_group_priority: str
    owner_client_id: str
    avatar: str = None
    max_chats_count: int = None
    groups: list = None
    work_scheduler: dict = None
    timezone: str = None
    job_title: str = None


@dataclass
class BotUpdated:
    id: str
    name: str = None
    avatar: str = None
    max_chats_count: int = None
    default_group_priority: str = None
    groups: list = None
    work_scheduler: dict = None
    timezone: str = None
    job_title: str = None


@dataclass
class BotDeleted:
    id: str


@dataclass
class GroupCreated:
    id: int
    name: str
    language_code: str
    agent_priorities: dict


@dataclass
class GroupDeleted:
    id: str


@dataclass
class GroupUpdated:
    id: int
    name: str = None
    language_code: str = None
    agent_priorities: dict = None


@dataclass
class TagCreated:
    name: str
    author_id: str
    created_at: str
    group_ids: list


@dataclass
class TagDeleted:
    name: str


@dataclass
class TagUpdated:
    name: str
    group_ids: list
    author_id: str = None
    created_at: str = None


# Other


@dataclass
class EventsMarkedAsSeen:
    user_id: str
    chat_id: str
    seen_up_to: str


# Webhook's action mapping to coressponding payload's data class definition
action_to_data_class_mapping_v_36 = {
    'incoming_chat': IncomingChat,
    'chat_deactivated': ChatDeactivated,
    'chat_access_updated': ChatAccessUpdated,
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
    'incoming_customer': IncomingCustomer,
    'customer_session_fields_updated': CustomerSessionFieldsUpdated,
    'agent_created': AgentCreated,
    'agent_approved': AgentApproved,
    'agent_updated': AgentUpdated,
    'agent_suspended': AgentSuspended,
    'agent_unsuspended': AgentUnsuspended,
    'agent_deleted': AgentDeleted,
    'auto_access_added': AutoAccessAdded,
    'auto_access_updated': AutoAccessUpdated,
    'auto_access_deleted': AutoAccessDeleted,
    'bot_created': BotCreated,
    'bot_updated': BotUpdated,
    'bot_deleted': BotDeleted,
    'group_created': GroupCreated,
    'group_deleted': GroupDeleted,
    'group_updated': GroupUpdated,
    'tag_created': TagCreated,
    'tag_deleted': TagDeleted,
    'tag_updated': TagUpdated,
    'events_marked_as_seen': EventsMarkedAsSeen,
}
