''' Customer RTM client example usage. '''

from livechat.customer.rtm.base import CustomerRTM

customer_rtm = CustomerRTM.get_client(
    organization_id='142cf3ad-5d54-4cf6-8ce1-3773d14d7f3f')
customer_rtm.open_connection()
customer_rtm.login(token='Bearer <your bearer token>')
response = customer_rtm.start_chat(continuous=True)
chat_id = response.payload.get('chat_id')
thread_id = response.payload.get('thread_id')

# Get all messages including the non-response messages (e.g. pushes). Returns a list
incoming_chat_push = customer_rtm.ws.messages[0]

customer_rtm.send_event(chat_id=chat_id,
                        event={
                            'type': 'message',
                            'text': 'Hello from Customer RTM!',
                            'visibility': 'all'
                        })
customer_rtm.get_chat(chat_id=chat_id, thread_id=thread_id)
customer_rtm.deactivate_chat(id=chat_id)
customer_rtm.close_connection()
