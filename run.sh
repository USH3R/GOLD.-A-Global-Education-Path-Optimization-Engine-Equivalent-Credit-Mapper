#!/bin/bash

echo "-------------------------------------------"
echo "Starting Gold app..."
echo "-------------------------------------------"

# Create virtual environment if missing
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate venv
source venv/bin/activate

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install flask requests beautifulsoup4 pandas

# Run Flask app
export FLASK_APP=app.py
flask run --host=0.0.0.0 --port=5000
