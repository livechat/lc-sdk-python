''' Agent WEB client example usage. '''

from livechat.agent.web.client import AgentWeb

agent_web = AgentWeb.get_client(access_token='<your access token>')
results = agent_web.start_chat(continuous=True)
chat_id = results.json()['chat_id']
thread_id = results.json()['thread_id']
agent_web.send_event(chat_id=chat_id,
                     event={
                         'type': 'message',
                         'text': 'Hello from Agent WEB!',
                         'recipients': 'all'
                     })
agent_web.get_chat(chat_id=chat_id, thread_id=thread_id)
agent_web.deactivate_chat(id=chat_id)
