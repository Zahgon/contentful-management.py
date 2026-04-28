from .resource import Resource

"""
contentful_management.tag
~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the Tag class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/tags

:copyright: (c) 2023 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class Tag(Resource):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/tags
    """

    def __init__(self, item, **kwargs):
        super(Tag, self).__init__(item, **kwargs)
        self.name = item.get('name', '')

    def delete(self):
        """
        Deletes this tag.
        """
        pass

    def to_json(self):
        """
        Returns the JSON representation of the tag.
        """
        pass

    def __repr__(self):
        return "<Tag id='{0}' name='{1}'>".format(
            self.sys.get('id', ''),
            self.name
        )
