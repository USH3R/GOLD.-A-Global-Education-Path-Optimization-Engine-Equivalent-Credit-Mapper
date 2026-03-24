import copy

def map_courses_to_degree(courses_taken, degree):
    """
    Map a user's completed courses to the required courses for a degree.

    Args:
        courses_taken (list[str]): List of courses the user has already completed.
        degree (dict): Degree dictionary loaded from degrees.json. Should contain:
            - "required_courses" (list)
            - "electives" (list, optional)
            - "total_credits" (int)

    Returns:
        dict: {
            "degree": str,
            "courses_needed": list,
            "total_credits": int,
            "transferable_credits": int
        }
    """
    if not degree or "required_courses" not in degree:
        return {
            "degree": degree.get("name", "Unknown") if isinstance(degree, dict) else "Unknown",
            "courses_needed": [],
            "total_credits": 0,
            "transferable_credits": 0,
            "error": "Invalid degree data"
        }

    # Deep copy to avoid modifying original lists
    required_courses = copy.deepcopy(degree.get("required_courses", []))
    electives = copy.deepcopy(degree.get("electives", []))
    total_credits = degree.get("total_credits", 0)

    # Track courses still needed
    courses_needed = []

    # Track transferable credits (courses user has already taken that match requirements)
    transferable_credits = 0

    # Check required courses
    for course in required_courses:
        if course in courses_taken:
            transferable_credits += 3  # assume each course is 3 credits
        else:
            courses_needed.append(course)

    # Check electives if any
    for course in electives:
        if course in courses_taken:
            transferable_credits += 3
        else:
            courses_needed.append(course)

    return {
        "degree": degree.get("name", "Unknown"),
        "courses_needed": courses_needed,
        "total_credits": total_credits,
        "transferable_credits": transferable_credits
    }import json
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
