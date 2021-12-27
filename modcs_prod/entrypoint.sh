#!/bin/sh
set -e

ls -la /home/user/vol/
ls -la /home/user/vol/web

# to clean all informations from database just uncomment this line
#python manage.py flush --no-input

# waiting and checking if database container is up
python manage.py wait_for_db

# preparing models to create database
python manage.py makemigrations


# creating records to models
python manage.py migrate accounts --noinput
python manage.py migrate admin --noinput
python manage.py migrate auth --noinput
python manage.py migrate contenttypes --noinput
python manage.py migrate sessions --noinput

# django_plotly_dash has a problem when using pymongo, so we have to fake migrate
python manage.py migrate django_plotly_dash --fake --noinput

# uncomment this line to create django superuser 
#python manage.py createsuperuser --noinput

#unset DJANGO_SUPERUSER_PASSWORD && unset DJANGO_SUPERUSER_USERNAME && unset DJANGO_SUPERUSER_EMAIL

python manage.py collectstatic --noinput

gunicorn app.wsgi:application --bind 0.0.0.0:8000