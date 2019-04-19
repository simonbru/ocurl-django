from django.shortcuts import get_object_or_404, redirect, render

from .forms import LinkForm
from .models import Link


def hello(request):
    if request.method == 'POST':
        form = LinkForm(data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LinkForm()
    # JRESTE SOUS LE DRAPS COMME KKK
    # TODO remove link forms after dev
    return render(request, 'links/index.html.j2', context={'form': form, 'links': Link.objects.all()})


def shortener_redirect(request, name):
    """Redirects to destination based on the name"""
    link = get_object_or_404(Link, name=name)
    if link.is_expired:
        return render(request, 'links/expired.html.j2', status=410)
    return redirect(link.destination)
