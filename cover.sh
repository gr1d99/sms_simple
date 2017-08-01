#!/bin/bash

# clean up previous results:
rm htmlcov/*
rm .coverage

# I do not want coverage data for my South migrations:
PARMS=--omit='*migrations*'

# run the tests and collect coverage, only for sms_simple app
coverage run --source=sms_simple /root/PycharmProjects/SMS/manage.py test

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