from flask import Flask,request, render_template
from flask import url_for

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html",title="New You Solutions",page_hero_title="New You Solutions",page_hero_video="static/videos/nys-home-video.mp4")
    

@app.route('/about',methods=["GET"])
def about():
    if request.method == "GET":
        return render_template("about.html",title="New You Solutions | About",page_hero_title="",page_hero_video="static/videos/nys-home-video.mp4")  

@app.route('/services',methods=["GET"])
def services():
    if request.method == "GET":
        return render_template("services.html",title="New You Solutions | Services")  

@app.route('/courses',methods=["GET"])
def courses():
    if request.method == "GET":
        return render_template("courses.html",title="New You Solutions | Courses")  

@app.route("/connect",methods=["GET","POST"])
def connect_page():
    if request.method == "GET":
        return render_template("connect.html",title="New You Solutions | Connect")
    
@app.route("/study-abroad",methods=["GET","POST"])
def study_abroad_page():
    if request.method == "GET":
        return render_template("study_abroad.html",title="New You Solutions | Study Abroad")
            

if __name__ == "__main__":
    app.run(debug=True)