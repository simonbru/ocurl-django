import random
import string
from django import forms
from .models import Link

class LinkForm(forms.ModelForm):

    name = forms.CharField(required=False)

    class Meta:
        model = Link
        fields = ['name', 'destination']

    def clean_name(self):
        """Generates a random string of 6 chars when name was not specified"""
        name = self.cleaned_data['name']

        if not name:
            # TODO improve naive algorithm as we could have concurrent creation that could cause unique exception
            for _ in range(10):
                try:
                    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
                    Link.objects.get(name=name)
                except Link.DoesNotExist:
                    break
        return name
