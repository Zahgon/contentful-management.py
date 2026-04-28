from .resource import Resource, EnvironmentAwareResource
from copy import deepcopy


"""
contentful_management.ui_extension
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the UIExtension class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/ui-extensions

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class UIExtension(Resource, EnvironmentAwareResource):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/ui-extensions
    """

    def __init__(self, item, **kwargs):
        super(UIExtension, self).__init__(item, **kwargs)
        self.extension = deepcopy(item.get('extension', {}))

    @property
    def source(self):
        pass

    @source.setter
    def source(self, value):
        pass

    @property
    def name(self):
        pass

    @name.setter
    def name(self, value):
        pass

    @property
    def field_types(self):
        pass

    @field_types.setter
    def field_types(self, value):
        pass

    @property
    def sidebar(self):
        pass

    @sidebar.setter
    def sidebar(self, value):
        pass

    @property
    def parameters(self):
        pass

    @parameters.setter
    def parameters(self, value):
        pass

    @classmethod
    def update_attributes_map(klass):
        """
        Defines keys and default values for non-generic attributes.
        """
        pass

    def to_json(self):
        """
        Returns the JSON Representation of the UI extension.
        """
        pass

    def __repr__(self):
        return "<UIExtension[{0}] id='{1}' field_types=[{2}]>".format(
            self.name,
            self.sys.get('id', ''),
            ', '.join(
                "'{0}'".format(t)
                for t in [
                    ft['type']
                    for ft in self.field_types
                ]
            )
        )
