# app.py
from flask import Flask, render_template, request, jsonify
from crawler import crawl_all
from degree_parser import load_degree, normalize_degree
from mapper import map_courses_to_degree
from optimizer import optimize_path

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/optimize", methods=["POST"])
def optimize():
    try:
        # Get target degree from form
        target_degree = request.form.get("degree", "").strip()
        if not target_degree:
            return jsonify({"error": "No degree provided"}), 400

        # Load and normalize degree requirements
        degree_data = normalize_degree(load_degree(target_degree))

        # Crawl courses from MOOCs, ACE, CLEP, etc.
        courses = crawl_all(subject=target_degree)

        # Map courses to degree requirements
        mapped_courses = map_courses_to_degree(courses, degree_data)

        # Run optimization engine
        optimized_result = optimize_path(mapped_courses)

        return jsonify(optimized_result)

    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

if __name__ == "__main__":
    # Flask dev server
    app.run(host="0.0.0.0", port=5000, debug=True)
