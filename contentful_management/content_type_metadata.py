"""
contentful_management.content_type_metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the ContentTypeMetadata class.

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class ContentTypeMetadata(object):
    """
    Represents metadata for a content type.
    """

    def __init__(self, metadata_data):
        self.raw = metadata_data
        self.taxonomy = self._hydrate_taxonomy(metadata_data.get('taxonomy', []))

        # Add other metadata fields as-is for future extensibility
        for key, value in metadata_data.items():
            if key != 'taxonomy':
                setattr(self, key, value)

    def _hydrate_taxonomy(self, taxonomy_data):
        """
        Hydrates taxonomy with proper object types.
        """
        pass

    def to_json(self):
        """
        Returns the JSON representation of the content type metadata.
        """
        pass

    def __repr__(self):
        return "<ContentTypeMetadata taxonomy_count='{0}'>".format(
            len(self.taxonomy) if self.taxonomy else 0
        )
