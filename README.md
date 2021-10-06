# LiveChat Platform API SDK for Python3

This Software Development Kit written in Python3 helps developers build external backend apps that extend LiveChat features. The SDK makes it easy to use Agent Chat API, Customer Chat API and Configuration API.

## API protocol docs

For protocol documentation of LiveChat APIs, please go to [Livechat Platform Docs](https://developers.livechatinc.com/docs/).

## Technical docs

Agent Chat API:
* [RTM API](https://livechat.github.io/lc-sdk-python/agent_rtm.html)
* [WEB API](https://livechat.github.io/lc-sdk-python/agent_web.html)

Customer Chat API:
* [RTM API](https://livechat.github.io/lc-sdk-python/customer_rtm.html)
* [WEB API](https://livechat.github.io/lc-sdk-python/customer_web.html)

Management:
* [Configuration API](https://livechat.github.io/lc-sdk-python/configuration_api.html)

Reports:
* [Reports API](https://livechat.github.io/lc-sdk-python/reports_api.html)

## Installation

### pip

```bash
pip install lc-sdk-python
```

## Usage

### Agent RTM API usage example

Basic example on how to login as an agent and change routing status to `not_accepting_chats`.

First, create your AgentRTM client and log in:
```python
>>> from livechat.agent import AgentRTM
>>> my_agent = AgentRTM.get_client()
>>> my_agent.login(token='Bearer <your bearer token>')
INFO:root:
REQUEST:
{
    "action": "login",
    "payload": {
        "token": "Bearer <your bearer token>
    },
    "request_id": "5571081909"
}
INFO:root:
RESPONSES:
{
    "response": {
        "request_id": "5571081909",
        "action": "login",
        "type": "response",
        "payload": {
            ...
        },
        "success": true
    },
    "pushes": []
}
```

Now you can change the routing status of the agent:

```python
>>> my_agent.set_routing_status(status='not_accepting_chats')
INFO:root:
REQUEST:
{
    "action": "set_routing_status",
    "payload": {
        "status": "not_accepting_chats"
    },
    "request_id": "8214452850"
}
INFO:root:
RESPONSES:
{
    "response": {
        "request_id": "8214452850",
        "action": "set_routing_status",
        "type": "response",
        "payload": {},
        "success": true
        ...
    }
}
```

Finally, log out:

```python
>>> my_agent.logout()
INFO:root:
REQUEST:
{
    "action": "logout",
    "payload": {},
    "request_id": "629300202"
}
INFO:root:
RESPONSES:
{
    "response": {
        "request_id": "629300202",
        "action": "logout",
        "type": "response",
        "success": true
    },
    "pushes": []
}
```


## Feedback

​If you find any bugs or have trouble implementing the code on your own, please create an issue or contact us via e-mail: apiteam.qa@livechat.com.

## About LiveChat

LiveChat is an online customer service software with live support, help desk software, and web analytics capabilities. It's used by more than 32,000 companies all over the world. For more info, check out [LiveChat](https://livechat.com/).
