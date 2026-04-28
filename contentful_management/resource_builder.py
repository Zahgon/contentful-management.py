from .tag import Tag
from .role import Role
from .user import User
from .entry import Entry
from .array import Array
from .asset import Asset
from .space import Space
from .locale import Locale
from .upload import Upload
from .api_key import ApiKey
from .webhook import Webhook
from .snapshot import Snapshot
from .environment import Environment
from .ui_extension import UIExtension
from .content_type import ContentType
from .webhook_call import WebhookCall
from .organization import Organization
from .webhook_health import WebhookHealth
from .preview_api_key import PreviewApiKey
from .editor_interface import EditorInterface
from .space_membership import SpaceMembership
from .space_periodic_usage import SpacePeriodicUsage
from .personal_access_token import PersonalAccessToken
from .organization_periodic_usage import OrganizationPeriodicUsage
from .taxonomy_concept import TaxonomyConcept
from .taxonomy_concept_scheme import TaxonomyConceptScheme


"""
contentful_management.resource_builder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the ResourceBuilder class.

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class ResourceBuilder(object):
    """
    Creates objects of the proper resource type.
    """

    def __init__(self, client, default_locale, json):
        self.client = client
        self.default_locale = default_locale
        self.json = json

    def build(self):
        """
        Creates the objects from the JSON response.
        """
        pass

    def _build_array(self):
        pass

    def _build_item(self, item):
        pass
