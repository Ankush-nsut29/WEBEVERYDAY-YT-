from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/" ,methods=["POST","GET"])
def home():
    if request.method=="POST":
        user=request.form["nm"]
        return  f"<h1 style= ' background-color: #181818; color: white ; font-family: sans-serif;text-align: center;' >HAPPY BIRTHDAY {user}!! </h1>" 
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)