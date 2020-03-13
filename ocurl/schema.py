import graphene
from graphene_django.debug import DjangoDebug

from links.schema import LinksMutation, LinksQuery
from users.schema import UsersMutation


class Query(LinksQuery, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='_debug')


class Mutation(LinksMutation, UsersMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
