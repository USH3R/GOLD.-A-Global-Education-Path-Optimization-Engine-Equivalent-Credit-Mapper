import json
from degree_parser import load_degree

def map_courses_to_degree(courses_taken, degree_name):
    """
    Maps a student's taken courses to the target degree.
    Returns courses needed, total credits, and transferable credits.
    """
    # Load full degree info
    degree_data = load_degree(degree_name)

    # If degree not found, return error
    if "error" in degree_data:
        return {
            "degree": degree_name,
            "courses_needed": [],
            "total_credits": 0,
            "transferable_credits": 0,
            "error": degree_data["error"]
        }

    all_courses = degree_data.get("courses", [])
    total_credits = sum(course.get("credits", 0) for course in all_courses)

    # Determine which courses the student still needs
    courses_needed = [
        course for course in all_courses if course["name"] not in courses_taken
    ]

    # Simulate transferable credits (for now, just count taken courses that match degree courses)
    transferable_credits = sum(
        course["credits"]
        for course in all_courses
        if course["name"] in courses_taken
    )

    return {
        "degree": degree_name,
        "courses_needed": courses_needed,
        "total_credits": total_credits,
        "transferable_credits": transferable_credits
    }
