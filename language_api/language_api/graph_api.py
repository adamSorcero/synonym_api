import graphene
from sorcero_nl.nl_expansion_caches import OntologyCache

# Generic Synonym Return Class
class SynonymType(graphene.ObjectType):
    """
    Defined Return type, each variable below is populated by the resolve method before returning
    """
    text = graphene.String()
    synonyms = graphene.List(graphene.String,description="synonyms")
    prefered_term = graphene.String()
    ontology_name = graphene.String()
    
    def __init__(self, **node_props):
        self.node_props = node_props
        super().__init__(**node_props)

# global ontology cache for database lookups
ontology_cache = OntologyCache()

class Ontology(graphene.ObjectType):

    # synonyms query     
    synonyms = graphene.List(SynonymType, description="Retrieve synonyms from an ontology ",
                          ontology_name=graphene.String(description='Name of the ontology to use for retrieval', default_value='ai_playground'),
                          text=graphene.String(description='Text to find synonyms for', default_value='example')
                        )

    # RESOLVER FUNCTIONS 
    # Note resolve_x functions must match the query defined above by name
    def resolve_synonyms(root, info, ontology_name=None,text=None):
        
        # Retrieve the ontology
        ontology = ontology_cache.retrieve(ontology_name)

        nodes = [
                    {"text":text,"synonyms":ontology.synonyms(text),"prefered_term":ontology.get_prefered_term(text),'ontology_name':ontology_name}
                ]

        return [SynonymType(**node) for node in nodes]
