''' API v3.4 webhooks data classes. '''

from dataclasses import dataclass

# pylint: disable=missing-class-docstring


@dataclass
class WebhookV34:
    webhook_id: str
    secret_key: str
    action: str
    organization_id: str
    additional_data: dict
    payload: dict
