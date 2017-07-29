#!/bin/bash
source /home/virtualenvs/py27/bin/activate
cd /root/PycharmProjects/django_apps/sms_simple
pip install -r requirements.txt
cd ..
python manage.py migrate
python manage.py test --noinput sms_simple
cd /root/PycharmProjects/django_apps/sms_simple
