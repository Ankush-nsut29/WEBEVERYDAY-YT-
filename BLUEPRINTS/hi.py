from flask import Flask,Blueprint,render_template,redirect,url_for,session

hi=Blueprint("hi",__name__)

@hi.route("/")
def hi_view():
    return render_template("hi.html", name=session.get("name", "Guest"))