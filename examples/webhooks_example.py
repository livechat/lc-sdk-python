''' Webhooks parser usage example. '''

from livechat.webhooks.parser import parse_webhook

webhook_example = {
    'webhook_id': '166c029b-a2c6-4010-aa0c-5a984353a7dd',
    'secret_key': 'top_secret_value',
    'action': 'chat_deactivated',
    'organization_id': 'f9c7cc55-b35a-4e76-b0d5-ae9fce362314',
    'payload': {
        'chat_id': 'PJ0MRSHTDG',
        'thread_id': 'K600PKZON8'
    },
    'additional_data': {}
}

parsed_wh = parse_webhook(webhook_example)
print(f'Webhook action: {parsed_wh.action}')
print(f'Chat ID from the webhook\'s payload: {parsed_wh.payload.chat_id}')
