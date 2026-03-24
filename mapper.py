import json

def map_courses_to_degree(courses, degree):
    mapped_courses = []
    transferable_credits = 0
    for course in courses:
        course_name = course["title"].lower()
        for req in degree["requirements"]:
            for req_course in req["courses"]:
                if req_course in course_name:
                    mapped_courses.append(course)
                    transferable_credits += course["credits"]
    return {
        "degree": degree["name"],
        "transferable_credits": transferable_credits,
        "courses_needed": [req["courses"] for req in degree["requirements"]]
    }

if __name__ == "__main__":
    from degree_parser import load_degree, normalize_degree
    from crawler import crawl_all

    degree = normalize_degree(load_degree())
    courses = crawl_all()
    result = map_courses_to_degree(courses, degree)
    with open("mapped_results.json", "w") as f:
        json.dump(result, f, indent=4)
