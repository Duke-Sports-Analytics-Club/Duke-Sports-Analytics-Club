from flask import render_template, request, url_for
from app import app
import string
import random

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route('/about', methods=['GET', 'POST'])
def about():
    random.seed(7)
    p = "".join(random.choices(string.ascii_lowercase, k=500))
    return render_template("about.html", paragraph=p)

@app.route('/profiles', methods=['GET', 'POST'])
def profiles():
    return render_template("profiles.html")

@app.route('/projects', methods=['GET', 'POST'])
def projects():
    if request.endpoint == url_for("ex1"):
        return redirect(url_for("ex1"))
    return render_template("projects.html")

@app.route('/ex1', methods=['GET', 'POST'])
def ex1():
    return render_template("ex1.html")

@app.route('/ex2', methods=['GET', 'POST'])
def ex2():
    return render_template("ex2.html")

@app.route('/ex3', methods=['GET', 'POST'])
def ex3():
    return render_template("ex3.html")