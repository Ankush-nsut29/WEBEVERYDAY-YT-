from flask import Flask,render_template,redirect,url_for,session,request

app=Flask(__name__)
app.secret_key="kebd hd"

@app.route("/",methods=["POST","GET"])
def q1():
    if request.method=="POST":
        x=request.form["ans"]
        session["score"]=0
        if x=="i":
            session["score"]=0
        elif x=="c":
            session["score"]=-10
        else:
            session["score"]=-30
        return redirect(url_for("q2"))    
    else:
        return render_template("q1.html")          

@app.route("/q2",methods=["POST","GET"])
def q2():
    if "score" not in session:
        return redirect(url_for("q1"))
    else:
        if request.method=="POST":
            x=request.form["ans"]
            if x=="sweet":
                session["score"]-=30
            elif x=="sour":
                session["score"]-=10
            else:
                session["score"]-=0    
            return redirect(url_for("q3"))      
        else:
            return render_template("q2.html")

@app.route("/q3",methods=["POST","GET"])
def q3():
    if "score" not in session:
        return redirect(url_for("q1"))
    else:
        if request.method=="POST":
            x=request.form["ans"]
            if x=="chai":
                session["score"]-=30
            if x=="coffee":
                session["score"]-=30
            elif x=="juice":
                session["score"]-=10
            else:
                session["score"]-=0    
            return redirect(url_for("result"))      
        else:
            return render_template("q3.html")
        
@app.route("/result")
def result():
    if "score" not in session:
        return redirect(url_for("q1"))   
    else:
        x= 100 + session["score"]
        return f"<h1>your score is {x}/100</h1>"
    
@app.route("/logout")
def logout():
    session.pop("score")
    return redirect(url_for("q1"))

    
if __name__=="__main__":
    app.run(debug=True)    
