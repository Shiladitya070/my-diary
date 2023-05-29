#!/bin/bash

echo "Installing dependencies..."
python3.9 -m pip install -r requirements.txt
echo "done Installing :)"
echo "Collecting static"
python3.9 manage.py collectstatic  --noinput --clear    
echo "Collecting static"



