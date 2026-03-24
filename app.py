from flask import Flask, render_template, request, jsonify
from crawler import crawl_all
from degree_parser import load_degree, normalize_degree
from mapper import map_courses_to_degree
from optimizer import optimize_path
import traceback

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/optimize", methods=["POST"])
def optimize():
    target_degree = request.form.get("degree", "").strip()
    
    try:
        # Load and normalize degree
        degree = normalize_degree(load_degree())
        
        # Crawl courses from sources
        courses = crawl_all()
        
        # Map courses to degree requirements
        mapped_courses = map_courses_to_degree(courses, degree)
        
        # Optimize the course path
        optimized_result = optimize_path(mapped_courses)
        
        # Return the optimized JSON
        return jsonify(optimized_result)
    
    except Exception as e:
        # Print full traceback to Codespaces terminal
        print("=== ERROR IN /optimize ===")
        print(traceback.format_exc())
        print("==========================")
        
        # Return a safe fallback JSON to the browser
        fallback_response = {
            "degree": target_degree if target_degree else "Unknown Degree",
            "total_cost": 0,
            "total_duration_weeks": 0,
            "courses_needed": ["Sample Course 1", "Sample Course 2"],
            "transferable_credits": 0,
            "error": "An unexpected error occurred. Check server logs."
        }
        return jsonify(fallback_response)

if __name__ == "__main__":
    # Debug mode on and host set for Codespaces
    app.run(debug=True, host="0.0.0.0", port=5000)
