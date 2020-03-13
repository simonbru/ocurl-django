from django import forms
from django.utils.crypto import get_random_string

from .models import Link


class LinkForm(forms.ModelForm):

    name = forms.CharField(required=False)

    class Meta:
        model = Link
        fields = ['name', 'destination', 'expiration_date']

    def clean_name(self):
        """Generates a random string of 6 chars when name was not specified"""
        name = self.cleaned_data['name']
        raise forms.ValidationError("Custom error")
        if not name:
            # TODO: improve naive algorithm as we could have concurrent
            #       creation that could cause unique exception
            for _ in range(10):
                try:
                    name = get_random_string(length=6)
                    Link.objects.get(name=name)
                except Link.DoesNotExist:
                    break
        return name


class SomeForm(forms.Form):
    truc = forms.CharField()

    def clean_truc(self):
        raise forms.ValidationError("Truc is not clean")
