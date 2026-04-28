from .resource import Resource, EnvironmentAwareResource


"""
contentful_management.editor_interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the EditorInterface class.

API reference: https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/editor-interfaces

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class EditorInterface(Resource, EnvironmentAwareResource):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/editor-interfaces
    """

    def __init__(self, item, **kwargs):
        super(EditorInterface, self).__init__(item, **kwargs)
        self.controls = item.get('controls', [])

    @classmethod
    def base_url(self, space_id, content_type_id, environment_id=None, **kwargs):
        """
        Returns the URI for the editor interface.
        """
        pass

    @classmethod
    def update_attributes_map(klass):
        """
        Attributes for object mapping.
        """
        pass

    def to_json(self):
        """
        Returns the JSON representation of the editor interface.
        """
        pass

    def _update_url(self):
        pass

    def __repr__(self):
        return "<EditorInterface id='{0}'>".format(
            self.sys.get('id', '')
        )
