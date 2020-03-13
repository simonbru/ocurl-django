from decouple import Csv, config

from .base import *

DEBUG = config('DEBUG', default=True, cast=bool)

SECRET_KEY = config('SECRET_KEY', default='verysecret')

INTERNAL_IPS = config('INTERNAL_IPS', default='127.0.0.1', cast=Csv())

INSTALLED_APPS += [
    'django_extensions',
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

GRAPHENE['MIDDLEWARE'] += [
    'graphene_django.debug.DjangoDebugMiddleware',
]
