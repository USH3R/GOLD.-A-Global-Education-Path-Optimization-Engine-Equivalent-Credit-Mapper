from flask import Flask, request, render_template_string
from mapper import map_courses_to_degree
from degree_parser import load_degree

app = Flask(__name__)

# Corrected to Master's Only
DEGREE_OPTIONS = [
    "Master of Computer Science",
    "Master of Business Administration",
    "Master of Psychology"
]

HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Gold: Graduate Path Optimizer</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 40px; color: #333; line-height: 1.6; background-color: #f4f7f6; }
        .container { max-width: 800px; margin: auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; border-bottom: 3px solid #d4af37; padding-bottom: 10px; }
        form { margin-bottom: 30px; padding: 20px; background: #ecf0f1; border-radius: 8px; }
        .result-box { border-left: 5px solid #d4af37; padding: 20px; background: #fff; }
        .result-line { margin-bottom: 12px; border-bottom: 1px solid #eee; padding-bottom: 5px; }
        .label { font-weight: bold; color: #2c3e50; width: 180px; display: inline-block; }
        .error { color: #e74c3c; background: #fdf2f2; padding: 10px; border-radius: 5px; border: 1px solid #e74c3c; }
        input[type="text"] { width: 100%; padding: 10px; margin: 10px 0 20px 0; border-radius: 5px; border: 1px solid #ccc; box-sizing: border-box; }
        input[type="submit"] { background: #2c3e50; color: white; border: none; padding: 12px 25px; border-radius: 5px; cursor: pointer; font-size: 16px; width: 100%; }
        input[type="submit"]:hover { background: #1a252f; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Gold: Graduate Path Optimizer</h1>
        
        <form method="POST">
          <label style="font-weight:bold; display:block; margin-bottom:10px;">Select Your Target Master's Degree:</label>
          <select name="degree" style="padding:10px; width: 100%; margin-bottom: 20px; border-radius: 5px; border: 1px solid #ccc;">
            {% for deg in degrees %}
              <option value="{{ deg }}">{{ deg }}</option>
            {% endfor %}
          </select>

          <label style="font-weight:bold; display:block; margin-bottom:10px;">Graduate Courses Completed (comma-separated):</label>
          <input type="text" name="completed_courses" placeholder="e.g., Advanced Algorithms, Psychopathology">

          <input type="submit" value="Optimize Master's Path">
        </form>

        {% if result %}
            <div class="result-box">
                <h2 style="margin-top:0; color: #2c3e50;">Optimization Result</h2>
                
                {% if result.error %}
                    <p class="error"><strong>Oops!</strong> {{ result.error }}</p>
                {% else %}
                    <div class="result-line">
                        <span class="label">Degree:</span> {{ result.degree }}
                    </div>
                    
                    <div class="result-line">
                        <span class="label">Courses Needed:</span> 
                        <span style="color: #555;">{{ result.courses_needed | join(', ') if result.courses_needed else 'All Requirements Met!' }}</span>
                    </div>
                    
                    <div class="result-line">
                        <span class="label">Total Credits:</span> {{ result
