FROM python:3.8

COPY ./requirements/base.txt ./requirements/prod.txt /requirements/
RUN pip install --upgrade pip && pip install -r /requirements/prod.txt

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

RUN mkdir -p /static /media

ENV DJANGO_SETTINGS_MODULE=update.settings.dev
ENV PORT 8000
ENV STATIC_ROOT /static
ENV MEDIA_ROOT /media

WORKDIR /app

COPY . /app

RUN python manage.py collectstatic --noinput
RUN python manage.py compilemessages

CMD ["/docker-entrypoint.sh"]
