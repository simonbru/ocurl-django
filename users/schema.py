import graphene
from graphene_django import DjangoObjectType


class TrucInput(graphene.InputObjectType):
    age = graphene.UUID(required=True)


class Authenticate(graphene.Mutation):
    class Arguments:
        login = graphene.String()
        password = graphene.String()
        truc = TrucInput()

    access_token = graphene.String()

    def mutate(root, info, login, password, truc):
        return Authenticate(access_token="blablabla")


class UsersMutation:
    authenticate = Authenticate.Field()
