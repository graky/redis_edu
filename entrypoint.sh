#!/bin/sh
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py makephrases --noinput
gunicorn djanredis.wsgi:application --bind 0.0.0.0:8000