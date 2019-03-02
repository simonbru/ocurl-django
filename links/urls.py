from django.urls import path

import links.views

urlpatterns = [
    path('', links.views.hello, name='home'),
    path('r/<str:name>/', links.views.shortener_redirect, name='link_redirect'),
]
