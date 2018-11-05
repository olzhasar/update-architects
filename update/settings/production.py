from .base import *
from .secret_settings import *

DEBUG = False

ALLOWED_HOSTS = [
    'localhost', '127.0.0.1',
    'up2date.kz',
    'www.up2date.kz',
]

STATIC_ROOT = '/var/www/static'

MEDIA_ROOT = '/var/www/media'

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = ['compressor.filters.cssmin.CSSCompressorFilter']
COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.SlimItFilter']

WAGTAILIMAGES_JPEG_QUALITY = 80

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

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

try:
    from .local import *
except ImportError:
    pass
