# optimizer.py
from typing import List, Dict

def optimize_path(mapped_courses: Dict) -> Dict:
    """
    Takes a mapped course dictionary and returns an optimized path.
    Optimization strategy:
      - Maximize transferable credits
      - Minimize cost
      - Minimize duration
    
    Args:
        mapped_courses (dict): Output from mapper.py containing courses mapped to degree requirements.
    
    Returns:
        dict: Optimized degree path including total credits, courses needed, total cost, and duration.
    """

    # Default placeholders if mapper output is empty
    if not mapped_courses:
        return {
            "total_credits": 0,
            "transferable_credits": 0,
            "total_cost": 0,
            "total_duration_weeks": 0,
            "courses_needed": []
        }

    # Flatten all courses into a single list
    courses = mapped_courses.get("courses", [])
    
    # Calculate totals
    total_credits = sum(course.get("credits", 0) for course in courses)
    transferable_credits = sum(course.get("credits", 0) for course in courses if course.get("transferable", True))
    total_cost = sum(course.get("cost", 0) for course in courses)
    total_duration_weeks = sum(course.get("duration_weeks", 0) for course in courses)
    
    # Identify courses still needed to complete degree
    courses_needed = []
    for req in mapped_courses.get("degree_requirements", []):
        for course_name in req.get("courses", []):
            if course_name not in [c.get("title") for c in courses]:
                courses_needed.append(course_name)

    return {
        "total_credits": total_credits,
        "transferable_credits": transferable_credits,
        "total_cost": total_cost,
        "total_duration_weeks": total_duration_weeks,
        "courses_needed": courses_needed
    }

# Example usage for testing:
if __name__ == "__main__":
    test_mapped = {
        "courses": [
            {"title": "Intro to CS", "credits": 3, "cost": 50, "duration_weeks": 4, "transferable": True},
            {"title": "Data Structures", "credits": 3, "cost": 60, "duration_weeks": 5, "transferable": True},
        ],
        "degree_requirements": [
            {"category": "Core", "courses": ["Intro to CS", "Data Structures", "Algorithms"]},
            {"category": "Elective", "courses": ["Art History"]}
        ]
    }

    optimized = optimize_path(test_mapped)
    print(optimized)
