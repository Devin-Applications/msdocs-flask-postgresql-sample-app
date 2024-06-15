#!/bin/bash

# Install Flask-Migrate
echo "Installing Flask-Migrate..."
pip install Flask-Migrate

# Verify Flask-Migrate installation
echo "Verifying Flask-Migrate installation..."
pip show Flask-Migrate

# Run database migrations
echo "Running database migrations..."
flask db upgrade

# Start the Gunicorn server
echo "Starting Gunicorn server..."
gunicorn --bind 0.0.0.0:8000 app:app

# Check if Gunicorn is running and listening on port 8000
if ! lsof -i:8000 | grep LISTEN; then
  echo "Gunicorn is not running or not listening on port 8000. Outputting logs for investigation."
  cat /home/LogFiles/2024_06_15_RD0003FFB1E4C0_default_docker.log
fi
