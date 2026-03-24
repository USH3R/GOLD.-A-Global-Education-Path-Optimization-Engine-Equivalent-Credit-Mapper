#!/bin/bash
# ------------------------------------------------
# Gold App: Codespaces-ready launcher
# ------------------------------------------------

echo "-------------------------------------------"
echo "Starting Gold app..."
echo "-------------------------------------------"

# Step 1: Create virtual environment if missing
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

# Step 2: Activate virtual environment
source venv/bin/activate

# Step 3: Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Step 4: Install dependencies
echo "Installing required packages..."
pip install flask requests beautifulsoup4 pandas

# Step 5: Run Flask app
echo "-------------------------------------------"
echo "Access the app in your browser:"
echo " - Use Codespaces 'Ports' panel to open http://localhost:5000 in a new tab"
echo "-------------------------------------------"

# Run app.py with Flask
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=5000
