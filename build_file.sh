#!/bin/bash

echo "Installing dependencies..."
python3 -m pip install -r requirements.txt
echo "done Installing :)"
echo "Collecting static"
python3 manage.py collectstatic  --noinput --clear    
echo "Collecting static done :)"

echo "making migrations"
python3 manage.py makemigrations
echo "migrate..."
python3 manage.py migrate
echo "done migartion :)"




