def crawl_all(subject="business"):
    # Temporary stub: returns mock courses for testing
    return [
        {"title": "Intro to Business", "credits": 3, "source": "Coursera", "cost": 49.99, "duration_weeks": 4},
        {"title": "Accounting 101", "credits": 3, "source": "Coursera", "cost": 49.99, "duration_weeks": 4},
        {"title": "Marketing Basics", "credits": 3, "source": "Coursera", "cost": 49.99, "duration_weeks": 4}
    ]import requests
from bs4 import BeautifulSoup
import json

def crawl_coursera(subject="business"):
    try:
        url = f"https://www.coursera.org/courses?query={subject}"
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        courses = []
        for div in soup.find_all("div", class_="course-card"):
            title_tag = div.find("h2")
            if title_tag:
                course = {
                    "title": title_tag.text.strip(),
                    "credits": 3,
                    "source": "Coursera",
                    "cost": 49.99,
                    "duration_weeks": 4
                }
                courses.append(course)
        return courses
    except Exception as e:
        print(f"Coursera crawl failed: {e}")
        # fallback mock data
        return [
            {"title": "Intro to Business", "credits": 3, "source": "Coursera", "cost": 49.99, "duration_weeks": 4}
        ]

def crawl_all():
    # Combine Coursera with other placeholders
    courses = crawl_coursera()
    courses += [
        {"title": "Cybersecurity Basics", "credits": 3, "source": "edX", "cost": 59.99, "duration_weeks": 6},
        {"title": "Advanced Algorithms", "credits": 3, "source": "Saylor", "cost": 0, "duration_weeks": 8},
    ]
    return courses

if __name__ == "__main__":
    all_courses = crawl_all()
    with open("courses.json", "w") as f:
        json.dump(all_courses, f, indent=4)
