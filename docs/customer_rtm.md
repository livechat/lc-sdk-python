# Class: CustomerRTM

## Index

### Initialize client

* [initialize client](customer_rtm.md#get_client)


## Initialize client

###  get_client

\+ **CustomerRTM.get_client**(`token`:TBD, `license`: TBD): *TBD*

*Defined in TBD

**Parameters:**

Name | Type |
------ | ------ |
`token` |  TBD |
`license` |  TBD |

**Returns:** *TBD*

### Methods

* [accept_greeting](customer_rtm.md#accept_greeting)
* [cancel_greeting](customer_rtm.md#cancel_greeting)
* [deactivate_chat](customer_rtm.md#deactivate_chat)
* [delete_chat_properties](customer_rtm.md#delete_chat_properties)
* [delete_event_properties](customer_rtm.md#delete_event_properties)
* [delete_thread_properties](customer_rtm.md#delete_thread_properties)
* [get_chat](customer_rtm.md#get_chat)
* [get_customer](customer_rtm.md#get_customer)
* [get_form](customer_rtm.md#get_form)
* [get_predicted_agent](customer_rtm.md#get_predicted_agent)
* [get_url_info](customer_rtm.md#get_url_info)
* [list_chats](customer_rtm.md#listchats)
* [list_group_statuses](customer_rtm.md#list_group_statuses)
* [list_threads](customer_rtm.md#listthreads)
* [login](customer_rtm.md#login)
* [mark_events_as_seen](customer_rtm.md#mark_events_as_seen)
* [resume_chat](customer_rtm.md#resume_chat)
* [send_event](customer_rtm.md#send_event)
* [send_rich_message_postback](customer_rtm.md#send_rich_message_postback)
* [send_sneak_peek](customer_rtm.md#send_sneak_peek)
* [set_customer_session_fields](customer_rtm.md#set_customer_session_fields)
* [start_chat](customer_rtm.md#start_chat)
* [update_chat_properties](customer_rtm.md#update_chat_properties)
* [update_customer](customer_rtm.md#update_customer)
* [update_event_properties](customer_rtm.md#update_event_properties)
* [update_thread_properties](customer_rtm.md#update_thread_properties)

## Methods

###  accept_greeting

▸ **accept_greeting**(`greeting_id`:  TBD, `unique_id`:  TBD): *TBD*

*Defined in TBD*

Marks an incoming greeting as seen.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`greeting_id` |  TBD | number representing type of a greeting |
`unique_id` |  TBD | specific greeting event ID  |

**Returns:** *TBD*

___

###  cancel_greeting

▸ **cancel_greeting**(`unique_id`:  TBD): *TBD*

*Defined in TBD*

Cancels a greeting (an invitation to the chat).
For example, Customers could cancel greetings by minimalizing the chat widget with a greeting.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`unique_id` |  TBD | specific greeting ID  |

**Returns:** *TBD*


###  deactivate_chat

▸ **deactivate_chat**(`chat_id`:  TBD): *TBD*

*Defined in TBD*

Deactivates a chat by closing the currently open thread. Sending messages to this thread will no longer be possible.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chat_id` |  TBD | chat ID to deactivate  |

**Returns:** *TBD*

___

###  delete_chat_properties

▸ **delete_chat_properties**(`chat_id`:  TBD, `properties`: TBD)): *TBD*

*Defined in TBD*

Deletes chat properties

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chat_id` |  TBD | chat to delete properties |
`properties` | TBD | properties to delete  |

**Returns:** *TBD*

___

###  delete_event_properties

▸ **delete_event_properties**(`chat_id`:  TBD, `thread_id`:  TBD, `event_id`:  TBD, `properties`: TBD)): *TBD*

*Defined in TBD*

Deletes event properties

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chat_id` |  TBD | chat ID of event to delete |
`thread_id` |  TBD | thread ID of event to delete |
`event_id` |  TBD | event to delete properties |
`properties` | TBD | properties to delete  |

**Returns:** *TBD*

___

###  delete_thread_properties

▸ **delete_thread_properties**(`chat_id`:  TBD, `thread_id`:  TBD, `properties`: TBD): *TBD*

*Defined in TBD*

Deletes thread properties

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chat_id` | TBD | chat ID of thread to delete |
`thread_id` |  TBD | thread to delete properties |
`properties` | TBD | properties to delete  |

**Returns:** *TBD*

___

###  get_chat

▸ **get_chat**(`chat_id`:  TBD, `thread_id`:  TBD): *TBD*

*Defined in TBD*

It returns a thread that the current Customer has access to in a given chat.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chat_id` |  TBD | ID of a chat to get |
`thread_id` |  TBD | thread ID to get (if not provided, last thread is returned)  |

**Returns:** *TBD*

___

###  get_customer

▸ **get_customer**(): *TBD*

*Defined in TBD*

Returns the info about the Customer requesting it.

**Returns:** *TBD*

___

###  get_form

▸ **getForm**(`group_id`:  TBD, `type`:  TBD): *TBD*

*Defined in TBD*

Returns an empty ticket form of a prechat or postchat survey.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`group_id` |  TBD | = group id to get form for |
`type` |  TBD | prechat or postchat  |

**Returns:** *TBD*

___

###  get_predicted_agent

▸ **get_predicted_agent**(): *TBD*

*Defined in TBD*

Gets the predicted Agent - the one the Customer will chat with when the chat starts.
To use this method, the Customer needs to be logged in, which can be done via the login method.

**Returns:** *TBD*

___

###  get_url_info

▸ **get_url_info**(`url`:  TBD): *TBD*

*Defined in TBD*

It returns the info on a given URL.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`url` |  TBD | URL to get info about  |

**Returns:** *TBD*

___

###  list_chats

▸ **list_chats**(`opts`: TBD): *TBD*

*Defined in TBD*

It returns summaries of the chats a Customer participated in.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`opts` | TBD | set of filters and pagination to limit returned entries  |

**Returns:** *TBD*


###  list_group_statuses

▸ **list_group_statuses**(`param`:  TBD): *TBD*

*Defined in TBD*

Lists statuses of groups.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`param` |  TBD | either boolean switch for all groups or list of group ID's to check  |

**Returns:** *TBD*


###  list_threads

▸ **list_threads**(`chat_id`: TBD, `opts`: TBD): *TBD*

*Defined in TBD*

Returns threads that the current Customer has access to in a given chat.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chat_id` |  TBD | chat ID to get threads from |
`opts` | TBD | additional options like pagination and sorting  |

**Returns:** *TBD*

___

###  login

▸ **login**(`loginData`:  TBD): *TBD*

*Defined in TBD*

It returns the initial state of the current Customer.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`loginData` | TBD | OAuth token form the Customer's account or full object with login parameters  |

**Returns:** *TBD*

___

###  mark_events_as_seen

▸ **mark_events_as_seen**(`chat_id`:  TBD, `seen_up_to`:  TBD): *TBD*

*Defined in TBD*

Marks events as seen by Agent.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chat_id` |  TBD | chat to mark events |
`seen_up_to` |  TBD | date up to which mark events  |

**Returns:** *TBD*


###  resume_chat

▸ **resume_chat**(`param`:   TBD): *TBD*

*Defined in TBD*

Restarts an archived chat

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`param` | TBD | either string ID of a chat to activate or full initial chat object  |

**Returns:** *TBD*


###  send_event

▸ **send_event**(`chat_id`:  TBD, `event`: TBD, `attach_to_last_thread`: TBD): *TBD*

*Defined in TBD*

Sends an Event object. Use this method to send a message by specifing the Message event type in the request.
It's possible to write to a chat without joining it. The user sending an event will be automatically added to the chat
with the present parameter set to false.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chat_id` |  TBD | chat to send event to |
`event` | TBD | Event object |
`attach_to_last_thread` |  TBD | if True, adds event to last inactive thread  |

**Returns:** *TBD*

___

###  send_rich_message_postback

▸ **send_rich_message_postback**(`opts`:  TBD): * TBD*

*Defined in  TBD*

Sends postback for rich message

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`opts` |  TBD | postback data  |

**Returns:** * TBD*

___

###  send_sneak_peek

▸ **send_sneak_peek**(`chat_id`:  TBD, `sneak_peek_text`:  TBD): * TBD*

*Defined in  TBD*

Sends a sneak peek to a chat.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chat_id` |  TBD | chat to send sneak peek to |
`sneak_peek_text` |  TBD| text to sneak peek  |

**Returns:** * TBD*

___

###  set_customer_session_fields

▸ **set_customer_session_fields**(`session_fields`: TBD): *TBD*

*Defined in TBD*

Sets session fields for Customer.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`session_fields` |  TBD| fields to set in form of object enclosed key:value pairs  |

**Returns:** *TBD*

___

###  start_chat

▸ **start_chat**(`opts`: TBD): *TBD*

*Defined in TBD*

Starts a chat

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`opts` | TBD | options like initial chat data or continuous switch  |

**Returns:** *TBD*


###  update_chat_properties

▸ **update_chat_properties**(`chat_id`: TBD, `properties`: TBD): *TBD*

*Defined in TBD*

Updates chat properties

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chat_id` | TBD | chat to update properties |
`properties` | TBD | properties to update  |

**Returns:** *TBD*

___

###  update_customer

▸ **update_customer**(`opts`: TBD): *TBD*

*Defined in TBD*

Updates Customer's properties.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`opts` | TBD | properties to update  |

**Returns:** *TBD*

___

###  update_event_properties

▸ **update_event_properties**(`chat_id`: TBD, `thread_id`: TBD, `event_id`: TBD, `properties`: TBD): *TBD*

*Defined in TBD*

Updates event properties

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chat_id` | TBD | chat ID of event to update |
`thread_id` | TBD | thread ID of event to update |
`event_id` | TBD| event to update properties |
`properties` | TBD| properties to update  |

**Returns:** *TBD*

___

###  update_thread_properties

▸ **update_thread_properties**(`chat_id`: TBD, `thread_id`: TBD, `properties`: TBD): *TBD*

*Defined in TBD*

Updates thread properties

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chat_id` | TBD | chat ID of thread to update |
`thread_id` | TBD | thread to update properties |
`properties` | TBD | properties to update  |

**Returns:** *TBD*