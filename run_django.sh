#!/bin/bash

# Wait for PostgreSQL to be ready
# This is a simple wait, for production, consider a more robust solution
until pg_isready -h db -p 5432 -U djangouser
do
  echo "Waiting for PostgreSQL..."
  sleep 2
done

# Apply database migrations
python my_site/manage.py migrate

# Start Django development server
python my_site/manage.py runserver 0.0.0.0:8000
