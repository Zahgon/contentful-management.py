from .resource import FieldsResource, PublishResource, ArchiveResource, EnvironmentAwareResource, MetadataResource
from .utils import is_link, is_link_array, snake_case
from .entry_snapshots_proxy import EntrySnapshotsProxy


"""
contentful_management.entry
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the Entry class.

API reference: https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/entries

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class Entry(MetadataResource, FieldsResource, PublishResource, ArchiveResource, EnvironmentAwareResource):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/entries
    """

    @classmethod
    def create_headers(klass, attributes):
        """
        Headers for entry creation.
        """
        pass

    def __init__(self, *args, **kwargs):
        self.__CONTENT_TYPE__ = None
        super(Entry, self).__init__(*args, **kwargs)

    def snapshots(self):
        """
        Provides access to snapshot management methods for the given entry.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/snapshots

        :return: :class:`EntrySnapshotsProxy <contentful_management.entry_snapshots_proxy.EntrySnapshotsProxy>` object.
        :rtype: contentful.entry_snapshots_proxy.EntrySnapshotsProxy

        Usage:

            >>> entry_snapshots_proxy = entry.snapshots()
            <EntrySnapshotsProxy space_id="cfexampleapi" environment_id="master" entry_id="nyancat">
        """
        pass

    def update(self, attributes=None):
        """
        Updates the entry with attributes.
        """
        pass

    def _coerce(self, value):
        pass

    def _missing_field_raw_id(self, name):
        pass

    def _is_missing_field(self, name):
        """
        Fields that are voided in the WebApp will be not returned in
        API responses, therefore we need to check if they are part of
        the content type to determine if they should or should not be
        serialized.
        """
        pass

    def _content_type(self):
        pass

    def _real_field_id_for(self, field_id):
        pass

    def __repr__(self):
        return "<Entry[{0}] id='{1}'>".format(
            self.sys['content_type'].sys.get('id', ''),
            self.sys.get('id', '')
        )
