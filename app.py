from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

@app.route("/")

def home():
    now = datetime.now()
    current_year = now.year
    current_month = now.strftime("%B") # "September"
    return render_template("index.html", year=current_year, month=current_month)

# New route for the solar system page
@app.route("/solar-system")
def solar_system():
    planet_count = 8
    return render_template("solar_system.html", planet_count=planet_count)