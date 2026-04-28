try:
    import simplejson as json
except ImportError:
    import json

import dateutil.parser
from .utils import unicode_class

"""
contentful_management.content_type_field_types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the field coercion classes.

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class BasicField(object):
    """
    Base coercion class.
    """

    def __init__(self, items=None):
        self._items = items

    def coerce(self, value):
        """
        Just returns the value.
        """
        pass

    def __repr__(self):
        return "<{0}>".format(
            self.__class__.__name__
        )


class SymbolField(BasicField):
    """
    Symbol coercion class.
    """

    def coerce(self, value):
        """
        Coerces value to str.
        """
        pass


class TextField(SymbolField):
    """
    Text coercion class.
    """
    pass


class IntegerField(BasicField):
    """
    Integer coercion class.
    """

    def coerce(self, value):
        """
        Coerces value to int.
        """
        pass


class NumberField(BasicField):
    """
    Number coercion class.
    """

    def coerce(self, value):
        """
        Coerces value to float.
        """
        pass


class DateField(BasicField):
    """
    Date coercion class.
    """

    def coerce(self, value):
        """
        Coerces ISO8601 date to :class:`datetime.datetime` object.
        """
        pass


class BooleanField(BasicField):
    """
    Boolean coercion class.
    """

    def coerce(self, value):
        """
        Coerces value to boolean.
        """
        pass


class LinkField(BasicField):
    """
    LinkField

    Nothing should be done here as include resolution is handled within
    entries due to depth handling (explained within Entry).
    Only present as a placeholder for proper resolution within ContentType.
    """
    pass


class ArrayField(BasicField):
    """
    Array coercion class.

    Coerces items in collection with it's proper coercion class.
    """

    def __init__(self, items=None):
        super(ArrayField, self).__init__(items)
        self._coercion = self._get_coercion()

    def coerce(self, value):
        """
        Coerces array items with proper coercion.
        """
        pass

    def _get_coercion(self):
        pass


class ObjectField(BasicField):
    """
    Object coercion class.
    """

    def coerce(self, value):
        """
        Coerces value to JSON.
        """
        pass


class LocationField(BasicField):
    """
    Location coercion class.
    """

    def coerce(self, value):
        """
        Coerces value to location hash.
        """
        pass


class RichTextField(BasicField):
    """
    Rich Text coercion class.
    """

    def coerce(self, value):
        """
        Returns the rich text object as is.
        Include resolution and other particular processing is done for CDA only.
        """
        pass


class ResourceLinkField(BasicField):
    """
    ResourceLinkField

    Nothing should be done here as ResourceLink does not support entity
    resolution on the backend side and linked field can’t be used in
    ordering and filtering queries.
    """
    pass
