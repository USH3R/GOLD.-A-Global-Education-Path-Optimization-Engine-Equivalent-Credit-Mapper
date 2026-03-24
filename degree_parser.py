import json

def load_degree(filename="degree.json"):
    with open(filename, "r") as f:
        return json.load(f)

def normalize_degree(degree):
    # Normalize course names and structure
    for req in degree.get("requirements", []):
        req["courses"] = [course.strip().lower() for course in req.get("courses", [])]
    return degree

if __name__ == "__main__":
    degree = {
        "name": "Master of Business Administration",
        "total_credits": 36,
        "requirements": [
            {"category": "Core", "credits": 24, "courses": ["Accounting", "Finance", "Marketing"]},
            {"category": "Elective", "credits": 12, "courses": []}
        ]
    }
    with open("degree.json", "w") as f:
        json.dump(degree, f, indent=4)
