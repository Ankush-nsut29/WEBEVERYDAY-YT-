from flask import Flask,Blueprint,render_template,redirect,url_for,session

by=Blueprint("by",__name__)

@by.route("/")
def by_view():
    return render_template("by.html", name=session.get("name", "Guest"))