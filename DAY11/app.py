from flask import Flask,redirect,url_for,render_template,session,request

app=Flask(__name__)
app.secret_key="ansni"

@app.route("/",methods=["POST","GET"])
def home():
    if request.method=="POST":
        problem=request.form["problem"]
        problem=problem.lower()
        l=problem.split()
        s="-".join(l)
        session["prob"]=s
        return redirect(url_for("result"))
    else:
        return render_template("index.html")

@app.route("/result")
def result():
    if "prob" not in session:
        return redirect(url_for("home"))
    else:
        p=session["prob"]
        return render_template("result.html", p=p)

if __name__=="__main__":
    app.run(debug=True)             
