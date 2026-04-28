from .resource import FieldsResource, PublishResource, ArchiveResource, EnvironmentAwareResource, MetadataResource


"""
contentful_management.asset
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the Asset class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/assets

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class Asset(MetadataResource, FieldsResource, PublishResource, ArchiveResource, EnvironmentAwareResource):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/assets
    """

    def url(self, **kwargs):
        """
        Returns a formatted URL for the asset's File
        with serialized parameters.

        Usage:
            >>> my_asset.url()
            "//images.contentful.com/spaces/foobar/..."
            >>> my_asset.url(w=120, h=160)
            "//images.contentful.com/spaces/foobar/...?w=120&h=160"
        """
        pass

    def process(self):
        """
        Calls the process endpoint for all locales of the asset.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/assets/asset-processing
        """
        pass

    def __repr__(self):
        return "<Asset id='{0}' url='{1}'>".format(
            self.sys.get('id', ''),
            self.url()
        )
