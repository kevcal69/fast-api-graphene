import graphene

from apps.graphql.listing.types import Listing


class ListingQuery(graphene.ObjectType):
    listing = graphene.Field(Listing)

    def resolve_listing(root, info):
        return {
            "name": "Kev Cal",
            "address": {
                "street": "21st flr Fib Building Mugworth Ave",
                "state": "California",
                "country": "US",
                "zipcode": "91000"
            }
        }
