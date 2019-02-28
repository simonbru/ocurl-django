from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .forms import LinkForm


def hello(request):
    if request.method == 'POST':
        form = LinkForm(data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LinkForm()
    # JRESTE SOUS LE DRAPS COMME KKK
    return render(request, 'links/index.html.j2', context={'form': form})
