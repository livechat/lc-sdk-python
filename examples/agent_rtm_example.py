''' Agent RTM client example usage. '''

from livechat.agent.rtm.base import AgentRTM

agent_rtm = AgentRTM.get_client()
agent_rtm.open_connection()
agent_rtm.login(token='<your access token>')
response = agent_rtm.start_chat(continuous=True)
chat_id = response.payload.get('chat_id')
thread_id = response.payload.get('thread_id')

# Get `incoming_chat` push from all messages including the non-response messages (i.e. pushes)
incoming_chat_push = agent_rtm.ws.messages[0]

agent_rtm.send_event(chat_id=chat_id,
                     event={
                         'type': 'message',
                         'text': 'Hello from Agent RTM!',
                         'visibility': 'all'
                     })
agent_rtm.get_chat(chat_id=chat_id, thread_id=thread_id)
agent_rtm.deactivate_chat(id=chat_id)
agent_rtm.logout()
agent_rtm.close_connection()
