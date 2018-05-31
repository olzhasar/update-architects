from .base import *
from .secret_settings import *


DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'update-architects.com',
                 '139.162.175.130']

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'update',
        'USER': 'update_user',
        'PASSWORD': 'aA14469425',
        'HOST': 'localhost',
        'PORT': '',
    }
}

try:
    from .local import *
except ImportError:
    pass
