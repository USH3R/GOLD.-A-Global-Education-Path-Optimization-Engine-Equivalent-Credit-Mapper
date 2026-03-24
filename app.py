from flask import Flask, request, jsonify, render_template_string
from degree_parser import load_degree, normalize_degree
from mapper import map_courses_to_degree

app = Flask(__name__)

# Only three available degrees
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
        degree_normalized = normalize_degree(degree_name)
        result = map_courses_to_degree(degree_normalized)
    return render_template_string(HTML_TEMPLATE, degrees=DEGREE_OPTIONS, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
