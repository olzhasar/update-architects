from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(b56aueko1(^$72ce5%7xh5feejh&64&h_tbh%1476vv1ubjpm'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'update',
        'USER': 'update',
        'PASSWORD': 'update',
        'HOST': 'localhost',
        'PORT': '',
    }
}


try:
    from .local import *
except ImportError:
    pass
