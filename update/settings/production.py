from .base import *
from .secret_settings import *

DEBUG = False

ALLOWED_HOSTS = [
    'localhost', '127.0.0.1',
    'update-architects.com',
    'www.update-architects.com'
]

STATIC_ROOT = '/var/www/static'

MEDIA_ROOT = '/var/www/media'

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = ['compressor.filters.cssmin.CSSCompressorFilter']
COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.SlimItFilter']

WAGTAILIMAGES_JPEG_QUALITY = 70

WAGTAIL_ENABLE_UPDATE_CHECK = False

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
