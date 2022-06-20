''' Webhooks parser module. '''

from typing import Union

from livechat.config import CONFIG
from livechat.webhooks.v33 import WebhookV33
from livechat.webhooks.v34 import WebhookV34
from livechat.webhooks.v35 import WebhookV35

stable_version = CONFIG.get('stable')


def parse_webhook(
    wh_body: dict,
    version: str = stable_version,
) -> Union[WebhookV33, WebhookV34, WebhookV35]:
    ''' Parses provided `wh_body` to a `Webhook` data class.

        Args:
            wh_body (dict): Webhook body received from LiveChat API.
            version (str): API's version. Defaults to the stable version of API.

        Returns:
            Webhook: data class with fields parsed from `wh_body`.

        Raises:
            ValueError: If provided `wh_body` is invalid (contains additional,
                        invalid or missing fields).
    '''
    webhook_data_class = {
        '3.3': WebhookV33,
        '3.4': WebhookV34,
        '3.5': WebhookV35,
    }.get(version)
    try:
        parsed_wh = webhook_data_class(**wh_body)
    except TypeError as error:
        raise ValueError(
            'Invalid webhook body. It should contain the following fields: '
            f'{webhook_data_class.__annotations__}') from error
    try:
        parsed_wh.payload = parsed_wh.payload_data_class()(**parsed_wh.payload)
    except KeyError as error:
        raise ValueError(
            f'`{parsed_wh.action}` is invalid webhook action. '
            'Check the correctness of the webhook body provided.') from error
    except TypeError as error:
        raise ValueError(
            'Invalid webhook payload. It should contain the following fields: '
            f'{parsed_wh.payload_data_class().__annotations__}') from error
    return parsed_wh
