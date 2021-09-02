import os
import sys
from django.core.management.utils import get_random_secret_key

import dj_database_url


SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())

ALLOWED_HOSTS = [os.getenv("DJANGO_ALLOWED_HOSTS"),
'www.lorenacastrob.com',
'lorenacastrob.com', 
]

DEBUG = os.getenv("DEBUG", "False") == "True"

DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
    }
