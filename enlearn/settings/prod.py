import os
from .base import *

DEBUG = False

ADMINS = [
    ('Maksim S.', 'sustavovm@yandex.ru'),
]

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}


ALLOWED_HOSTS = ['en-learn.com', 'www.en-learn.com']