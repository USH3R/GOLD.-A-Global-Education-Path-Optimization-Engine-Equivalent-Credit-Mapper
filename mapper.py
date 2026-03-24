# mapper.py
from degree_parser import load_degree

def map_courses_to_degree(degree_name):
    """
    Map the loaded degree to the courses and return full stats.
    """
    degree_data = load_degree(degree_name)

    # If there's an error in loading, return immediately
    if "error" in degree_data:
        return {
            "degree": degree_name,
            "courses_needed": [],
            "total_credits": 0,
            "transferable_credits": 0,
            "error": degree_data["error"]
        }

    # Build the mapped response
    mapped = degree_data.get("courses_needed", [])
    total_credits = degree_data.get("total_credits", 0)
    transferable_credits = degree_data.get("transferable_credits", 0)

    return {
        "degree": degree_name,
        "courses_needed": mapped,
        "total_credits": total_credits,
        "transferable_credits": transferable_credits
    }
