from flask import Flask,session,render_template,redirect,url_for,request

app=Flask(__name__)
app.secret_key="vfytdcgvnb "

@app.route("/",methods=["POST","GET"])
def name():
    if request.method=="POST":
        nm=request.form["nm"]
        if "name" not in session:
            session["name"]=nm
        return redirect(url_for("sem1"))   
    else:
        return render_template("name.html")

@app.route("/sem1",methods=["POST","GET"])
def sem1():
    if request.method=="POST":
        cg1=request.form["cg1"]
        if "sem1" not in session:
            session["sem1"]=cg1
        return redirect(url_for("sem2"))   
    else:
        return render_template("sem1.html")   

@app.route("/sem2",methods=["POST","GET"])
def sem2():
    if request.method=="POST":
        cg2=request.form["cg2"]
        if "sem2" not in session:
            session["sem2"]=cg2
        return redirect(url_for("result"))   
    else:
        return render_template("sem2.html")

@app.route("/result")
def result():
    name=session["name"]
    CGPA=(20*float(session["sem1"])+24*(float(session["sem2"])))/44
    return render_template("result.html",name=name,CGPA=CGPA)

@app.route("/logout")
def logout():
    session.pop("name",None)
    session.pop("sem1",None)
    session.pop("sem2",None)
    return redirect(url_for("name"))

if __name__=="__main__":
    app.run(debug=True)