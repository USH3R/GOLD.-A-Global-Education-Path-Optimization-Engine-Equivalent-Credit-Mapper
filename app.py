from flask import Flask, request, render_template_string
from mapper import map_courses_to_degree

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
        try:
            # Simulate student with no courses taken yet
            courses_taken = []
            result = map_courses_to_degree(courses_taken, degree_name)
        except Exception as e:
            # Return safe error info if anything fails
            result = {
                "degree": degree_name,
                "courses_needed": [],
                "transferable_credits": 0,
                "error": str(e)
            }
    return render_template_string(HTML_TEMPLATE, degrees=DEGREE_OPTIONS, result=result)

if __name__ == "__main__":
    # Run on all interfaces for Codespaces; debug=True shows errors in-browser
    app.run(host="0.0.0.0", port=5000, debug=True)from flask import Flask, request, jsonify, render_template_string
from mapper import map_courses_to_degree

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
        try:
            # For now, we simulate user has taken no courses
            courses_taken = []
            result = map_courses_to_degree(courses_taken, degree_name)
        except Exception as e:
            result = {
                "degree": degree_name,
                "courses_needed": [],
                "transferable_credits": 0,
                "error": str(e)
            }
    return render_template_string(HTML_TEMPLATE, degrees=DEGREE_OPTIONS, result=result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
