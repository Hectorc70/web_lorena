import os
import sys
from django.core.management.utils import get_random_secret_key

from decouple import config

""" SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())

ALLOWED_HOSTS = [os.getenv("DJANGO_ALLOWED_HOSTS"),
'www.lorenacastrob.com',
'lorenacastrob.com', 
'web-lorena-d6o8t.ondigitalocean.app',
'lorenacastro.herokuapp.com'
]

DEBUG = True

DATABASES = {
        'default': {
            'ENGINE':'django.db.backends.mysql',
            'NAME':os.getenv('DB_NAME'),
            'USER':os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': os.getenv('DB_PORT'),
        }
} """


SECRET_KEY = config("DJANGO_SECRET_KEY", get_random_secret_key())

ALLOWED_HOSTS = [
'www.lorenacastrob.com',
'lorenacastrob.com', 
'web-lorena-d6o8t.ondigitalocean.app',
'lorenacastro.herokuapp.com'
]

DEBUG = config('DEBUG')

DATABASES = {
        'default': {
            'ENGINE':'django.db.backends.mysql',
            'NAME':config('DB_NAME'),
            'USER':config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': config('DB_HOST'),
            'PORT': config('DB_PORT'),
        }
}

