# optimizer.py

def optimize_path(mapped_data):
    """
    Take mapped courses and create optimized path.
    Strategy:
        - Max transferable credits
        - Minimize cost
        - Minimize duration
    """
    mapped_courses = mapped_data.get("mapped_courses", [])
    total_cost = sum(c.get("cost", 0) for c in mapped_courses)
    total_duration_weeks = sum(c.get("duration_weeks", 0) for c in mapped_courses)

    return {
        "degree": mapped_data["degree_name"],
        "total_cost": total_cost,
        "total_duration_weeks": total_duration_weeks,
        "courses_needed": [c["title"] for c in mapped_courses],
        "transferable_credits": mapped_data.get("transferable_credits", 0)
    }

if __name__ == "__main__":
    import json
    sample_mapped = {
        "degree_name": "Business Admin",
        "mapped_courses": [
            {"title": "Intro to Business", "credits": 3, "cost": 50, "duration_weeks": 4}
        ],
        "transferable_credits": 3
    }
    optimized = optimize_path(sample_mapped)
    print(json.dumps(optimized, indent=4))
