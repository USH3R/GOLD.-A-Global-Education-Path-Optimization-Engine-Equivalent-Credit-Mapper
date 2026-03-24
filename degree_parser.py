def load_degree():
    return {
        "name": "Business Administration",
        "keywords": [
            "business",
            "management",
            "finance",
            "marketing",
            "accounting",
            "operations",
            "economics"
        ]
    }


def normalize_degree(degree):
    # DO NOT strip keywords — just pass through clean
    return {
        "name": degree.get("name", "Unknown"),
        "keywords": degree.get("keywords", [])
    }def load_degree():
    """
    Returns a basic degree structure.
    This is a placeholder until we plug in real university data.
    """
    return {
        "name": "Business Administration",
        "keywords": [
            "business",
            "management",
            "finance",
            "marketing",
            "accounting",
            "operations",
            "economics"
        ]
    }


def normalize_degree(degree):
    """
    Ensures consistent structure for downstream modules.
    """
    if not degree:
        return {"name": "Unknown", "keywords": []}

    name = degree.get("name", "Unknown")
    keywords = degree.get("keywords", [])

    # Normalize everything to lowercase
    keywords = [k.lower() for k in keywords]

    return {
        "name": name,
        "keywords": keywords
    }# degreeparser.py

# Placeholder database of degrees (could later scrape universities)
DEGREE_DB = {
    "business administration": {
        "degree_name": "Business Administration",
        "requirements": [
            {"category": "Core", "credits": 60, "courses": ["Intro to Business", "Accounting 101", "Management 101"]},
            {"category": "Elective", "credits": 60, "courses": ["Marketing Basics", "Economics Basics"]}
        ]
    },
    "mba": {
        "degree_name": "MBA",
        "requirements": [
            {"category": "Core", "credits": 60, "courses": ["Finance", "Leadership", "Strategy"]},
            {"category": "Elective", "credits": 60, "courses": ["Entrepreneurship", "Global Business"]}
        ]
    }
}

def load_degree(degree_name="business administration"):
    # Return degree dict, defaulting to business admin
    return DEGREE_DB.get(degree_name.lower(), DEGREE_DB["business administration"])

def normalize_degree(degree):
    # Just return as-is for now; could standardize course names
    return {
        "degree_name": degree["degree_name"],
        "requirements": degree["requirements"]
    }

if __name__ == "__main__":
    import json
    d = normalize_degree(load_degree("MBA"))
    print(json.dumps(d, indent=4))
