from flask import Flask,render_template,redirect,url_for,request

app=Flask(__name__)

d1={"10":10,"20":40,"30":50,"40":200,"50":200,"60":200,"more":1000}

d2={"10":5,"20":20,"30":30,"40":40,"50":50,"60":60,"more":70}

d3={"10":0,"20":5,"30":10,"40":15,"50":20,"60":20,"more":25}

@app.route("/",methods=["POST","GET"])
def home():
    if request.method=="POST":
        diff=request.form["diff"]
        time=request.form["time"]
        hints=request.form["hint"]
        total=0
        if diff=="e":
            total+=d1[time]
            total+=50*int(hints)
        elif diff=="m":
            total+=d2[time]
            total+=20*int(hints)
        else:
            total+=d3[time]
            total+=5*int(hints)
        s=""
        if total==0:
            s="YOU ARE A LEETCODE GOD"
        elif total<=10:
            s="YOU ARE A GIGA CHAD"
        elif total<=50:
            s="YOU ARE A LEETCODE PRO"
        elif total<=100:
            s="YOU ARE AVERAGE"
        elif total<=300:
            s="YOU ARE COOKED LOL"
        else:
            s="JUST LEAVE LEECODE YOU IDIOT"

        return redirect(url_for("result",s=s))
    
    else:
        return render_template("index.html")   
    
@app.route("/result/<s>")
def result(s):
    return render_template("result.html",s=s)


if __name__ == "__main__":
    app.run(debug=True)                 



