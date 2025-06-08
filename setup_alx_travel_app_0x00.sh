#!/bin/bash

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Run seed command
python manage.py seed

# Start server
python manage.py runserver
