import streamlit as st


import streamlit as st
from HTTP_requests.graphQL_api import GraphQL_API


class API:
    """
    A class which interfaces with the GraphQL Endpoint
    """
    def __init__(self,url_base,endpoint):
        self.url_base = url_base
        self.endpoint = endpoint

        self.graph = GraphQL_API(self.url_base, self.endpoint)

        
    def query(self,ontology_name,text):
        """
        Runs the synonyms query with an ontology_name and ontology_text
        """

        query = """

        {synonyms(ontologyName:"%s",text:"%s") {
        text
        preferedTerm
        ontologyName
        synonyms
        }}

        """ % (ontology_name,text)

        return self.graph.query(query)

############################
# Begin Streamlit Interface
############################


# Create the API interface
api = API(url_base='http://127.0.0.1:8125',endpoint="/language") # Todo Pull from env

st.header("Synonym API")

text = st.text_input("Word Lookup")
ontology_name = st.text_input("Ontology Name")

st.header("Results")

# Query the API interface
results = api.query(ontology_name,text)

st.write(results)
