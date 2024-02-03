import os
import logging
from .base import *

DEBUG = False

ADMINS = [
    ('Maksim S.', 'sustavovm@yandex.ru'),
]


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


ALLOWED_HOSTS = ['www.en-learn.ru','en-learn.ru']

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler(BASE_DIR / 'logs' / 'uwsgi.log')
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('{levelname} {asctime} {module} {message}', style='{')
handler.setFormatter(formatter)

logger.addHandler(handler)

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
