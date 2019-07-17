#!/bin/bash

# Start Gunicorn processes
echo Now starting Gunicorn.
exec gunicorn scr.wsgi:application --bind 0.0.0.0:8000 --workers 3
