from .client_proxy import ClientProxy
from .editor_interface import EditorInterface


"""
contentful_management.editor_interfaces_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the EditorInterfacesProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/editor-interface

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class EditorInterfacesProxy(ClientProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/editor-interface
    """

    def __init__(self, client, space_id, environment_id=None, content_type_id=None):
        super(EditorInterfacesProxy, self).__init__(client, space_id, environment_id)
        self.content_type_id = content_type_id

    @property
    def _resource_class(self):
        pass

    def all(self):
        """
        Gets the default editor interface.
        """
        pass

    def find(self):
        """
        Gets the default editor interface.
        """
        pass

    def default(self):
        """
        Gets the default editor interface.
        """
        pass

    def create(self, *args, **kwargs):
        """
        Not supported.
        """

        raise Exception("Not Supported")

    def delete(self, *args, **kwargs):
        """
        Not supported.
        """

        raise Exception("Not Supported")

    def _url(self, **kwargs):
        pass

    def __repr__(self):
        return "<{0} space_id='{1}' environment_id='{2}' content_type_id='{3}'>".format(
            self.__class__.__name__,
            self.space_id,
            self.environment_id,
            self.content_type_id
        )
