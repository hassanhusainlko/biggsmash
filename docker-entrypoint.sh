#!/bin/sh
set -e

python manage.py migrate
python manage.py collectstatic --noinput --clear

exec gunicorn biggsmash.wsgi:application --bind 0.0.0.0:8001
