import json
import os
import difflib
from typing import Dict, Any, Optional

# Path to the JSON database
DEGREES_FILE = os.path.join(os.path.dirname(__file__), "degrees.json")

def load_degrees() -> Dict[str, Any]:
    """Load all degrees from the JSON database."""
    try:
        with open(DEGREES_FILE, "r", encoding="utf-8") as f:
            degrees = json.load(f)
        return degrees
    except FileNotFoundError:
        print(f"Error: {DEGREES_FILE} not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: {DEGREES_FILE} contains invalid JSON.")
        return {}

def normalize_degree(name: str) -> str:
    """Normalize input for matching."""
    return name.strip().lower()

def find_degree(degree_name: str, degrees: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """
    Return the full degree dictionary matching the input name.
    Uses exact match first, then fuzzy matching.
    """
    normalized_input = normalize_degree(degree_name)

    # Exact match
    for key, value in degrees.items():
        if normalize_degree(key) == normalized_input:
            return value

    # Fuzzy match
    degree_keys = list(degrees.keys())
    degree_keys_normalized = [normalize_degree(k) for k in degree_keys]
    matches = difflib.get_close_matches(normalized_input, degree_keys_normalized, n=1, cutoff=0.6)
    if matches:
        match_index = degree_keys_normalized.index(matches[0])
        return degrees[degree_keys[match_index]]

    return None

def load_degree(degree_name: str) -> Dict[str, Any]:
    """
    Load a full degree dictionary by name.
    Returns error dict if not found.
    """
    degrees = load_degrees()
    degree = find_degree(degree_name, degrees)
    if degree is None:
        return {
            "degree": degree_name,
            "courses_needed": [],
            "total_credits": 0,
            "transferable_credits": 0,
            "error": f"Degree '{degree_name}' not found in database."
        }
    return degree
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
