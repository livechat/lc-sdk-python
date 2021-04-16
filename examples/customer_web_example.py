''' Customer WEB client example usage. '''

from livechat.customer.web.client import CustomerWeb

customer_web = CustomerWeb.get_client(license_id=12345,
                                      access_token='<your access token>')
results = customer_web.start_chat(continuous=True)
chat_id = results.json()['chat_id']
thread_id = results.json()['thread_id']
customer_web.send_event(chat_id=chat_id,
                        event={
                            'type': 'message',
                            'text': 'Hello from Customer WEB!',
                            'recipients': 'all'
                        })
customer_web.get_chat(chat_id=chat_id, thread_id=thread_id)
customer_web.deactivate_chat(id=chat_id)
