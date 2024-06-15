#!/bin/bash

# Install Flask-Migrate
pip install Flask-Migrate

# Run database migrations
flask db upgrade

# Start the Gunicorn server
gunicorn --bind 0.0.0.0:8000 app:app
