from .client_proxy import ClientProxy
from .taxonomy_concept_scheme import TaxonomyConceptScheme


class TaxonomyConceptSchemesProxy(ClientProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/taxonomy/concept-scheme
    """
    @property
    def _resource_class(self):
        pass

    def __init__(self, client, organization_id):
        super(TaxonomyConceptSchemesProxy, self).__init__(client, None)
        self.organization_id = organization_id

    def total(self, **kwargs):
        """
        Gets the total number of taxonomy concept schemes.
        """
        pass

    def find(self, concept_scheme_id, **kwargs):
        """
        Finds a taxonomy concept scheme.
        """
        pass

    def all(self, query=None, **kwargs):
        """
        Gets all taxonomy concept schemes.
        """
        pass

    def create(self, resource_id=None, attributes=None, **kwargs):
        """
        Creates a taxonomy concept scheme with an optional user-defined ID.
        """
        pass

    def update(self, concept_scheme_id, version, attributes):
        """
        Updates a taxonomy concept scheme.
        """
        pass

    def delete(self, concept_scheme_id, version):
        """
        Deletes a taxonomy concept scheme.
        """
        pass

    def _url(self, resource_id=None, **kwargs):
        pass

    def __repr__(self):
        return f"<TaxonomyConceptSchemesProxy organization_id='{self.organization_id}'>"
