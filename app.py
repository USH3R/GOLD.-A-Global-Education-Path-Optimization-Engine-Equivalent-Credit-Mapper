from flask import Flask, request, jsonify, render_template_string
from mapper import map_courses_to_degree
from degree_parser import load_degree

app = Flask(__name__)

DEGREE_OPTIONS = [
    "Bachelor of Computer Science",
    "Bachelor of Business Administration",
    "Bachelor of Psychology"
]

HTML_TEMPLATE = """
<!doctype html>
<title>Gold: Education Path Optimizer</title>
<h1>Gold: Education Path Optimizer</h1>
<form method="POST">
  <label for="degree">Choose your target degree:</label>
  <select name="degree">
    {% for deg in degrees %}
      <option value="{{ deg }}">{{ deg }}</option>
    {% endfor %}
  </select>
  <input type="submit" value="Optimize">
</form>

{% if result %}
<h2>Optimization Result:</h2>
<pre>{{ result }}</pre>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        degree_name = request.form.get("degree")
        degree_data = load_degree(degree_name)

        if degree_data is None or "error" in degree_data:
            # Handle missing or invalid degree
            result = {
                "degree": degree_name,
                "courses_needed": [],
                "total_credits": 0,
                "transferable_credits": 0,
                "error": degree_data.get("error", "Invalid degree data")
            }
        else:
            try:
                # Simulate no courses taken yet
                courses_taken = []
                result = map_courses_to_degree(courses_taken, degree_data)
            except Exception as e:
                result = {
                    "degree": degree_name,
                    "courses_needed": [],
                    "total_credits": 0,
                    "transferable_credits": 0,
                    "error": str(e)
                }

    return render_template_string(HTML_TEMPLATE, degrees=DEGREE_OPTIONS, result=result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)from flask import Flask, request, jsonify, render_template_string
from mapper import map_courses_to_degree
from degree_parser import load_degree  # Import our fixed parser

app = Flask(__name__)

DEGREE_OPTIONS = [
    "Bachelor of Computer Science",
    "Bachelor of Business Administration",
    "Bachelor of Psychology"
]

HTML_TEMPLATE = """
<!doctype html>
<title>Gold: Education Path Optimizer</title>
<h1>Gold: Education Path Optimizer</h1>
<form method="POST">
  <label for="degree">Choose your target degree:</label>
  <select name="degree">
    {% for deg in degrees %}
      <option value="{{ deg }}">{{ deg }}</option>
    {% endfor %}
  </select>
  <input type="submit" value="Optimize">
</form>

{% if result %}
<h2>Optimization Result:</h2>
<pre>{{ result }}</pre>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        degree_name = request.form.get("degree")
        degree_data = load_degree(degree_name)  # <-- This is critical
        try:
            # courses_taken is empty for now
            courses_taken = []
            result = map_courses_to_degree(courses_taken, degree_data)
        except Exception as e:
            result = {
                "degree": degree_name,
                "courses_needed": [],
                "total_credits": 0,
                "transferable_credits": 0,
                "error": str(e)
            }
    return render_template_string(HTML_TEMPLATE, degrees=DEGREE_OPTIONS, result=result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
