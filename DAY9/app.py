from flask import Flask,redirect,url_for,render_template,session,request

app=Flask(__name__)
app.secret_key="abcdefg"

@app.route("/",methods=["POST","GET"])
def login():
    if request.method=="POST":
        session.permanent=True
        user=request.form["nm"]
        session["user"]=user
        return redirect(url_for("user"))
    else:
        return render_template("index.html")
    
@app.route("/user")
def user():
    if "user" not in session:
        return redirect(url_for("login"))
    else:
        current_user = session["user"]
        if "no" not in session:
            session["no"] = 0

        session["no"] += 1 
        return f"<h1>hi {current_user} you have visited {session['no']} times</h1>"
        

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__=="__main__":
    app.run(debug=True)    