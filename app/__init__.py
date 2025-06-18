import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

# Import page data
from app.data.work_experiences import work_experiences
from app.data.education import educations
from app.data.hobbies import hobbies

load_dotenv()
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",
                           title="Smriti Rangaragajan",
                           url=os.getenv("URL"))

# ---------- Work ----------
@app.route("/work")
def work_page():
    return render_template("work.html",
                           title="Work Experience",
                           work_experiences=work_experiences)

# ---------- Education ----------
@app.route("/education")
def education_page():
    return render_template("education.html",
                           title="Education",
                           educations=educations)

# ---------- Hobbies ----------
@app.route("/hobbies")
def hobbies_page():
    return render_template("hobbies.html",
                           title="Hobbies",
                           hobbies=hobbies)

# ---------- Map ----------
@app.route("/map")
def map_page():
    return render_template("map.html",
                           title="Countries I've Visited")
