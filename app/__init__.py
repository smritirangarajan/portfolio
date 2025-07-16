import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import * 
import datetime
from playhouse.shortcuts import model_to_dict



# Import page data
from app.data.work_experiences import work_experiences
from app.data.education import educations
from app.data.hobbies import hobbies

import pymysql
pymysql.install_as_MySQLdb()

load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING") == "true":
    print("Running in test mode...")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(os.getenv('MYSQL_DATABASE'),
                         user=os.getenv('MYSQL_USER'),
                         password=os.getenv('MYSQL_PASSWORD'),
                         host=os.getenv('MYSQL_HOST'),
                         port=3306)

print(mydb)

@app.route("/")
def index():
    return render_template("index.html",
                           title="Smriti Rangaragajan",
                           url=os.getenv("URL"))

class TimelinePost(Model):
    name=CharField()
    email=CharField()
    content=TextField()
    created_at=DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

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

@app.route('/test-post', methods=['POST'])
def test_post():
    print("🔥 TEST POST received")
    return {"status": "ok"}

# ---------- Timeline Post ----------
@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    print("✅ Flask received a POST request!")  # 👈 Add this
    name=request.form['name']
    email=request.form['email']
    content=request.form['content']
    timeline_post=TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts':[
            model_to_dict(p) for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/api/timeline_post/<int:id>', methods=['DELETE'])
def delete_timeline_post(id):
    try:
        post = TimelinePost.get_by_id(id)
        post.delete_instance()
        return {"deleted": id}
    except TimelinePost.DoesNotExist:
        return {"error": f"Post with ID {id} does not exist"}, 404
    
@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title='Timeline')

