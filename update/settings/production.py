from .base import *

DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'update-architects.com',
                 '139.162.175.130']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(b56aueko1(^$72ce5%7xh5feejh&64&h_tbh%1476vv1ubjpm'

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
