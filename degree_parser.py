# degree_parser.py
def load_degree(degree_name="business administration"):
    """
    Load degree requirements for the specified degree.
    Currently returns stub data; later can load real catalog info.
    """
    # Replace this stub with actual degree parsing from a catalog later
    return {
        "degree_name": degree_name,
        "total_credits": 120,
        "requirements": [
            {"category": "Core", "credits": 60, "courses": ["Intro to Business", "Accounting 101", "Management 101"]},
            {"category": "Elective", "credits": 60, "courses": ["Marketing Basics", "Finance Fundamentals"]}
        ]
    }

def normalize_degree(degree_data):
    """
    Normalize course names and requirements.
    """
    # For now, just pass through
    return degree_data
