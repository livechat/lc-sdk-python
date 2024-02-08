''' Customer WEB client example usage. '''

from livechat.customer.web.base import CustomerWeb
from livechat.utils.structures import AccessToken, TokenType

customer_web = CustomerWeb.get_client(
    organization_id='142cf3ad-5d54-4cf6-8ce1-3773d14d7f3f',
    access_token=AccessToken(type=TokenType.BEARER,
                             token='dal:A6420cNvdVS4cRMJP269GfgT1LA'))
results = customer_web.start_chat(continuous=True)
chat_id = results.json().get('chat_id')
thread_id = results.json().get('thread_id')
customer_web.send_event(chat_id=chat_id,
                        event={
                            'type': 'message',
                            'text': 'Hello from Customer WEB!',
                            'visibility': 'all'
                        })
customer_web.get_chat(chat_id=chat_id, thread_id=thread_id)
customer_web.deactivate_chat(id=chat_id)
