from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource,Api,reqparse,marshal_with,abort,fields

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///database.db"
db=SQLAlchemy(app)
api=Api(app)

user_args=reqparse.RequestParser()
user_args.add_argument('name',type=str,required=True,help="Name cant be blank")
user_args.add_argument('email',type=str,required=True,help="Email cant be blank")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
}

class Users(Resource):
    @marshal_with(resource_fields) 
    def get(self):
        users = User.query.all()
        return users
    
    @marshal_with(resource_fields)
    def post(self):
        args = user_args.parse_args()
        
        existing_user_name = User.query.filter_by(name=args['name']).first()
        existing_user_email = User.query.filter_by(email=args['email']).first()

        if existing_user_name:
            abort(409, message=f"User with name '{args['name']}' already exists.")
        if existing_user_email:
            abort(409, message=f"User with email '{args['email']}' already exists.")

        new_user = User(name=args['name'], email=args['email'])
        db.session.add(new_user)
        db.session.commit()
        return new_user, 201 

api.add_resource(Users, '/api/users/')

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),unique=True,nullable=False)
    email=db.Column(db.String(100),unique=True,nullable=False)
    
    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email})"

@app.route("/")
def home():
    return f"<h1>FLASK API SERVER</h1>"

if __name__=="__main__":
    app.run(debug=True)