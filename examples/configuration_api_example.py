''' Configuration API client example usage. '''

from livechat.configuration.base import ConfigurationApi
from livechat.utils.structures import AccessToken, TokenType

# Get list of existing groups.
configuration_api = ConfigurationApi.get_client(token=AccessToken(
    scheme=TokenType.BEARER, token='dal:A420qcNvdVS4cRMJP269GfgT1LA'))
groups = configuration_api.list_groups()
print(groups.json())

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
webhook_id = webhook.json().get('id')
configuration_api.unregister_webhook(id=webhook_id,
                                     owner_client_id='<your owner_client_id>')
