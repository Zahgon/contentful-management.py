from .resource import Resource


"""
contentful_management.webhook_health
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the WebhookHealth class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/webhook-calls/webhook-health

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class WebhookHealth(Resource):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/webhook-calls/webhook-health
    """

    def __init__(self, item, **kwargs):
        super(WebhookHealth, self).__init__(item, **kwargs)
        self.calls = item.get('calls', {})
        self.total = self.calls.get('total', 0)
        self.healthy = self.calls.get('healthy', 0)

    @classmethod
    def base_url(klass, space_id, webhook_id, **kwargs):
        """
        Returns the URI for the webhook health.
        """
        pass

    @property
    def webhook_id(self):
        pass

    def __repr__(self):
        return "<WebhookHealth[{0}] total={1} healthy={2}>".format(
            self.webhook_id,
            self.total,
            self.healthy
        )
