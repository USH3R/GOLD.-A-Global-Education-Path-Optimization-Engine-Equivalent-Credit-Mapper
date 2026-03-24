import json
import os

# Path to the degrees database
DEGREES_FILE = os.path.join(os.path.dirname(__file__), "degrees.json")

def load_degrees():
    """Load all degrees from the JSON database."""
    try:
        with open(DEGREES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {DEGREES_FILE} not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: {DEGREES_FILE} contains invalid JSON.")
        return {}

def normalize_degree(degree_name):
    """
    Normalize user input to match degree names in JSON.
    Lowercase and strip whitespace for consistent matching.
    """
    if not degree_name:
        return None
    return degree_name.strip().lower()

def find_degree(degree_name, degrees):
    """
    Find a degree dictionary by name, using exact match first.
    """
    normalized_input = normalize_degree(degree_name)
    for key in degrees.keys():
        if key.lower() == normalized_input:
            return degrees[key]
    return None

def load_degree(degree_name):
    """
    Load a degree by name. Returns a dict with courses and metadata,
    or an error dict if not found.
    """
    degrees = load_degrees()
    degree = find_degree(degree_name, degrees)
    if degree is None:
        return {"error": f"Degree '{degree_name}' not found in database."}
    return degree
