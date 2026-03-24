from flask import Flask, render_template, request, jsonify
from crawler import crawl_all
from degree_parser import load_degree, normalize_degree
from mapper import map_courses_to_degree
from optimizer import optimize_path

app = Flask(__name__)

@app.route("/")
def index():
    # Renders the front-end form
    return render_template("index.html")

@app.route("/optimize", methods=["POST"])
def optimize():
    try:
        target_degree = request.form.get("degree", "").strip()
        if not target_degree:
            return jsonify({"error": "No degree entered"}), 400

        # 1️⃣ Load and normalize degree requirements
        degree = normalize_degree(load_degree())

        # 2️⃣ Crawl all available courses
        courses = crawl_all()

        # 3️⃣ Map courses to degree requirements
        mapped = map_courses_to_degree(courses, degree)

        # 4️⃣ Run optimizer for best path
        optimized = optimize_path(mapped)

        return jsonify(optimized)

    except Exception as e:
        # Return error in JSON if pipeline fails
        return jsonify({"error": f"Pipeline failed: {str(e)}"}), 500

if __name__ == "__main__":
    # Run on all interfaces to allow Codespaces port forwarding
    app.run(host="0.0.0.0", port=5000, debug=True)
