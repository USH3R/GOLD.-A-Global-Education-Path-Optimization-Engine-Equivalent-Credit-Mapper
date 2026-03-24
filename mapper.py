# mapper.py
# Maps completed courses to degree requirements

def map_courses_to_degree(courses, degree_info):
    """
    Given a list of completed courses and a degree_info dictionary,
    returns a list of courses still needed to complete the degree.
    """
    required_courses = degree_info.get("courses", [])
    courses_needed = [course for course in required_courses if course not in courses]
    return courses_needed


def calculate_degree_stats(courses_needed, degree_info):
    """
    Returns a dictionary with total duration, cost, and transferable credits
    based on the courses needed.
    """
    num_courses = len(courses_needed)
    stats = {
        "total_duration_weeks": num_courses * degree_info.get("duration_weeks", 0),
        "total_cost": num_courses * degree_info.get("cost", 0),
        "transferable_credits": num_courses * degree_info.get("transferable_credits", 0)
    }
    return statsdef map_courses_to_degree(courses, degree):
    mapped = []
    transferable_credits = 0

    keywords = degree.get("keywords", [])

    print("DEBUG KEYWORDS:", keywords)

    for course in courses:
        title = course.get("title", "").lower()
        print("CHECKING COURSE:", title)

        match_score = 0

        for keyword in keywords:
            if keyword.lower() in title:
                match_score += 1

        print("MATCH SCORE:", match_score)

        if match_score > 0:
            mapped.append({
                "title": course["title"],
                "credits": course.get("credits", 3),
                "cost": course.get("cost", 0),
                "duration_weeks": course.get("duration_weeks", 0),
                "score": match_score
            })

            transferable_credits += course.get("credits", 3)

    print("MAPPED COURSES:", mapped)

    return {
        "degree": degree.get("name", "Unknown"),
        "mapped_courses": mapped,
        "transferable_credits": transferable_credits
    }def map_courses_to_degree(courses, degree):
    mapped = []
    transferable_credits = 0

    keywords = degree.get("keywords", [])

    for course in courses:
        title = course.get("title", "").lower()

        match_score = 0

        # Check every keyword against the course title
        for keyword in keywords:
            if keyword in title:
                match_score += 1

        # If ANY match, include the course
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
    }def map_courses_to_degree(courses, degree):
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
