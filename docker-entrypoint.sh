#!/bin/bash

python manage.py migrate
python manage.py collectstatic --no-input

exec gunicorn challenge.wsgi:application --bind 0.0.0.0:8000 --capture-output