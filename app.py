from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/optimize", methods=["POST"])
def optimize():
    target_degree = request.form.get("degree")
    
    # --- Stub response for immediate testing ---
    sample_response = {
        "degree": target_degree,
        "total_cost": 0,
        "total_duration_weeks": 0,
        "courses_needed": ["Sample Course 1", "Sample Course 2"],
        "transferable_credits": 0
    }
    return jsonify(sample_response)

if __name__ == "__main__":
    # Open on all interfaces for Codespaces; debug off for now
    app.run(host="0.0.0.0", port=5000)
