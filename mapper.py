def map_courses_to_degree(courses, degree):
    mapped_courses = []
    transferable_credits = 0

    for course in courses:
        course_name_lower = course["title"].lower()
        for req in degree["requirements"]:
            for required_course in req["courses"]:
                if required_course in course_name_lower or course_name_lower in required_course:
                    mapped_courses.append(course)
                    transferable_credits += course["credits"]

    return {
        "degree": degree["degree_name"],
        "transferable_credits": transferable_credits,
        "courses_needed": [req["courses"] for req in degree["requirements"]],
        "total_cost": sum(c["cost"] for c in mapped_courses),
        "total_duration_weeks": sum(c["duration_weeks"] for c in mapped_courses)
    }
