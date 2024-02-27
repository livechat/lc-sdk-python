''' Agent WEB client example usage. '''

from livechat.agent.web.base import AgentWeb
from livechat.utils.structures import AccessToken, TokenType

# token can be also passed as a raw string like `Bearer dal:A420qcNvdVS4cRMJP269GfgT1LA`
agent_web = AgentWeb.get_client(access_token=AccessToken(
    scheme=TokenType.BEARER, token='dal:A420qcNvdVS4cRMJP269GfgT1LA'))
results = agent_web.start_chat(continuous=True)
chat_id = results.json().get('chat_id')
thread_id = results.json().get('thread_id')
agent_web.send_event(chat_id=chat_id,
                     event={
                         'type': 'message',
                         'text': 'Hello from Agent WEB!',
                         'visibility': 'all'
                     })
agent_web.get_chat(chat_id=chat_id, thread_id=thread_id)
agent_web.deactivate_chat(id=chat_id)
