import requests
from bs4 import BeautifulSoup
import json

def crawl_coursera(subject="business"):
    url = f"https://www.coursera.org/courses?query={subject}"
    response = requests.get(url)
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

def crawl_all():
    # Placeholder to extend for other sources
    courses = crawl_coursera()
    # Add more crawling functions for edX, Study.com, Saylor, ACE, CLEP
    return courses

if __name__ == "__main__":
    all_courses = crawl_all()
    with open("courses.json", "w") as f:
        json.dump(all_courses, f, indent=4)
