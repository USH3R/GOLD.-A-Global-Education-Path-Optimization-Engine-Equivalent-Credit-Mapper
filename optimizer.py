import json

def optimize_path(mapped_data):
    # Simple ranking: maximize credits
    total_credits = mapped_data.get("transferable_credits", 0)
    cost = sum(course.get("cost", 0) for course in mapped_data.get("courses_needed", []))
    duration = sum(course.get("duration_weeks", 0) for course in mapped_data.get("courses_needed", []))
    return {
        "degree": mapped_data["degree"],
        "total_credits": total_credits,
        "estimated_cost": cost,
        "estimated_duration_weeks": duration,
        "courses_needed": mapped_data["courses_needed"]
    }

if __name__ == "__main__":
    from mapper import map_courses_to_degree
    from degree_parser import load_degree, normalize_degree
    from crawler import crawl_all

    degree = normalize_degree(load_degree())
    courses = crawl_all()
    mapped = map_courses_to_degree(courses, degree)
    optimized = optimize_path(mapped)
    with open("optimized_path.json", "w") as f:
        json.dump(optimized, f, indent=4)
