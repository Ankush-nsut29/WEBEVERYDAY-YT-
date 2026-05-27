from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route("/", methods=["POST","GET"])
def home():
    if request.method=="POST":
        n=request.form["nm"]
        c=len(n)
        w=len(n.split())
        m=w/200
        return redirect(url_for("result",w=w,c=c,m=m))
    else:
        return render_template("index.html")
    
@app.route("/result/<w>/<c>/<m>")
def result(w,c,m):
    return render_template("result.html",w=w,c=c,m=m)    

if __name__=="__main__":
    app.run(debug=True)