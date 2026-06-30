from flask import Flask
from hi import hi
from home import home
from by import by

app=Flask(__name__)
app.secret_key="your_secret_key_here"
app.register_blueprint(home,url_prefix="/")
app.register_blueprint(hi,url_prefix="/hi")
app.register_blueprint(by,url_prefix="/by")

if __name__=="__main__":
    app.run(debug=True)

