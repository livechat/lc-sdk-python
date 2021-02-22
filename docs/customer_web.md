# Class: RTM

## Index

### Initialize client

* [initialize client](customer_rtm.md#get_client)


## Initialize client

###  get_client

\+ **CustomerRTM.get_client**(`token`:string, `license`: string): *TBD*

*Defined in TBD

**Parameters:**

Name | Type |
------ | ------ |
`token` | string |
`license` | string |

**Returns:** *[RTM](_src_customer_rtm_.rtm.md)*



## Methods

###  acceptGreeting

▸ **acceptGreeting**(`greeting_id`: number, `unique_id`: string): *Promise‹[EmptyResponse](../interfaces/_src_customer_structures_.emptyresponse.md)›*

*Defined in [src/customer/rtm.ts:348](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/customer/rtm.ts#L348)*

Marks an incoming greeting as seen.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`greeting_id` | number | number representing type of a greeting |
`unique_id` | string | specific greeting event ID  |

**Returns:** *Promise‹[EmptyResponse](../interfaces/_src_customer_structures_.emptyresponse.md)›*

___

###  cancelGreeting

▸ **cancelGreeting**(`unique_id`: string): *Promise‹[EmptyResponse](../interfaces/_src_customer_structures_.emptyresponse.md)›*

*Defined in [src/customer/rtm.ts:357](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/customer/rtm.ts#L357)*

Cancels a greeting (an invitation to the chat).
For example, Customers could cancel greetings by minimalizing the chat widget with a greeting.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`unique_id` | string | specific greeting ID  |

**Returns:** *Promise‹[EmptyResponse](../interfaces/_src_customer_structures_.emptyresponse.md)›*

___

###  checkGoals

▸ **checkGoals**(`session_fields`: object[], `group_id`: number, `page_url`: number): *Promise‹[EmptyResponse](../interfaces/_src_customer_structures_.emptyresponse.md)›*

*Defined in [src/customer/rtm.ts:302](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/customer/rtm.ts#L302)*

Customer can use this method to trigger checking if goals were achieved.
Then, Agents receive the information. You should call this method to provide goals
parameters for the server when the customers limit is reached. Works only for offline Customers.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`session_fields` | object[] | object enclosed key:value pairs |
`group_id` | number | group id to check goals in |
`page_url` | number | page URL  |

**Returns:** *Promise‹[EmptyResponse](../interfaces/_src_customer_structures_.emptyresponse.md)›*

___

###  connect

▸ **connect**(): *Promise‹void›*

*Inherited from [RTMAPI](_src_internal_index_.rtmapi.md).[connect](_src_internal_index_.rtmapi.md#connect)*

*Defined in [src/internal/index.ts:72](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/internal/index.ts#L72)*

**Returns:** *Promise‹void›*

___

###  deactivateChat

▸ **deactivateChat**(`chat_id`: string): *Promise‹[EmptyResponse](../interfaces/_src_customer_structures_.emptyresponse.md)›*

*Defined in [src/customer/rtm.ts:100](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/customer/rtm.ts#L100)*

Deactivates a chat by closing the currently open thread. Sending messages to this thread will no longer be possible.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chat_id` | string | chat ID to deactivate  |

**Returns:** *Promise‹[EmptyResponse](../interfaces/_src_customer_structures_.emptyresponse.md)›*

___

###  deleteChatProperties

▸ **deleteChatProperties**(`chat_id`: string, `properties`: [Properties](../interfaces/_src_objects_index_.properties.md)): *Promise‹[EmptyResponse](../interfaces/_src_customer_structures_.emptyresponse.md)›*

*Defined in [src/customer/rtm.ts:152](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/customer/rtm.ts#L152)*

Deletes chat properties

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chat_id` | string | chat to delete properties |
`properties` | [Properties](../interfaces/_src_objects_index_.properties.md) | properties to delete  |

**Returns:** *Promise‹[EmptyResponse](../interfaces/_src_customer_structures_.emptyresponse.md)›*

___

###  deleteEventProperties

▸ **deleteEventProperties**(`chat_id`: string, `thread_id`: string, `event_id`: string, `properties`: [Properties](../interfaces/_src_objects_index_.properties.md)): *Promise‹[EmptyResponse](../interfaces/_src_customer_structures_.emptyresponse.md)›*

*Defined in [src/customer/rtm.ts:212](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/customer/rtm.ts#L212)*

Deletes event properties

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chat_id` | string | chat ID of event to delete |
`thread_id` | string | thread ID of event to delete |
`event_id` | string | event to delete properties |
`properties` | [Properties](../interfaces/_src_objects_index_.properties.md) | properties to delete  |

**Returns:** *Promise‹[EmptyResponse](../interfaces/_src_customer_structures_.emptyresponse.md)›*

___

###  deleteThreadProperties

▸ **deleteThreadProperties**(`chat_id`: string, `thread_id`: string, `properties`: [Properties](../interfaces/_src_objects_index_.properties.md)): *Promise‹[EmptyResponse](../interfaces/_src_customer_structures_.emptyresponse.md)›*

*Defined in [src/customer/rtm.ts:176](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/customer/rtm.ts#L176)*

Deletes thread properties

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chat_id` | string | chat ID of thread to delete |
`thread_id` | string | thread to delete properties |
`properties` | [Properties](../interfaces/_src_objects_index_.properties.md) | properties to delete  |

**Returns:** *Promise‹[EmptyResponse](../interfaces/_src_customer_structures_.emptyresponse.md)›*

___

###  getChat

▸ **getChat**(`chat_id`: string, `thread_id?`: undefined | string): *Promise‹[GetChatResponse](../interfaces/_src_customer_structures_.getchatresponse.md)›*

*Defined in [src/customer/rtm.ts:75](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/customer/rtm.ts#L75)*

It returns a thread that the current Customer has access to in a given chat.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chat_id` | string | ID of a chat to get |
`thread_id?` | undefined &#124; string | thread ID to get (if not provided, last thread is returned)  |

**Returns:** *Promise‹[GetChatResponse](../interfaces/_src_customer_structures_.getchatresponse.md)›*

___

###  getCustomer

▸ **getCustomer**(): *Promise‹[CustomerParameters](../interfaces/_src_customer_structures_.customerparameters.md)›*

*Defined in [src/customer/rtm.ts:280](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/customer/rtm.ts#L280)*

Returns the info about the Customer requesting it.

**Returns:** *Promise‹[CustomerParameters](../interfaces/_src_customer_structures_.customerparameters.md)›*

___

###  getForm

▸ **getForm**(`group_id`: number, `type`: string): *Promise‹[GetFormResponse](../interfaces/_src_customer_structures_.getformresponse.md)›*

*Defined in [src/customer/rtm.ts:314](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/customer/rtm.ts#L314)*

Returns an empty ticket form of a prechat or postchat survey.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`group_id` | number | = group id to get form for |
`type` | string | prechat or postchat  |

**Returns:** *Promise‹[GetFormResponse](../interfaces/_src_customer_structures_.getformresponse.md)›*

___

###  getPredictedAgent

▸ **getPredictedAgent**(): *Promise‹[GetPredictedAgentResponse](../interfaces/_src_customer_structures_.getpredictedagentresponse.md)›*

*Defined in [src/customer/rtm.ts:322](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/customer/rtm.ts#L322)*

Gets the predicted Agent - the one the Customer will chat with when the chat starts.
To use this method, the Customer needs to be logged in, which can be done via the login method.

**Returns:** *Promise‹[GetPredictedAgentResponse](../interfaces/_src_customer_structures_.getpredictedagentresponse.md)›*

___

###  getURLInfo

▸ **getURLInfo**(`url`: string): *Promise‹[GetURLInfoResponse](../interfaces/_src_customer_structures_.geturlinforesponse.md)›*

*Defined in [src/customer/rtm.ts:330](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/customer/rtm.ts#L330)*

It returns the info on a given URL.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`url` | string | URL to get info about  |

**Returns:** *Promise‹[GetURLInfoResponse](../interfaces/_src_customer_structures_.geturlinforesponse.md)›*

___

###  listChats

▸ **listChats**(`opts?`: [ListChatParameters](../interfaces/_src_agent_structures_.listchatparameters.md)): *Promise‹[ListChatsResponse](../interfaces/_src_customer_structures_.listchatsresponse.md)›*

*Defined in [src/customer/rtm.ts:57](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/customer/rtm.ts#L57)*

It returns summaries of the chats a Customer participated in.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`opts?` | [ListChatParameters](../interfaces/_src_agent_structures_.listchatparameters.md) | set of filters and pagination to limit returned entries  |

**Returns:** *Promise‹[ListChatsResponse](../interfaces/_src_customer_structures_.listchatsresponse.md)›*

___

###  listGroupProperties

▸ **listGroupProperties**(`license_id`: number, `group_id`: number, `namespace?`: undefined | string, `name?`: undefined | string): *Promise‹[Properties](../interfaces/_src_objects_index_.properties.md)›*

*Defined in [src/customer/rtm.ts:247](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/customer/rtm.ts#L247)*

Returns the properties of a given group. It only returns the properties a Customer has access to.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`license_id` | number | ID of license to return properties of |
`group_id` | number | ID of group to return properties of |
`namespace?` | undefined &#124; string | property namespace |
`name?` | undefined &#124; string | property name  |

**Returns:** *Promise‹[Properties](../interfaces/_src_objects_index_.properties.md)›*

___

###  listGroupStatuses

▸ **listGroupStatuses**(`param`: boolean | number[]): *Promise‹[ListGroupStatusesResponse](../interfaces/_src_customer_structures_.listgroupstatusesresponse.md)›*

*Defined in [src/customer/rtm.ts:288](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/customer/rtm.ts#L288)*

Lists statuses of groups.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`param` | boolean &#124; number[] | either boolean switch for all groups or list of group ID's to check  |

**Returns:** *Promise‹[ListGroupStatusesResponse](../interfaces/_src_customer_structures_.listgroupstatusesresponse.md)›*

___

###  listLicenseProperties

▸ **listLicenseProperties**(`license_id`: number, `namespace?`: undefined | string, `name?`: undefined | string): *Promise‹[Properties](../interfaces/_src_objects_index_.properties.md)›*

*Defined in [src/customer/rtm.ts:232](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/customer/rtm.ts#L232)*

Returns the properties of a given license. It only returns the properties a Customer has access to.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`license_id` | number | ID of license to return properties of |
`namespace?` | undefined &#124; string | property namespace |
`name?` | undefined &#124; string | property name  |

**Returns:** *Promise‹[Properties](../interfaces/_src_objects_index_.properties.md)›*

___

###  listThreads

▸ **listThreads**(`chat_id`: string, `opts?`: [ListThreadsParameters](../interfaces/_src_agent_structures_.listthreadsparameters.md)): *Promise‹[ListThreadsResponse](../interfaces/_src_customer_structures_.listthreadsresponse.md)›*

*Defined in [src/customer/rtm.ts:66](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/customer/rtm.ts#L66)*

Returns threads that the current Customer has access to in a given chat.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chat_id` | string | chat ID to get threads from |
`opts?` | [ListThreadsParameters](../interfaces/_src_agent_structures_.listthreadsparameters.md) | additional options like pagination and sorting  |

**Returns:** *Promise‹[ListThreadsResponse](../interfaces/_src_customer_structures_.listthreadsresponse.md)›*

___

###  login

▸ **login**(`loginData`: string | [LoginRequest](../interfaces/_src_customer_structures_.loginrequest.md)): *Promise‹[LoginResponse](../interfaces/_src_customer_structures_.loginresponse.md)›*

*Defined in [src/customer/rtm.ts:46](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/customer/rtm.ts#L46)*

It returns the initial state of the current Customer.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`loginData` | string &#124; [LoginRequest](../interfaces/_src_customer_structures_.loginrequest.md) | OAuth token form the Customer's account or full object with login parameters  |

**Returns:** *Promise‹[LoginResponse](../interfaces/_src_customer_structures_.loginresponse.md)›*

___

###  markEventsAsSeen

▸ **markEventsAsSeen**(`chat_id`: string, `seen_up_to`: string): *Promise‹[EmptyResponse](../interfaces/_src_customer_structures_.emptyresponse.md)›*

*Defined in [src/customer/rtm.ts:339](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/customer/rtm.ts#L339)*

Marks events as seen by Agent.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chat_id` | string | chat to mark events |
`seen_up_to` | string | date up to which mark events  |

**Returns:** *Promise‹[EmptyResponse](../interfaces/_src_customer_structures_.emptyresponse.md)›*

___

###  on

▸ **on**(`push`: [Pushes](../enums/_src_agent_structures_.pushes.md), `handler`: function): *function*

*Defined in [src/customer/rtm.ts:37](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/customer/rtm.ts#L37)*

Allows to subscribe a handler for a given push. Returns function to unsubscribe.
Note: multiple subscriptions for the same push are not allowed in sigle websocket connection.

**Parameters:**

▪ **push**: *[Pushes](../enums/_src_agent_structures_.pushes.md)*

push name to subscribe to

▪ **handler**: *function*

function receiving push payload

▸ (`payload`: any): *void*

**Parameters:**

Name | Type |
------ | ------ |
`payload` | any |

**Returns:** *function*

▸ (): *void*

___

###  resumeChat

▸ **resumeChat**(`param`: string | [ResumeChatParameters](../interfaces/_src_customer_structures_.resumechatparameters.md)): *Promise‹[ResumeChatResponse](../interfaces/_src_customer_structures_.resumechatresponse.md)›*

*Defined in [src/customer/rtm.ts:91](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/customer/rtm.ts#L91)*

Restarts an archived chat

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`param` | string &#124; [ResumeChatParameters](../interfaces/_src_customer_structures_.resumechatparameters.md) | either string ID of a chat to activate or full initial chat object  |

**Returns:** *Promise‹[ResumeChatResponse](../interfaces/_src_customer_structures_.resumechatresponse.md)›*

___

###  send

▸ **send**(`action`: string, `payload`: any): *Promise‹any›*

*Inherited from [RTMAPI](_src_internal_index_.rtmapi.md).[send](_src_internal_index_.rtmapi.md#send)*

*Defined in [src/internal/index.ts:120](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/internal/index.ts#L120)*

**Parameters:**

Name | Type |
------ | ------ |
`action` | string |
`payload` | any |

**Returns:** *Promise‹any›*

___

###  sendEvent

▸ **sendEvent**(`chat_id`: string, `event`: [Event](../modules/_src_objects_index_.md#event), `attach_to_last_thread?`: undefined | false | true): *Promise‹[SendEventResponse](../interfaces/_src_customer_structures_.sendeventresponse.md)›*

*Defined in [src/customer/rtm.ts:112](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/customer/rtm.ts#L112)*

Sends an Event object. Use this method to send a message by specifing the Message event type in the request.
It's possible to write to a chat without joining it. The user sending an event will be automatically added to the chat
with the present parameter set to false.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chat_id` | string | chat to send event to |
`event` | [Event](../modules/_src_objects_index_.md#event) | Event object |
`attach_to_last_thread?` | undefined &#124; false &#124; true | if true, adds event to last inactive thread  |

**Returns:** *Promise‹[SendEventResponse](../interfaces/_src_customer_structures_.sendeventresponse.md)›*

___

###  sendRichMessagePostback

▸ **sendRichMessagePostback**(`opts`: [SendRichMessagePostbackParameters](../interfaces/_src_customer_structures_.sendrichmessagepostbackparameters.md)): *Promise‹[EmptyResponse](../interfaces/_src_customer_structures_.emptyresponse.md)›*

*Defined in [src/customer/rtm.ts:124](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/customer/rtm.ts#L124)*

Sends postback for rich message

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`opts` | [SendRichMessagePostbackParameters](../interfaces/_src_customer_structures_.sendrichmessagepostbackparameters.md) | postback data  |

**Returns:** *Promise‹[EmptyResponse](../interfaces/_src_customer_structures_.emptyresponse.md)›*

___

###  sendSneakPeek

▸ **sendSneakPeek**(`chat_id`: string, `sneak_peek_text`: string): *Promise‹[EmptyResponse](../interfaces/_src_customer_structures_.emptyresponse.md)›*

*Defined in [src/customer/rtm.ts:134](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/customer/rtm.ts#L134)*

Sends a sneak peek to a chat.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chat_id` | string | chat to send sneak peek to |
`sneak_peek_text` | string | text to sneak peek  |

**Returns:** *Promise‹[EmptyResponse](../interfaces/_src_customer_structures_.emptyresponse.md)›*

___

###  setCustomerSessionFields

▸ **setCustomerSessionFields**(`session_fields`: object[]): *Promise‹[EmptyResponse](../interfaces/_src_customer_structures_.emptyresponse.md)›*

*Defined in [src/customer/rtm.ts:273](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/customer/rtm.ts#L273)*

Sets session fields for Customer.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`session_fields` | object[] | fields to set in form of object enclosed key:value pairs  |

**Returns:** *Promise‹[EmptyResponse](../interfaces/_src_customer_structures_.emptyresponse.md)›*

___

###  startChat

▸ **startChat**(`opts?`: [StartChatParameters](../interfaces/_src_agent_structures_.startchatparameters.md)): *Promise‹[StartChatResponse](../interfaces/_src_customer_structures_.startchatresponse.md)›*

*Defined in [src/customer/rtm.ts:83](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/customer/rtm.ts#L83)*

Starts a chat

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`opts?` | [StartChatParameters](../interfaces/_src_agent_structures_.startchatparameters.md) | options like initial chat data or continuous switch  |

**Returns:** *Promise‹[StartChatResponse](../interfaces/_src_customer_structures_.startchatresponse.md)›*

___

###  subscribePush

▸ **subscribePush**(`push`: string, `callback`: function): *void*

*Inherited from [RTMAPI](_src_internal_index_.rtmapi.md).[subscribePush](_src_internal_index_.rtmapi.md#subscribepush)*

*Defined in [src/internal/index.ts:138](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/internal/index.ts#L138)*

**Parameters:**

▪ **push**: *string*

▪ **callback**: *function*

▸ (`payload`: any): *void*

**Parameters:**

Name | Type |
------ | ------ |
`payload` | any |

**Returns:** *void*

___

###  unsubscribePush

▸ **unsubscribePush**(`push`: string): *void*

*Inherited from [RTMAPI](_src_internal_index_.rtmapi.md).[unsubscribePush](_src_internal_index_.rtmapi.md#unsubscribepush)*

*Defined in [src/internal/index.ts:145](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/internal/index.ts#L145)*

**Parameters:**

Name | Type |
------ | ------ |
`push` | string |

**Returns:** *void*

___

###  updateChatProperties

▸ **updateChatProperties**(`chat_id`: string, `properties`: [Properties](../interfaces/_src_objects_index_.properties.md)): *Promise‹[EmptyResponse](../interfaces/_src_customer_structures_.emptyresponse.md)›*

*Defined in [src/customer/rtm.ts:143](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/customer/rtm.ts#L143)*

Updates chat properties

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chat_id` | string | chat to update properties |
`properties` | [Properties](../interfaces/_src_objects_index_.properties.md) | properties to update  |

**Returns:** *Promise‹[EmptyResponse](../interfaces/_src_customer_structures_.emptyresponse.md)›*

___

###  updateCustomer

▸ **updateCustomer**(`opts`: [CustomerParameters](../interfaces/_src_customer_structures_.customerparameters.md)): *Promise‹[EmptyResponse](../interfaces/_src_customer_structures_.emptyresponse.md)›*

*Defined in [src/customer/rtm.ts:265](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/customer/rtm.ts#L265)*

Updates Customer's properties.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`opts` | [CustomerParameters](../interfaces/_src_customer_structures_.customerparameters.md) | properties to update  |

**Returns:** *Promise‹[EmptyResponse](../interfaces/_src_customer_structures_.emptyresponse.md)›*

___

###  updateEventProperties

▸ **updateEventProperties**(`chat_id`: string, `thread_id`: string, `event_id`: string, `properties`: [Properties](../interfaces/_src_objects_index_.properties.md)): *Promise‹[EmptyResponse](../interfaces/_src_customer_structures_.emptyresponse.md)›*

*Defined in [src/customer/rtm.ts:191](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/customer/rtm.ts#L191)*

Updates event properties

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chat_id` | string | chat ID of event to update |
`thread_id` | string | thread ID of event to update |
`event_id` | string | event to update properties |
`properties` | [Properties](../interfaces/_src_objects_index_.properties.md) | properties to update  |

**Returns:** *Promise‹[EmptyResponse](../interfaces/_src_customer_structures_.emptyresponse.md)›*

___

###  updateThreadProperties

▸ **updateThreadProperties**(`chat_id`: string, `thread_id`: string, `properties`: [Properties](../interfaces/_src_objects_index_.properties.md)): *Promise‹[EmptyResponse](../interfaces/_src_customer_structures_.emptyresponse.md)›*

*Defined in [src/customer/rtm.ts:162](https://github.com/livechat/lc-sdk-js/blob/21d7a55/src/customer/rtm.ts#L162)*

Updates thread properties

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chat_id` | string | chat ID of thread to update |
`thread_id` | string | thread to update properties |
`properties` | [Properties](../interfaces/_src_objects_index_.properties.md) | properties to update  |

**Returns:** *Promise‹[EmptyResponse](../interfaces/_src_customer_structures_.emptyresponse.md)›*