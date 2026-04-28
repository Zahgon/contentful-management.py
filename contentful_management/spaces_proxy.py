from .client_proxy import ClientProxy
from .space import Space


"""
contentful_management.spaces_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the SpacesProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/spaces

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class SpacesProxy(ClientProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/spaces
    """

    def __init__(self, client):
        super(SpacesProxy, self).__init__(client, None)

    def __repr__(self):
        return "<SpacesProxy>"

    @property
    def _resource_class(self):
        pass

    def all(self, query=None, **kwargs):
        """
        Gets all spaces.
        """
        pass

    def find(self, space_id, query=None, **kwargs):
        """
        Gets a space by ID.
        """
        pass

    def create(self, attributes=None, **kwargs):
        """
        Creates a space with given attributes.
        """
        pass

    def delete(self, space_id):
        """
        Deletes a space by ID.
        """
        pass
