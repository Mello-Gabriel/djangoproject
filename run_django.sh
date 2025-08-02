#!/bin/bash

# Apply database migrations
python my_site/manage.py migrate

# Start Django development server
python my_site/manage.py runserver 0.0.0.0:8000
