#!/bin/sh

set -e

flask db upgrade

python /portfolio/insert_data.py

exec gunicorn -b :5000 --access-logfile - --error-logfile - portfolio:portfolio
