from .base import *


DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'enlearn',
        'USER': 'maksonik',
        'PASSWORD': '123456789',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]