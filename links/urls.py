from django.urls import path

import links.views

urlpatterns = [
    path('', links.views.hello),
    path('r/<str:name>/', links.views.shortener_redirect),
]
