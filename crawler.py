def crawl_all():
    """
    Stable course dataset (no fragile scraping)
    """

    return [
        # --- BUSINESS ---
        {"title": "Business Management Basics", "credits": 3, "cost": 50, "duration_weeks": 4},
        {"title": "Operations Management", "credits": 3, "cost": 60, "duration_weeks": 5},
        {"title": "Introduction to Finance", "credits": 3, "cost": 70, "duration_weeks": 6},
        {"title": "Marketing Fundamentals", "credits": 3, "cost": 50, "duration_weeks": 4},
        {"title": "Principles of Accounting", "credits": 3, "cost": 80, "duration_weeks": 6},
        {"title": "Microeconomics", "credits": 3, "cost": 40, "duration_weeks": 3},

        # --- CYBERSECURITY ---
        {"title": "Cybersecurity Basics", "credits": 3, "cost": 100, "duration_weeks": 6},
        {"title": "Network Security Fundamentals", "credits": 3, "cost": 120, "duration_weeks": 8},
        {"title": "Ethical Hacking Introduction", "credits": 3, "cost": 150, "duration_weeks": 8},
        {"title": "Encryption and Cryptography", "credits": 3, "cost": 130, "duration_weeks": 7},
        {"title": "IT Systems Security", "credits": 3, "cost": 90, "duration_weeks": 5},

        # --- COMPUTER SCIENCE ---
        {"title": "Introduction to Programming", "credits": 3, "cost": 50, "duration_weeks": 4},
        {"title": "Data Structures", "credits": 3, "cost": 70, "duration_weeks": 6},
        {"title": "Algorithms", "credits": 3, "cost": 80, "duration_weeks": 6},
        {"title": "Software Engineering", "credits": 3, "cost": 90, "duration_weeks": 7},
        {"title": "Database Systems", "credits": 3, "cost": 75, "duration_weeks": 5}
    def crawl_all():
    """
    Returns a simulated set of MOOC / ACE-style courses.
    This ensures the engine produces real results immediately.
    """

    courses = [
        {
            "title": "Business Management Basics",
            "credits": 3,
            "cost": 0,
            "duration_weeks": 4,
            "source": "Saylor"
        },
        {
            "title": "Introduction to Finance",
            "credits": 3,
            "cost": 0,
            "duration_weeks": 5,
            "source": "Coursera"
        },
        {
            "title": "Marketing Fundamentals",
            "credits": 3,
            "cost": 0,
            "duration_weeks": 4,
            "source": "edX"
        },
        {
            "title": "Principles of Accounting",
            "credits": 3,
            "cost": 0,
            "duration_weeks": 6,
            "source": "Study.com"
        },
        {
            "title": "Operations Management",
            "credits": 3,
            "cost": 0,
            "duration_weeks": 5,
            "source": "Saylor"
        },
        {
            "title": "Microeconomics",
            "credits": 3,
            "cost": 0,
            "duration_weeks": 4,
            "source": "Coursera"
        },
        {
            "title": "Cybersecurity Basics",
            "credits": 3,
            "cost": 0,
            "duration_weeks": 6,
            "source": "edX"
        }
    ]

    return courses# crawler.py
import requests
from bs4 import BeautifulSoup

def crawl_coursera(subject="business"):
    url = f"https://www.coursera.org/courses?query={subject}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    courses = []

    # Example: scrape titles (placeholder logic)
    for div in soup.find_all("div", class_="course-card"):
        title_tag = div.find("h2")
        if title_tag:
            courses.append({
                "title": title_tag.text.strip(),
                "credits": 3,  # placeholder credit
                "source": "Coursera",
                "cost": 49.99,
                "duration_weeks": 4
            })
    return courses

def crawl_all():
    # Combine multiple sources here in the future
    courses = crawl_coursera()
    # Future sources: edX, Saylor, Study.com, ACE, CLEP
    return courses

if __name__ == "__main__":
    import json
    all_courses = crawl_all()
    with open("courses.json", "w") as f:
        json.dump(all_courses, f, indent=4)
