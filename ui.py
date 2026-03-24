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
    target_degree = request.form.get("degree")
    degree = normalize_degree(load_degree())
    courses = crawl_all()
    mapped = map_courses_to_degree(courses, degree)
    optimized = optimize_path(mapped)
    return jsonify(optimized)

if __name__ == "__main__":
    app.run(debug=True)
