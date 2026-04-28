from .client_proxy import ClientProxy
from .taxonomy_concept import TaxonomyConcept


class TaxonomyConceptsProxy(ClientProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/taxonomy/concept
    """

    @property
    def _resource_class(self):
        pass

    def __init__(self, client, organization_id):
        super(TaxonomyConceptsProxy, self).__init__(client, None)
        self.organization_id = organization_id

    def find(self, concept_id, **kwargs):
        """
        Finds a taxonomy concept.
        """
        pass

    def all(self, query=None, **kwargs):
        """
        Gets all taxonomy concepts.
        """
        pass

    def create(self, resource_id=None, attributes=None, **kwargs):
        """
        Creates a taxonomy concept with an optional user-defined ID.
        """
        pass

    def update(self, concept_id, version, attributes):
        """
        Updates a taxonomy concept.
        """
        pass

    def delete(self, concept_id, version):
        """
        Deletes a taxonomy concept.
        """
        pass

    def _url(self, resource_id=None, **kwargs):
        pass

    def descendants(self, concept_id, query=None, **kwargs):
        """
        Gets descendants of a taxonomy concept.
        """
        pass

    def ancestors(self, concept_id, query=None, **kwargs):
        """
        Gets ancestors of a taxonomy concept.
        """
        pass

    def total(self, **kwargs):
        """
        Gets the total number of taxonomy concepts.
        """
        pass

    def __repr__(self):
        return f"<TaxonomyConceptsProxy organization_id='{self.organization_id}'>"
