import dateutil.parser

from datetime import datetime

from .utils import snake_case, camel_case, base_path_for, sanitize_date


"""
contentful_management.resource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the Resource, FieldResource, PublishResource, ArchiveResource and Link classes.

API reference: https://www.contentful.com/developers/docs/references/content-delivery-api/#/introduction/common-resource-attributes

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class Resource(object):
    """
    Base resource class.

    Implements common resource attributes.

    API reference: https://www.contentful.com/developers/docs/references/content-delivery-api/#/introduction/common-resource-attributes
    """

    def __init__(self, item, default_locale='en-US', client=None):
        self.raw = item
        self.default_locale = default_locale
        self._client = client
        self.sys = self._hydrate_sys(item)

    @classmethod
    def base_url(klass, space_id='', resource_id=None, environment_id=None, **kwargs):
        """
        Returns the URI for the resource.
        """
        pass

    @classmethod
    def create_attributes(klass, attributes, previous_object=None):
        """
        Attributes for resource creation.
        """
        pass

    @classmethod
    def create_headers(klass, attributes):
        """
        Headers for resource creation.
        """
        pass

    @classmethod
    def update_attributes_map(klass):
        """
        Defines keys and default values for non-generic attributes.
        """
        pass

    def delete(self):
        """
        Deletes the resource.
        """
        pass

    def update(self, attributes=None):
        """
        Updates the resource with attributes.
        """
        pass

    def save(self):
        """
        Saves the current state of the resource.
        """
        pass

    def reload(self, result=None):
        """
        Reloads the resource.
        """
        pass

    def to_link(self):
        """
        Returns a link for the resource.
        """
        pass

    def to_json(self):
        """
        Returns the JSON representation of the resource.
        """
        pass

    def _hydrate_sys(self, item):
        pass

    def _linkables(self):
        pass

    def _dateables(self):
        pass

    def _build_link(self, link):
        pass

    def _update_headers(self):
        pass

    def _update_url(self):
        pass

    def _update_from_resource(self, other):
        pass

    @property
    def _environment_id(self):
        """
        Returns the Environment ID.
        """
        pass

    def __getattr__(self, name, *args, **kwargs):
        if name in ['__getstate__', '__setstate__']:
            return super(Resource, self).__getattr__(name, *args, **kwargs)
        if name in self.sys:
            return self.sys[name]
        raise AttributeError(
            "'{0}' object has no attribute '{1}'".format(
                self.__class__.__name__,
                name
            )
        )


class MetadataResource(Resource):
    """
    Metadata resource class.

    Implements metadata handling for resources.
    """

    def __init__(self, item, **kwargs):
        super(MetadataResource, self).__init__(item, **kwargs)
        self._metadata = self._hydrate_metadata(item)

    def _hydrate_metadata(self, item):
        pass

    def coerce_tags(self, tags):
        """
        Coerces tags to the proper type.
        """
        pass

    def coerce_concepts(self, concepts):
        """
        Coerces concepts to the proper type.
        """
        pass

    @classmethod
    def create_attributes(klass, attributes, previous_object=None):
        """
        Attributes for resource creation.
        """
        pass


class FieldsResource(Resource):
    """
    Fields resource class.

    Implements locale handling for resource fields.
    """

    @classmethod
    def create_attributes(klass, attributes, previous_object=None):
        """
        Attributes for resource creation.
        """
        pass

    def __init__(self, item, **kwargs):
        super(FieldsResource, self).__init__(item, **kwargs)
        self._fields = self._hydrate_fields(item)

    def fields(self, locale=None):
        """
        Get fields for a specific locale.

        :param locale: (optional) Locale to fetch, defaults to default_locale.
        """
        pass

    def fields_with_locales(self):
        """
        Get fields with locales per field.
        """
        pass

    def to_json(self):
        """
        Returns the JSON Representation of the resource.
        """
        pass

    @property
    def locale(self):
        """
        Returns the resource locale.
        """
        pass

    def _real_field_id_for(self, field_id):
        pass

    def _serialize_value(self, value):
        pass

    def _hydrate_fields(self, item):
        pass

    def _coerce(self, value):
        pass

    def _locale(self):
        pass

    def _update_from_resource(self, other):
        pass

    def __getattr__(self, name, *args, **kwargs):
        if name in ['__getstate__', '__setstate__']:
            return super(FieldsResource, self).__getattr__(name, *args, **kwargs)
        locale = self._locale()
        if name in self._fields.get(locale, {}):
            return self._fields[locale][name]
        return super(FieldsResource, self).__getattr__(name)

    def __setattr__(self, name, value):
        if name not in ['raw', 'sys', 'default_locale',
                        '_client', '_fields', '__CONTENT_TYPE__', '_metadata']:
            locale = self._locale()
            if (name in self._fields.get(locale, {}) or
                    self._is_missing_field(name)):
                if locale not in self._fields:
                    self._fields[locale] = {}
                self._fields[locale][name] = value
                return self._fields[locale][name]
        return super(FieldsResource, self).__setattr__(name, value)

    def _is_missing_field(self, name):
        """
        By default, fields not appearing on responses are considered
        as object meta-data, and they will not be added to `_fields`,
        making them not part of the serialization when sent back to
        the API for saving.
        """
        pass


class PublishResource(object):
    """
    Allows for resource publish/unpublish.
    """

    @property
    def is_published(self):
        """
        Checks if resource is published.
        """
        pass

    @property
    def is_updated(self):
        """
        Checks if a resource has been updated since last publish.
        Returns False if resource has not been published before.
        """
        pass

    def publish(self):
        """
        Publishes the resource.
        """
        pass

    def unpublish(self):
        """
        Unpublishes the resource.
        """
        pass


class ArchiveResource(object):
    """
    Allows for resource archive/unarchive.
    """

    @property
    def is_archived(self):
        """
        Checks if Resource is archived.
        """
        pass

    def archive(self):
        """
        Archives the resource.
        """
        pass

    def unarchive(self):
        """
        Unarchives the resource.
        """
        pass


class EnvironmentAwareResource(object):
    """
    Allows environment aware resources to resolve the environment ID.
    """

    @property
    def _environment_id(self):
        """
        Returns the Environment ID.
        """
        pass


class Link(Resource):
    """
    Link Class

    API reference: https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/links
    """

    def resolve(self, space_id=None, environment_id=None):
        """
        Resolves link to a specific resource.
        """
        pass

    def to_json(self):
        """
        Returns the JSON representation of the link.
        """
        pass

    def __repr__(self):
        return "<Link[{0}] id='{1}'>".format(
            self.link_type,
            self.id
        )
