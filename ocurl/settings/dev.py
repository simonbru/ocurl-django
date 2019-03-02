from decouple import config

from .base import *

DEBUG = config('DEBUG', default=True, cast=bool)

SECRET_KEY = config('SECRET_KEY', default='verysecret')
