def map_courses_to_degree(courses, degree):
    mapped = []
    transferable_credits = 0

    # Extract keywords from degree name
    degree_keywords = degree.get("name", "").lower().split()

    for course in courses:
        title = course.get("title", "").lower()

        # Simple keyword match (loose matching)
        match_score = sum(1 for word in degree_keywords if word in title)

        if match_score > 0:
            mapped.append({
                "title": course["title"],
                "credits": course.get("credits", 3),
                "cost": course.get("cost", 0),
                "duration_weeks": course.get("duration_weeks", 0),
                "score": match_score
            })
            transferable_credits += course.get("credits", 3)

    return {
        "degree": degree.get("name", "Unknown"),
        "mapped_courses": mapped,
        "transferable_credits": transferable_credits
    }
