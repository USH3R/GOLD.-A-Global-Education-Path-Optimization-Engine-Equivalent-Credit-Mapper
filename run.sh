#!/bin/bash

echo "-------------------------------------------"
echo "Starting Gold app..."
echo "-------------------------------------------"

# --- Step 1: Create virtual environment if it doesn't exist ---
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

# --- Step 2: Activate virtual environment ---
source venv/bin/activate

# --- Step 3: Upgrade pip ---
echo "Upgrading pip..."
pip install --upgrade pip

# --- Step 4: Install required Python packages ---
echo "Installing required packages..."
pip install flask requests beautifulsoup4 pandas

# --- Step 5: Ensure app.py exists ---
if [ ! -f "app.py" ]; then
    echo "Error: app.py not found in repo root!"
    echo "Make sure you have renamed UI.py to app.py."
    exit 1
fi

# --- Step 6: Set Flask environment variables ---
export FLASK_APP=app.py
export FLASK_ENV=development

# --- Step 7: Run Flask app ---
echo "-------------------------------------------"
echo "Access the app in your browser using the Codespaces 'Ports' panel:"
echo "http://localhost:5000"
echo "-------------------------------------------"

# Open in default browser if Codespaces supports it
flask run --host=0.0.0.0 --port=5000
