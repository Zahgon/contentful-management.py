from .client_proxy import ClientProxy
from .upload import Upload
from .utils import str_type


"""
contentful_management.uploads_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the UploadsProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/uploads

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class UploadsProxy(ClientProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/uploads
    """

    @property
    def _resource_class(self):
        pass

    def all(*args, **kwargs):
        """
        Not supported.
        """

        raise Exception("Not supported")

    def create(self, file_or_path, **kwargs):
        """
        Creates an upload for the given file or path.
        """
        pass

    def find(self, upload_id, **kwargs):
        """
        Finds an upload by ID.
        """
        pass

    def delete(self, upload_id):
        """
        Deletes an upload by ID.
        """
        pass
