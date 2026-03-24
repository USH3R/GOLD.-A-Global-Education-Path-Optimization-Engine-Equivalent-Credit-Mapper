def optimize_path(mapped_data):
    courses = mapped_data.get("mapped_courses", [])

    if not courses:
        return {
            "degree": mapped_data.get("degree"),
            "total_cost": 0,
            "total_duration_weeks": 0,
            "courses_needed": [],
            "transferable_credits": 0
        }

    # Sort by best match score
    courses = sorted(courses, key=lambda x: x["score"], reverse=True)

    total_cost = sum(c["cost"] for c in courses)
    total_duration = sum(c["duration_weeks"] for c in courses)
    total_credits = sum(c["credits"] for c in courses)

    return {
        "degree": mapped_data.get("degree"),
        "total_cost": total_cost,
        "total_duration_weeks": total_duration,
        "courses_needed": [c["title"] for c in courses],
        "transferable_credits": total_credits
    }
