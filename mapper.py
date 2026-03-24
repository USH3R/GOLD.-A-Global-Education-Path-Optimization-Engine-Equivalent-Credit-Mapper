from degree_parser import load_degree

def map_courses_to_degree(courses, degree_name):
    """
    Maps a list of available courses to a target degree.
    Returns required courses, transferable credits, and missing courses.
    """
    degree = load_degree(degree_name)

    # If degree not found
    if "error" in degree:
        return {
            "degree": degree_name,
            "error": degree["error"],
            "courses_needed": [],
            "transferable_credits": 0
        }

    required_courses = [c["name"] for c in degree["courses"]]
    transferable_credits = degree.get("transferable_credits", 0)

    # Determine missing courses
    courses_needed = [c for c in required_courses if c not in courses]

    return {
        "degree": degree_name,
        "courses_needed": courses_needed,
        "transferable_credits": transferable_credits
    }# mapper.py
from degree_parser import load_degree

def calculate_stats(degree_data):
    """
    Example helper to calculate summary stats for a degree.
    """
    stats = {
        "degree": degree_data.get("name", "Unknown"),
        "courses_needed": degree_data.get("courses", []),
        "total_credits": sum(c.get("credits", 0) for c in degree_data.get("courses", [])),
        "transferable_credits": degree_data.get("transferable_credits", 0),
    }
    return stats

def map_courses_to_degree(courses, degree_name):
    """
    Map available courses to the selected degree.
    """
    mapped = []
    transferable_credits = 0

    degree_data = load_degree(degree_name)

    # Check if degree exists
    if "error" in degree_data:
        return {
            "degree": degree_name,
            "courses_needed": [],
            "total_credits": 0,
            "transferable_credits": 0,
            "error": degree_data["error"]
        }

    # Map courses that match degree requirements
    required_courses = degree_data.get("courses", [])
    for course in required_courses:
        course_name = course.get("name")
        course_credits = course.get("credits", 0)
        # Check if course is in available courses
        if course_name in courses:
            transferable_credits += course_credits
        else:
            mapped.append(course)

    # Return mapping stats
    return {
        "degree": degree_data.get("name", degree_name),
        "courses_needed": mapped,
        "total_credits": sum(c.get("credits", 0) for c in required_courses),
        "transferable_credits": transferable_credits
    }
