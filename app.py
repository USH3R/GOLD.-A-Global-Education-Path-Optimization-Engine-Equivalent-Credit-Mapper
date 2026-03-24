from flask import Flask, request, render_template_string
from mapper import map_courses_to_degree
from degree_parser import load_degree

app = Flask(__name__)

# Options shown in the HTML dropdown
DEGREE_OPTIONS = [
    "Bachelor of Computer Science",
    "Bachelor of Business Administration",
    "Bachelor of Psychology"
]

# The professional, formatted HTML
HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Gold: Education Path Optimizer</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 40px; color: #333; line-height: 1.6; }
        h1 { color: #2c3e50; border-bottom: 2px solid #eee; padding-bottom: 10px; }
        form { background: #f9f9f9; padding: 20px; border-radius: 8px; margin-bottom: 30px; }
        .result-box { background: #fff; border: 1px solid #ddd; padding: 25px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .result-line { margin-bottom: 15px; font-size: 1.1em; }
        .label { font-weight: bold; color: #2c3e50; min-width: 180px; display: inline-block; }
        .error { color: #c0392b; font-weight: bold; }
    </style>
</head>
<body>
    <h1>Gold: Education Path Optimizer</h1>
    
    <form method="POST">
      <label for="degree" style="font-weight:bold;">Choose your target degree:</label><br><br>
      <select name="degree" style="padding:8px; width: 300px;">
        {% for deg in degrees %}
          <option value="{{ deg }}">{{ deg }}</option>
        {% endfor %}
      </select>
      <input type="submit" value="Optimize" style="padding:8px 20px; cursor:pointer; background:#2c3e50; color:white; border:none; border-radius:4px;">
    </form>

    {% if result %}
    <div class="result-box">
        <h2 style="margin-top:0;">Optimization Result:</h2>
        
        {% if result.error %}
            <p class="error">Error: {{ result.error }}</p>
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
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        degree_name = request.form.get("degree")
        
        # Load degree data using the parser
        degree_data = load_degree(degree_name)

        if not degree_data or "error" in degree_data:
            result = {
                "degree": degree_name,
                "error": degree_data.get("error") if degree_data else "Invalid degree data"
            }
        else:
            try:
                # Currently simulating 0 courses taken
                courses_taken = []
                result = map_courses_to_degree(courses_taken, degree_data)
            except Exception as e:
                result = {"degree": degree_name, "error": str(e)}

    return render_template_string(HTML_TEMPLATE, degrees=DEGREE_OPTIONS, result=result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
