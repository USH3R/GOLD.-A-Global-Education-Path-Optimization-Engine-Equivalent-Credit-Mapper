# app.py
from flask import Flask, render_template, request, jsonify
from crawler import crawl_all
from degree_parser import load_degree, normalize_degree
from mapper import map_courses_to_degree
from optimizer import optimize_path

app = Flask(__name__)

# Home page
@app.route("/")
def index():
    return render_template("index.html")

# Optimize endpoint
@app.route("/optimize", methods=["POST"])
def optimize():
    try:
        # Get target degree from form submission
        target_degree = request.form.get("degree", "").strip()
        if not target_degree:
            return jsonify({"error": "No degree provided"}), 400

        # Load and normalize degree requirements
        degree_data = load_degree()                # Load from your degree data source
        normalized_degree = normalize_degree(degree_data, target_degree)  # Normalize based on user input

        # Crawl courses from MOOCs / ACE / CLEP / Saylor / Study.com
        courses = crawl_all()  # Returns list of course dicts with metadata

        # Map courses to degree requirements
        mapped_courses = map_courses_to_degree(courses, normalized_degree)

        # Optimize path for max transfer, min cost/time
        optimized_result = optimize_path(mapped_courses)

        # Return JSON to front-end
        return jsonify(optimized_result)

    except Exception as e:
        # Catch any unexpected errors and return as JSON
        return jsonify({"error": "Unexpected error occurred", "details": str(e)}), 500


if __name__ == "__main__":
    # Run Flask on all interfaces so Codespaces can expose port
    app.run(host="0.0.0.0", port=5000, debug=True)
