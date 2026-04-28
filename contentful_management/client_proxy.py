"""
contentful_management.client_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the ClientProxy class.

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class ClientProxy(object):
    """
    Base class for proxies.
    """

    def __init__(self, client, space_id, environment_id=None):
        self.client = client
        self.space_id = space_id
        self.environment_id = environment_id

    def __repr__(self):
        return "<{0} space_id='{1}'{2}>".format(
            self.__class__.__name__,
            self.space_id,
            " environment_id='{0}'".format(self.environment_id) if self.environment_id is not None else ''
        )

    @property
    def _resource_class(self):
        raise Exception("Must Implement")

    def all(self, query=None):
        """
        Gets resource collection for _resource_class.
        """
        pass

    def find(self, resource_id, query=None, **kwargs):
        """Gets a single resource."""
        pass

    def create(self, resource_id=None, attributes=None):
        """
        Creates a resource with the given ID (optional) and attributes.
        """
        pass

    def delete(self, resource_id, **kwargs):
        """
        Deletes a resource by ID.
        """
        pass

    def _url(self, resource_id='', **kwargs):
        pass
