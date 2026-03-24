# mapper.py
"""
Maps crawled courses to degree requirements.
Calculates transferable credits, total cost, and estimated duration.
Outputs structured data ready for optimization.
"""

from collections import defaultdict

def map_courses_to_degree(courses, degree):
    """
    courses: list of dicts from crawl_all()
      example course dict: {
          "title": "Intro to Business",
          "credits": 3,
          "source": "Coursera",
          "cost": 49.99,
          "duration_weeks": 4
      }

    degree: dict from degree_parser
      example: {
          "degree_name": "MBA",
          "total_credits": 60,
          "requirements": [
              {"category": "Core", "credits": 40, "courses": ["Intro to Business", "Accounting"]},
              {"category": "Elective", "credits": 20, "courses": []}
          ]
      }

    returns a dict:
      {
        "degree_name": str,
        "transferable_credits": int,
        "total_cost": float,
        "total_duration_weeks": int,
        "courses_needed": list of strings
      }
    """

    mapped_courses = []
    total_credits = 0
    total_cost = 0
    total_duration = 0
    courses_needed = []

    # Track which degree requirements are already fulfilled
    fulfilled_courses = defaultdict(set)

    for course in courses:
        course_title = course.get("title", "").lower()
        course_credits = course.get("credits", 0)
        course_cost = course.get("cost", 0)
        course_duration = course.get("duration_weeks", 0)

        matched = False
        for req in degree.get("requirements", []):
            for req_course in req.get("courses", []):
                if req_course.lower() in course_title and req_course not in fulfilled_courses[req["category"]]:
                    mapped_courses.append({
                        "course": course_title,
                        "category": req["category"],
                        "credits": course_credits,
                        "cost": course_cost,
                        "duration_weeks": course_duration,
                        "source": course.get("source", "Unknown")
                    })
                    total_credits += course_credits
                    total_cost += course_cost
                    total_duration += course_duration
                    fulfilled_courses[req["category"]].add(req_course)
                    matched = True
                    break
            if matched:
                break

        if not matched:
            # Treat as elective if it doesn't match core
            mapped_courses.append({
                "course": course_title,
                "category": "Elective",
                "credits": course_credits,
                "cost": course_cost,
                "duration_weeks": course_duration,
                "source": course.get("source", "Unknown")
            })
            total_credits += course_credits
            total_cost += course_cost
            total_duration += course_duration

        # Add the course title to the final list of courses needed
        courses_needed.append(course.get("title", "Unknown Course"))

    return {
        "degree_name": degree.get("degree_name", "Unknown Degree"),
        "transferable_credits": total_credits,
        "total_cost": total_cost,
        "total_duration_weeks": total_duration,
        "courses_needed": courses_needed
    }


# --- Quick test when run standalone ---
if __name__ == "__main__":
    # Sample courses
    courses = [
        {"title": "Intro to Business", "credits": 3, "source": "Coursera", "cost": 49.99, "duration_weeks": 4},
        {"title": "Accounting Basics", "credits": 3, "source": "edX", "cost": 59.99, "duration_weeks": 5},
        {"title": "Leadership Skills", "credits": 2, "source": "Saylor", "cost": 0, "duration_weeks": 3}
    ]

    # Sample degree
    degree = {
        "degree_name": "MBA",
        "total_credits": 60,
        "requirements": [
            {"category": "Core", "credits": 40, "courses": ["Intro to Business", "Accounting Basics"]},
            {"category": "Elective", "credits": 20, "courses": []}
        ]
    }

    result = map_courses_to_degree(courses, degree)
    import json
    print(json.dumps(result, indent=4))
