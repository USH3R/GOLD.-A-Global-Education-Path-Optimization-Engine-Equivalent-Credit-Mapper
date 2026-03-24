#!/bin/bash

echo "-------------------------------------------"
echo "Starting Gold app..."
echo "-------------------------------------------"

# Step 1: Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

# Step 2: Activate virtual environment
source venv/bin/activate

# Step 3: Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Step 4: Install required Python packages
echo "Installing required packages..."
pip install flask requests beautifulsoup4 pandas

# Step 5: Run Flask app on all interfaces for Codespaces
# Flask app should be named app.py
export FLASK_APP=app.py
export FLASK_RUN_HOST=0.0.0.0
export FLASK_ENV=development

echo "-------------------------------------------"
echo "Access the app in your browser:"
echo "Use the Codespaces 'Ports' panel to open in a new tab."
echo "-------------------------------------------"

# Step 6: Launch Flask
flask run
