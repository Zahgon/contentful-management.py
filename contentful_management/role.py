from .resource import Resource


"""
contentful_management.role
~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the Role class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/roles

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class Role(Resource):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/roles
    """

    def __init__(self, item, **kwargs):
        super(Role, self).__init__(item, **kwargs)
        self.name = item.get('name', '')
        self.description = item.get('description', '')
        self.permissions = item.get('permissions', {})
        self.policies = item.get('policies', [])

    @classmethod
    def update_attributes_map(klass):
        """
        Defines keys and default values for non-generic attributes.
        """
        pass

    def to_json(self):
        """
        Returns the JSON representation of the role.
        """
        pass

    def __repr__(self):
        return "<Role[{0}] id='{1}'>".format(
            self.name,
            self.sys.get('id', '')
        )
