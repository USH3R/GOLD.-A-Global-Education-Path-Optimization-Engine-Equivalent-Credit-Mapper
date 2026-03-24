from flask import Flask, request, render_template_string
from mapper import map_courses_to_degree
from degree_parser import load_degree

app = Flask(__name__)

# What the user sees in the dropdown
DEGREE_OPTIONS = [
    "Master of Computer Science",
    "Master of Business Administration",
    "Master of Psychology"
]

# Map UI names → JSON keys
DEGREE_KEY_MAP = {
    "Master of Computer Science": "master_of_computer_science",
    "Master of Business Administration": "master_of_business_administration",
    "Master of Psychology": "master_of_psychology"
}

HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Gold: Education Path Optimizer</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 40px; color: #333; background-color: #f4f7f6; }
        .container { max-width: 800px; margin: auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }
        form { margin-bottom: 30px; padding: 20px; background: #ecf0f1; border-radius: 8px; }
        .result-box { border-left: 5px solid #3498db; padding: 20px; background: #fff; }
        .result-line { margin-bottom: 12px; }
        .label { font-weight: bold; display: inline-block; width: 200px; }
        .error { color: #e74c3c; background: #fdf2f2; padding: 10px; border-radius: 5px; border: 1px solid #e74c3c; }
        input[type="submit"] { background: #3498db; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; }
        input[type="submit"]:hover { background: #2980b9; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Gold: Education Path Optimizer</h1>
        
        <form method="POST">
          <label style="font-weight:bold;">Select Your Target Degree:</label><br><br>
          <select name="degree" style="padding:10px; width:100%; margin-bottom:20px;">
            {% for deg in degrees %}
              <option value="{{ deg }}">{{ deg }}</option>
            {% endfor %}
          </select>
          <input type="submit" value="Run Optimization">
        </form>

        {% if result %}
            <div class="result-box">
                <h2>Optimization Result</h2>

                {% if result.error %}
                    <p class="error"><strong>Error:</strong> {{ result.error }}</p>
                {% else %}
                    <div class="result-line">
                        <span class="label">Degree:</span> {{ result.degree }}
                    </div>

                    <div class="result-line">
                        <span class="label">Courses Needed:</span>
                        {{ result.courses_needed | join(', ') if result.courses_needed else 'None' }}
                    </div>

                    <div class="result-line">
                        <span class="label">Total Credits:</span> {{ result.total_credits }}
                    </div>

                    <div class="result-line">
                        <span class="label">Transferable Credits:</span> {{ result.transferable_credits }}
                    </div>
                {% endif %}
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        display_name = request.form.get("degree")

        try:
            # Convert UI name → JSON key
            degree_key = DEGREE_KEY_MAP.get(display_name)

            if not degree_key:
                raise Exception("Invalid degree selection")

            # Load degree data
            degree_data = load_degree(degree_key)

            if not degree_data or "error" in degree_data:
                raise Exception(f"Degree '{display_name}' not found in database")

            # Simulate no prior courses
            courses_taken = []

            # Run mapping
            result = map_courses_to_degree(courses_taken, degree_data)

            # Ensure UI displays clean name
            result["degree"] = display_name

        except Exception as e:
            result = {
                "degree": display_name,
                "courses_needed": [],
                "total_credits": 0,
                "transferable_credits": 0,
                "error": str(e)
            }

    return render_template_string(HTML_TEMPLATE, degrees=DEGREE_OPTIONS, result=result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
