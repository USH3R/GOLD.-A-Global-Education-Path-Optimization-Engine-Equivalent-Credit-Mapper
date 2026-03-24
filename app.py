from flask import Flask, render_template, request, jsonify

from crawler import crawl_all
from degreeparser import load_degree, normalize_degree
from mapper import map_courses_to_degree
from optimizer import optimize_path

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/optimize", methods=["POST"])
def optimize():
    target_degree = request.form.get("degree")

    try:
        # STEP 1: degree
        degree = normalize_degree(load_degree(target_degree))
        print("DEGREE:", degree)

        # STEP 2: courses
        courses = crawl_all()
        print("COURSES:", courses)

        # STEP 3: mapping
        mapped = map_courses_to_degree(courses, degree)
        print("MAPPED:", mapped)

        # STEP 4: optimization
        optimized = optimize_path(mapped)
        print("OPTIMIZED:", optimized)

        return jsonify(optimized)

    except Exception as e:
        print("🔥 FULL ERROR:", str(e))

        # RETURN REAL ERROR TO BROWSER
        return jsonify({
            "degree": target_degree,
            "error": str(e),
            "courses_needed": [],
            "total_cost": 0,
            "total_duration_weeks": 0,
            "transferable_credits": 0
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
