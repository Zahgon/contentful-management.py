from .resource import Resource


class TaxonomyConceptScheme(Resource):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/taxonomy/concept-scheme
    """

    def __init__(self, item, **kwargs):
        super(TaxonomyConceptScheme, self).__init__(item, **kwargs)
        self.uri = item.get('uri', '')
        self.pref_label = item.get('prefLabel', {})
        self.definition = item.get('definition', {})
        self.top_concepts = item.get('topConcepts', [])
        self.concepts = item.get('concepts', [])
        self.total_concepts = item.get('totalConcepts', 0)

    @classmethod
    def create_attributes(klass, attributes, previous_object=None):
        """
        Attributes for taxonomy concept scheme creation.
        """
        pass

    def to_json(self):
        """
        Returns the JSON representation of the taxonomy concept scheme.
        """
        pass

    def __repr__(self):
        return f"<TaxonomyConceptScheme id='{self.sys.get('id', '')}'>"
