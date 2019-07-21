import os
from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    'localhost', '127.0.0.1',
    'up2date.kz',
    'www.up2date.kz',
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

STATIC_ROOT = '/var/www/static'

MEDIA_ROOT = '/var/www/media'

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = False
#COMPRESS_CSS_FILTERS = ['compressor.filters.cssmin.CSSCompressorFilter']
#COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.SlimItFilter']

WAGTAILIMAGES_JPEG_QUALITY = 80

WAGTAIL_ENABLE_UPDATE_CHECK = False

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': oS.getenv('DB_PORT', ''),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'localhost:6379',
    }
}

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

try:
    from .local import *
except ImportError:
    pass
