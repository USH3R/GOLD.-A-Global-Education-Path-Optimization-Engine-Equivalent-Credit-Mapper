#!/bin/bash

echo "-------------------------------------------"
echo "Starting Gold app..."
echo "-------------------------------------------"

# 1️⃣ Create Python virtual environment if not exists
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

# 2️⃣ Activate virtual environment
source venv/bin/activate

# 3️⃣ Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# 4️⃣ Install required Python packages
echo "Installing required packages..."
pip install flask requests beautifulsoup4 pandas

# 5️⃣ Check if app.py exists
if [ ! -f "app.py" ]; then
    echo "Error: app.py not found in repo root!"
    exit 1
fi

# 6️⃣ Inform user and run Flask app
echo "-------------------------------------------"
echo "Access the app in your browser:"
echo "Use the Codespaces 'Ports' panel to open in a new tab."
echo "-------------------------------------------"

# 7️⃣ Start Flask app
#    host 0.0.0.0 allows Codespaces to expose the port to browser
FLASK_APP=app.py flask run --host=0.0.0.0 --port=5000#!/bin/bash
# run.sh — starts the Gold app in Codespaces with one command

echo "-------------------------------------------"
echo "Starting Gold app..."
echo "-------------------------------------------"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install required packages
echo "Installing required packages..."
pip install flask requests beautifulsoup4 pandas

# Inform the user
echo "-------------------------------------------"
echo "Access the app in your browser:"
echo "http://localhost:5000"
echo "Use the Codespaces 'Ports' panel to open in a new tab."
echo "-------------------------------------------"

# Run the Flask app
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=5000#!/bin/bash

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
