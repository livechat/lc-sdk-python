''' Agent RTM client example usage. '''

from livechat.agent.rtm.client import AgentRTM

agent_rtm = AgentRTM.get_client()
agent_rtm.open_connection()
agent_rtm.login(token='<your access token>')
results = agent_rtm.start_chat(continuous=True)
chat_id = results['response']['payload']['chat_id']
thread_id = results['response']['payload']['thread_id']
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
