''' Configuration API client example usage. '''

from livechat.configuration.client import ConfigurationApi

# Get group name.
configuration_api = ConfigurationApi.get_client(token='<your access token>')
groups = configuration_api.list_groups()
group_1 = groups.json()[1]['id']
group_1_info = configuration_api.get_group(id=1)
name = group_1_info.json()['name']

# Register and unregister webhook.
webhook = configuration_api.register_webhook(
    action='incoming_chat',
    secret_key='<your secret_key>',
    url='<your url>',
    description='Your incoming chat webhook description.',
    owner_client_id='<your owner_client_id>',
    type='license')
configuration_api.enable_license_webhooks(
    owner_client_id='<your owner_client_id>')
configuration_api.disable_license_webhooks(
    owner_client_id='<your owner_client_id>')
webhook_id = webhook.json()['id']
configuration_api.unregister_webhook(id=webhook_id,
                                     owner_client_id='<your owner_client_id>')
