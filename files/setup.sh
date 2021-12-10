#!/usr/bin/env bash

python -m django startproject dr_social_backend \
    && cd dr_social_backend \
    && python manage.py collectstatic --noinput \
    && python manage.py runserver 0.0.0.0:8000

