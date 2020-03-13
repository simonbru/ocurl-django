import graphene

from links.schema import LinksQuery


class Query(LinksQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
