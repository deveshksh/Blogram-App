#!/bin/bash

echo "BUILD START"

# Activate your virtual environment (if using one)
# source /path/to/your/venv/bin/activate

# Install dependencies
python3.9 -m pip install -r requirements.txt

# Collect static files
python3.9 manage.py collectstatic --noinput --clear

echo "BUILD END"
