#!/usr/bin/env bash

# Export .env in order to create super user with --noinput
if [ -f .env ]
then
  export $(cat .env | sed 's/#.*//g' | xargs)
fi

python manage.py collectstatic --noinput \
  && python manage.py makemigrations \
  && python manage.py migrate \
  && python manage.py createsuperuser --noinput \
  && python manage.py runserver 0.0.0.0:8000

