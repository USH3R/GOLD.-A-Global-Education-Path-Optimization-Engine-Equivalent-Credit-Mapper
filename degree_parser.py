import json
import difflib
from typing import Dict, Any, Optional
import os

DEGREES_DB_FILE = os.path.join(os.path.dirname(__file__), "degrees.json")

def load_degrees() -> Dict[str, Any]:
    """Load degree definitions from the JSON database."""
    try:
        with open(DEGREES_DB_FILE, "r", encoding="utf-8") as f:
            degrees = json.load(f)
        return degrees
    except FileNotFoundError:
        print(f"Error: {DEGREES_DB_FILE} not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: {DEGREES_DB_FILE} contains invalid JSON.")
        return {}

def normalize_degree(name: str) -> str:
    """Lowercase and strip whitespace for consistent matching."""
    return name.strip().lower()

def find_degree(degree_name: str, degrees: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Return the degree dictionary matching the input name."""
    normalized_input = normalize_degree(degree_name)

    # Exact match first
    for key, value in degrees.items():
        if normalize_degree(key) == normalized_input:
            return value

    # Fuzzy match if exact fails
    degree_keys = list(degrees.keys())
    degree_keys_normalized = [normalize_degree(k) for k in degree_keys]
    matches = difflib.get_close_matches(normalized_input, degree_keys_normalized, n=1, cutoff=0.6)
    if matches:
        match_index = degree_keys_normalized.index(matches[0])
        return degrees[degree_keys[match_index]]

    return None

def load_degree(degree_name: str) -> Dict[str, Any]:
    """Load a degree by name; return error if not found."""
    degrees = load_degrees()
    degree = find_degree(degree_name, degrees)
    if degree is None:
        return {"error": f"Degree '{degree_name}' not found in database."}
    return degree
