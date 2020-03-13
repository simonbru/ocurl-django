import graphene
from graphene_django import DjangoObjectType
from graphene_django.forms.mutation import DjangoModelFormMutation, DjangoFormMutation

from .forms import LinkForm, SomeForm
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


class LinkModelFormMutation(DjangoModelFormMutation):
    class Meta:
        # fields = ("name", "destination")
        form_class = LinkForm

class LinkFormMutation(DjangoFormMutation):
    class Meta:
        # fields = ("name", "destination")
        form_class = LinkForm



class SomeFormMutation(DjangoFormMutation):
    class Meta:
        form_class = SomeForm


class LinksMutation:
    update_link_form = LinkModelFormMutation.Field()
    update_link_form2 = LinkFormMutation.Field()
    # update_link_serializer = LinkSerializerMutation.Field()
    some_form_mutation = SomeFormMutation.Field()
