import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Smriti Rangaragajan", url=os.getenv("URL"))

@app.route('/work')
def work_page():
    return render_template('work.html', title="Work Experience")

@app.route('/education')
def education_page():
    return render_template('education.html', title="Education")

@app.route('/hobbies')
def hobbies_page():
    return render_template('hobbies.html', title="Hobbies")

@app.route('/map')
def map_page():
    return render_template('map.html', title="Countries I've Visited")