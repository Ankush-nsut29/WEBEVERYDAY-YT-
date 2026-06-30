from flask import Flask,redirect,url_for,render_template,request,Blueprint,session

home=Blueprint("home",__name__)

@home.route("/",methods=["GET","POST"])
def home_view():
    if request.method=="POST":
        name=request.form["nm"]
        session["name"]=name
        return redirect(url_for("hi.hi_view"))
    else:
        return render_template("home.html")
