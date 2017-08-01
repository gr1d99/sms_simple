#!/bin/bash
source /home/virtualenvs/py27/bin/activate
cd /root/PycharmProjects/django_apps/sms_simple
pip install -r requirements.txt
cd ..
python manage.py migrate
python manage.py makemigrations
python manage.py migrate

# clean up previous results:
rm htmlcov/*
rm .coverage

# I do not want coverage data for my South migrations:
PARMS=--omit='*migrations*'

# run the tests and collect coverage, only for sms_simple app
coverage run --source=sms_simple /root/PycharmProjects/django_apps/manage.py test
python manage.py jenkins

# generate plaintext and HTML report
echo "----------------------------"
echo "Coverage results:"
coverage report $PARMS
coverage html $PARMS
echo "HTML report generated in htmlcov/index.html"

# optionally display an HTML report
if [ "$1" == "-f" ]
then
  firefox htmlcov/index.html
fi
cd /root/PycharmProjects/django_apps/sms_simple
