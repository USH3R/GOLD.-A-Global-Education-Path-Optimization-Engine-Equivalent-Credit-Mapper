# mapper.py
from degree_parser import load_degree

def map_courses_to_degree(courses_taken, degree_name):
    """
    Map the courses a student has taken to the target degree.
    
    Parameters:
    - courses_taken: list of course names the student has completed
    - degree_name: string of the target degree
    
    Returns:
    A dictionary with:
    - degree
    - courses_needed
    - total_credits
    - transferable_credits
    - error (if any)
    """
    # Load full degree info
    degree = load_degree(degree_name)

    if "error" in degree:
        return {
            "degree": degree_name,
            "courses_needed": [],
            "total_credits": 0,
            "transferable_credits": 0,
            "error": degree["error"]
        }

    # Determine which courses are still needed
    courses_needed = [c for c in degree.get("courses", []) if c not in courses_taken]

    # Mock transferable credits: count of courses already taken
    transferable_credits = len([c for c in courses_taken if c in degree.get("courses", [])])

    return {
        "degree": degree_name,
        "courses_needed": courses_needed,
        "total_credits": len(degree.get("courses", [])),
        "transferable_credits": transferable_credits
    }
