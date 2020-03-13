import graphene
from graphene_django import DjangoObjectType

from .models import Link


class LinkType(DjangoObjectType):
    class Meta:
        model = Link


class LinksQuery:
    links = graphene.List(LinkType)
    link = graphene.Field(LinkType, id=graphene.ID(), name=graphene.String())

    def resolve_links(self, info, **kwargs):
        return Link.objects.all()

    def resolve_link(self, info, **kwargs):
        return Link.objects.get(**kwargs)
