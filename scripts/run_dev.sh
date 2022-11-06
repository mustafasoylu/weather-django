#!/bin/sh

# set environment variables
export DEBUG=True

# activate virtualenv
source venv/bin/activate

# run the application
python manage.py runserver
