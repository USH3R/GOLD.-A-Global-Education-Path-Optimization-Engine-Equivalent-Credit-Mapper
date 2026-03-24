#!/bin/bash

# -------------------------------------------
# Gold App: Run Script for GitHub Codespaces
# -------------------------------------------

echo "-------------------------------------------"
echo "Starting Gold app..."
echo "-------------------------------------------"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing required packages..."
pip install flask requests beautifulsoup4 pandas

# Ensure Flask app is found
if [ ! -f "app.py" ]; then
    echo "Error: app.py not found in repo root!"
    exit 1
fi

# Inform user how to access app
echo "-------------------------------------------"
echo "Access the app in your browser:"
echo "http://localhost:5000"
echo "Use the Codespaces 'Ports' panel to open in a new tab."
echo "-------------------------------------------"

# Run Flask app
export FLASK_APP=app.py
export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=5000
flask run
