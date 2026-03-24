# mapper.py

def map_courses_to_degree(courses, degree):
    """
    Map available courses to the degree requirements.
    Returns dict ready for optimization.
    """
    mapped_courses = []
    transferable_credits = 0

    # Simple mapping: match course titles if substring in requirement
    for req in degree["requirements"]:
        req_courses = req["courses"]
        for course in courses:
            for r_course in req_courses:
                if course["title"].lower() in r_course.lower() or r_course.lower() in course["title"].lower():
                    mapped_courses.append(course)
                    transferable_credits += course["credits"]

    return {
        "degree_name": degree["degree_name"],
        "requirements": degree["requirements"],
        "mapped_courses": mapped_courses,
        "transferable_credits": transferable_credits
    }

if __name__ == "__main__":
    import json
    sample_courses = [{"title": "Intro to Business", "credits": 3}]
    degree = {
        "degree_name": "Business Admin",
        "requirements": [{"category": "Core", "credits": 60, "courses": ["Intro to Business"]}]
    }
    mapped = map_courses_to_degree(sample_courses, degree)
    print(json.dumps(mapped, indent=4))
