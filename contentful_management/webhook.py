from .resource import Resource
from .webhook_webhooks_call_proxy import WebhookWebhooksCallProxy
from .webhook_webhooks_health_proxy import WebhookWebhooksHealthProxy


"""
contentful_management.webhook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the Webhook class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/webhooks

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class Webhook(Resource):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/webhooks
    """

    def __init__(self, item, **kwargs):
        super(Webhook, self).__init__(item, **kwargs)
        self.name = item.get('name', '')
        self.url = item.get('url', '')
        self.topics = item.get('topics', [])
        self.http_basic_username = item.get('httpBasicUsername', '')
        self.headers = item.get('headers', [])
        self.filters = item.get('filters', [])
        self.transformation = item.get('transformation', {})

    @classmethod
    def update_attributes_map(klass):
        """
        Defines keys and default values for non-generic attributes.
        """
        pass

    @classmethod
    def create_attributes(klass, attributes, previous_object=None):
        """
        Attributes for webhook creation.
        """
        pass

    def calls(self):
        """
        Provides access to call overview for the given webhook.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/webhook-calls

        :return: :class:`WebhookWebhooksCallProxy <contentful_management.webhook_webhooks_call_proxy.WebhookWebhooksCallProxy>` object.
        :rtype: contentful.webhook_webhooks_call_proxy.WebhookWebhooksCallProxy

        Usage:

            >>> webhook_webhooks_call_proxy = webhook.calls()
            <WebhookWebhooksCallProxy space_id="cfexampleapi" webhook_id="my_webhook">
        """
        pass

    def health(self):
        """
        Provides access to health overview for the given webhook.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/webhook-calls/webhook-health

        :return: :class:`WebhookWebhooksHealthProxy <contentful_management.webhook_webhooks_health_proxy.WebhookWebhooksHealthProxy>` object.
        :rtype: contentful.webhook_webhooks_health_proxy.WebhookWebhooksHealthProxy

        Usage:

            >>> webhook_webhooks_health_proxy = webhook.health()
            <WebhookWebhooksHealthProxy space_id="cfexampleapi" webhook_id="my_webhook">
        """
        pass

    def to_json(self):
        """
        Returns the JSON representation of the webhook.
        """
        pass

    def __repr__(self):
        return "<Webhook[{0}] id='{1}'>".format(
            self.name,
            self.sys.get('id', '')
        )
