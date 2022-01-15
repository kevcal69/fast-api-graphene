import graphene
from fastapi import FastAPI
from starlette.applications import Starlette
from starlette_graphene3 import GraphQLApp, make_playground_handler

from apps.graphql.schema import schema


app = Starlette()
app.mount("/", GraphQLApp(schema, on_get=make_playground_handler()))
