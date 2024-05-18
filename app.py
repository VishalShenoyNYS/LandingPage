from flask import Flask,request, render_template
from flask import url_for

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html",title="New You Solutions",page_hero_title="",page_hero_video="static/videos/nys-home-video.mp4")
    

@app.route('/about',methods=["GET"])
def about():
    if request.method == "GET":
        return render_template("about.html",title="New You Solutions | About",page_hero_title="",page_hero_video="static/videos/nys-home-video.mp4")  

@app.route('/services',methods=["GET"])
def services():
    if request.method == "GET":
        return render_template("services.html",title="New You Solutions | Services",page_hero_title="",page_hero_video="static/videos/nys-home-video.mp4")  

@app.route('/courses',methods=["GET"])
def courses():
    if request.method == "GET":
        return render_template("courses.html",title="New You Solutions | Courses",page_hero_title="",page_hero_video="static/videos/nys-home-video.mp4")  
if __name__ == "__main__":
    app.run(debug=True)