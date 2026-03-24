import json
import os

DEGREES_FILE = os.path.join(os.path.dirname(__file__), "degrees.json")

def load_degrees():
    """Load all degrees from the JSON database."""
    try:
        with open(DEGREES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading degrees.json: {e}")
        return {}

def normalize_degree(degree_name):
    """Normalize user input to match degree names in JSON."""
    return degree_name.strip().lower()

def load_degree(degree_name):
    """Return degree courses and metadata for a given degree name."""
    degrees = load_degrees()
    normalized_input = normalize_degree(degree_name)

    # Exact match first
    for key in degrees.keys():
        if key.lower() == normalized_input:
            return degrees[key]

    # If no match, return error object
    return {"error": f"Degree '{degree_name}' not found in database."}
