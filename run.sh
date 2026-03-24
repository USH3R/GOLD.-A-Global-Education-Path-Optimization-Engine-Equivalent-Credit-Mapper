#!/bin/bash
echo "-------------------------------------------"
echo "Starting Gold app..."
echo "-------------------------------------------"

# Activate virtual environment
source venv/bin/activate

# Upgrade pip just in case
pip install --upgrade pip

# Install required packages
pip install flask requests beautifulsoup4 pandas

# Run Flask app
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=5000
