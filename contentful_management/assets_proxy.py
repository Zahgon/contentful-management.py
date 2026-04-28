from .client_proxy import ClientProxy
from .asset import Asset
from .utils import normalize_select


"""
contentful_management.assets_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the AssetsProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/assets

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class AssetsProxy(ClientProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/assets
    """

    @property
    def _resource_class(self):
        pass

    def all(self, query=None, **kwargs):
        """
        Gets all assets of a space.
        """
        pass

    def find(self, asset_id, query=None, **kwargs):
        """
        Gets a single asset by ID.
        """
        pass
