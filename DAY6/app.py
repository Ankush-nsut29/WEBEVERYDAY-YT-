from flask import Flask,render_template,request

app= Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    if request.method=="POST":
        x=request.form["x"]
        op=request.form["opr"]
        y=request.form["y"]
        if op=="+":
            z=int(x)+int(y)
        elif op=="-":
            z=int(x)-int(y)
        elif op=="*":
            z=int(x)*int(y)
        elif op=="/":
            if int(y)==0:
                z="cant divide by 0"
            else:    
                z=int(x)/int(y)
        else:
            z="invalid syntax"    
        return f"<h1 style= ' background-color: #181818; color: white ; font-family: sans-serif;text-align: center;'>{z}</h1>"
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)