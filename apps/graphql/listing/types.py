import graphene


class Address(graphene.ObjectType):
    street = graphene.String()
    state = graphene.String()
    country = graphene.String()
    zip_code = graphene.String()


class Listing(graphene.ObjectType):
    name = graphene.String()
    address = graphene.Field(Address)
