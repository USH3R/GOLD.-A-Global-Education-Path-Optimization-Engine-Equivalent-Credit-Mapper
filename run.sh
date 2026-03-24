#!/bin/bash

# -----------------------------
# Gold App Launcher - run.sh
# Fully automated for Codespaces / Linux
# -----------------------------

# Repo root assumed
echo "-------------------------------------------"
echo "Starting Gold app..."
echo "-------------------------------------------"

# --- Step 1: Check for Python 3 ---
if ! command -v python3 &> /dev/null
then
    echo "Python3 not found. Install Python3 to continue."
    exit 1
fi

# --- Step 2: Create virtual environment if missing ---
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

# --- Step 3: Activate virtual environment ---
source venv/bin/activate

# --- Step 4: Install required packages ---
echo "Installing dependencies..."
pip install --upgrade pip
pip install flask requests beautifulsoup4 pandas

# --- Step 5: Run Flask app ---
export FLASK_APP=app.py
export FLASK_ENV=development

# Attempt to open browser automatically
URL="http://localhost:5000"
if command -v xdg-open &> /dev/null; then
    xdg-open $URL
elif command -v gnome-open &> /dev/null; then
    gnome-open $URL
else
    echo "Could not automatically open browser."
fi

# Run the Flask app
flask run --host=0.0.0.0 --port=5000
