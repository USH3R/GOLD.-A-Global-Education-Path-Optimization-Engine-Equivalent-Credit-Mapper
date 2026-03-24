#!/bin/bash

# -------------------------------
# Gold Application Launcher Script
# -------------------------------
# This script sets up the environment and runs the Gold app
# in development mode. It is compatible with GitHub Codespaces,
# Linux, and macOS terminals.
# -------------------------------

# Step 1: Set environment variables
export FLASK_APP=app.py         # Main Flask file
export FLASK_ENV=development    # Enables debug/reload mode

# Step 2: Set default host and port
HOST=0.0.0.0
PORT=5000

# Step 3: Print startup message
echo "-------------------------------------------"
echo "Starting Gold app..."
echo "Access the app at: http://localhost:$PORT"
echo "-------------------------------------------"

# Step 4: Start Flask server in background
# & allows you to run optional browser open commands afterward
flask run --host=$HOST --port=$PORT &

# Capture the Flask process ID so we can manage it if needed
FLASK_PID=$!

# Step 5 (Optional): Attempt to open browser automatically
# Works for Linux and macOS. Silently fails if not available.
xdg-open http://localhost:$PORT 2>/dev/null || open http://localhost:$PORT 2>/dev/null || echo "Open the URL manually in your browser."

# Step 6: Wait for Flask process
wait $FLASK_PID
