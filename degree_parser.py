import json

def load_degree():
    # Simple example degree requirements
    return {
        "degree_name": "Business Administration",
        "total_credits": 120,
        "requirements": [
            {"category": "Core", "credits": 60, "courses": ["Intro to Business", "Management 101", "Accounting Basics"]},
            {"category": "Elective", "credits": 60, "courses": ["Cybersecurity Basics", "Advanced Algorithms", "Project Management"]}
        ]
    }

def normalize_degree(degree_data):
    # Convert course names to lowercase for easier matching
    degree_data["requirements"] = [
        {**req, "courses": [c.lower() for c in req["courses"]]} for req in degree_data["requirements"]
    ]
    return degree_data
