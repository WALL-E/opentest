#!/bin/bash


/usr/local/bin/gunicorn --worker-class=gevent project.wsgi:application -b 0.0.0.0:8000
#
# DEBUG
#
# python3.6 manage.py runserver 0.0.0.0:8000
# DJANGO_SETTINGS_MODULE=project.settings python3.6 manage.py runserver 0.0.0.0:9000
# DJANGO_SETTINGS_MODULE=project.settings_internal python3.6 manage.py runserver 0.0.0.0:9001
