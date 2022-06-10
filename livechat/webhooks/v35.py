''' API v3.5 webhooks data classes. '''

from dataclasses import dataclass

# pylint: disable=missing-class-docstring


@dataclass
class WebhookV35:
    webhook_id: str
    secret_key: str
    action: str
    organization_id: str
    additional_data: dict
    payload: dict
