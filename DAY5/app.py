from flask import Flask, render_template,request

app=Flask(__name__)

d={"police": "100", "fire":"101" , "ambulance":"102" , "general":"112", "women": "14490" , "dog" : "me"}

@app.route("/" , methods=["GET","POST"])
def home():
    if request.method=="POST":
        key=request.form["nm"]
        if key in d:
            return render_template("post_result.html", message=f"CALL {d[key]}")
        else:
            return render_template("post_result.html", message="GIVE A VALID INPUT")
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)