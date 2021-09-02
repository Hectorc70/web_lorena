import os
import sys
from django.core.management.utils import get_random_secret_key

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())

ALLOWED_HOSTS = [os.getenv("DJANGO_ALLOWED_HOSTS"),
'www.lorenacastrob.com',
'lorenacastrob.com', 
]

DEBUG = os.getenv("DEBUG", "False") == "True"

DATABASES = {
        'default': {
            'ENGINE':'django.db.backends.mysql',
            'NAME':os.getenv('DB_NAME'),
            'USER':os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': os.getenv('DB_PORT'),
        }
}