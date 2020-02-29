from app import app
from app.forms import LoginForm
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Frank"}
    posts = [
        {
            "author": {"username": "Frank"},
            "body": "Beautiful day in Rastatt",
        },
        {
            "author": {"username": "Silke"},
            "body": "Ich han schon wieder in die Bux geschiss",
        },
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Sign In", form=form)
