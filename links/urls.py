from django.urls import path

from links.views import hello

urlpatterns = [
    path('', hello),
]
