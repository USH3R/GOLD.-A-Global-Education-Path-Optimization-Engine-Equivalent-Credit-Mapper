from flask import Flask, request, render_template_string
from mapper import map_courses_to_degree
from degree_parser import load_degree

app = Flask(__name__)

# These are the "Friendly Names" shown to the user
DEGREE_OPTIONS = [
    "Bachelor of Computer Science",
    "Bachelor of Business Administration",
    "Bachelor of Psychology"
]

HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Gold: Education Path Optimizer</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 40px; color: #333; line-height: 1.6; background-color: #f4f7f6; }
        .container { max-width: 800px; margin: auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }
        form { margin-bottom: 30px; padding: 20px; background: #ecf0f1; border-radius: 8px; }
        .result-box { border-left: 5px solid #3498db; padding: 20px; background: #fff; }
        .result-line { margin-bottom: 12px; border-bottom: 1px solid #eee; padding-bottom: 5px; }
        .label { font-weight: bold; color: #2c3e50; width: 180px; display: inline-block; }
        .error { color: #e74c3c; background: #fdf2f2; padding: 10px; border-radius: 5px; border: 1px solid #e74c3c; }
        input[type="submit"] { background: #3498db; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-size: 16px; }
        input[type="submit"]:hover { background: #2980b9; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Gold: Education Path Optimizer</h1>
        
        <form method="POST">
          <label for="degree" style="font-weight:bold; display:block; margin-bottom:10px;">Select Your Target Degree:</label>
          <select name="degree" style="padding:10px; width: 100%; margin-bottom: 20px; border-radius: 5px; border: 1px solid #ccc;">
            {% for deg in degrees %}
              <option value="{{ deg }}">{{ deg }}</option>
            {% endfor %}
          </select>
          <input type="submit" value="Run Optimization">
        </form>

        {% if result %}
            <div class="result-box">
                <h2 style="margin-top:0; color: #2980b9;">Optimization Result</h2>
                
                {% if result.error %}
                    <p class="error"><strong>Oops!</strong> {{ result.error }}</p>
                    <p style="font-size: 0.9em; color: #666;">Tip: Ensure your degrees.json contains a key that matches your selection.</p>
                {% else %}
                    <div class="result-line">
                        <span class="label">Degree:</span> {{ result.degree }}
                    </div>
                    
                    <div class="result-line">
                        <span class="label">Courses Needed:</span> 
                        <span style="color: #555;">{{ result.courses_needed | join(', ') if result.courses_needed else 'None' }}</span>
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
        
        # 1. Normalize the name (e.g., "Bachelor of Psychology" -> "psychology")
        # This makes it easier to match whatever is in your JSON.
        search_name = display_name.lower().replace("bachelor of ", "").replace(" ", "_").strip()
        
        # 2. Try loading the data
        degree_data = load_degree(search_name)

        # 3. If that fails, try loading with the full name just in case
        if not degree_data or "error" in degree_data:
            degree_data = load_degree(display_name)

        if not degree_data or "error" in degree_data:
            result = {
                "degree": display_name,
                "error": f"Degree '{display_name}' (tried '{search_name}') not found in database."
            }
        else:
            try:
                # Still assuming 0 courses taken for now
                courses_taken = []
                result = map_courses_to_degree(courses_taken, degree_data)
                # Ensure the display name looks nice in the result
                result["degree"] = display_name 
            except Exception as e:
                result = {"degree": display_name, "error": f"Mapping Error: {str(e)}"}

    return render_template_string(HTML_TEMPLATE, degrees=DEGREE_OPTIONS, result=result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)from flask import Flask, request, render_template_string
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
