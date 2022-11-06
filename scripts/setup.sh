#!/bin/bash

# update pip
python3 -m pip install --upgrade pip

# install virtualenv
python3 -m pip install virtualenv

# create the virtual environment
python3 -m virtualenv venv

# activate virtualenv
source venv/bin/activate

# update pip
pip install --upgrade pip

# install dependencies
pip install -r requirements.txt
