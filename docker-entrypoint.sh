#!/bin/sh

python manage.py migrate --noinput
uwsgi --ini /app/update/uwsgi.ini
