import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

# TODO: Import from language intelligence
from language_api.graph_api import Ontology


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Your server can be found at /language"}

app.add_route("/language", GraphQLApp(schema=graphene.Schema(query=Ontology)))

