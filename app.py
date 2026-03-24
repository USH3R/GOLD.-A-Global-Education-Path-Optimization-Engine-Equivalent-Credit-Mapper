# app.py
from flask import Flask, render_template, request, jsonify
from crawler import crawl_all
from degree_parser import load_degree, normalize_degree
from mapper import map_courses_to_degree
from optimizer import optimize_path

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def index():
    """
    Render the main page with the degree input form.
    """
    return render_template("index.html")

@app.route("/optimize", methods=["POST"])
def optimize():
    """
    Endpoint to receive the target degree, run crawler, map courses, and return
    an optimized path.
    """
    target_degree = request.form.get("degree", "").strip()
    if not target_degree:
        return jsonify({"error": "No degree provided"}), 400

    # Load and normalize degree requirements
    degree = normalize_degree(load_degree(target_degree))

    # Crawl all courses from sources
    courses = crawl_all()

    # Map courses to degree requirements
    mapped = map_courses_to_degree(courses, degree)

    # Run optimizer
    optimized = optimize_path(mapped)

    return jsonify(optimized)

if __name__ == "__main__":
    # Run Flask app accessible from Codespaces
    app.run(host="0.0.0.0", port=5000, debug=True)
