from .client_proxy import ClientProxy
from .entry import Entry
from .utils import normalize_select


"""
contentful_management.entries_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the EntriesProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/entries

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class EntriesProxy(ClientProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/entries
    """

    def __init__(self, client, space_id, environment_id=None, content_type_id=None):
        super(EntriesProxy, self).__init__(client, space_id, environment_id=environment_id)
        self.content_type_id = content_type_id

    @property
    def _resource_class(self):
        pass

    def all(self, query=None):
        """
        Gets all entries of a space.
        """
        pass

    def find(self, entry_id, query=None):
        """
        Gets a single entry by ID.
        """
        pass

    def create(self, resource_id=None, attributes=None, **kwargs):
        """
        Creates an entry with a given ID (optional) and attributes.
        """
        pass
