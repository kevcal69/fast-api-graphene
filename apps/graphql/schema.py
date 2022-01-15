import graphene

from apps.graphql.listing.schema import ListingQuery


query = [ListingQuery]


class Query(*query, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
