''' Customer RTM client example usage. '''

from livechat.customer.rtm.client import CustomerRTM

customer_rtm = CustomerRTM.get_client(license_id=12345)
customer_rtm.open_connection()
customer_rtm.login(token='Bearer <your bearer token>')
results = customer_rtm.start_chat(continuous=True)
chat_id = results['response']['payload']['chat_id']
thread_id = results['response']['payload']['thread_id']
customer_rtm.send_event(chat_id=chat_id,
                        event={
                            'type': 'message',
                            'text': 'Hello from Customer RTM!',
                            'recipients': 'all'
                        })
customer_rtm.get_chat(chat_id=chat_id, thread_id=thread_id)
customer_rtm.deactivate_chat(id=chat_id)
customer_rtm.close_connection()
