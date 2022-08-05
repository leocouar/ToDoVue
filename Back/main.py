from flask import Flask, Response, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config.from_object('config.MainConfig')
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    firstname = db.Column(db.String(20))
    lastname = db.Column(db.String(20))
    password = db.Column(db.String(255), nullable=False)
    nacdate = db.Column(db.DateTime)
    deleted = db.Column(db.Boolean)
    tasks = db.relationship('Task', backref='User', lazy=True)

    def __init__(self, username, firstname, lastname, password, nacdate, deleted):
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.nacdate = nacdate
        self.deleted = deleted

class Task(db.Model):
    _tablename_="Task"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.Text)
    date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'),primary_key=True, nullable=False)

    def __init__(self,user_id,title,description,date):
        self.user_id = user_id
        self.title = title
        self.description = description
        self.date = date





db.create_all()

@app.route('/')
def index():
    return '''  <div>
                <h3> Sistema De Gestion ToDo. </h3>
                <h4>Proyecto de API con Flask y SQLAlchemy</h4>
                <h4>Creado por Leonardo Couñago Arballo</h4>
                </div>'''


@app.route('/ping')
def ping():
    return jsonify({"menssage":"Pong!"})

@app.route("/users", methods=['GET'])
def getUsers():
    return "hola"

@app.route('/user', methods=['POST'])
def createUser():
    username = request.json['username']
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    password = request.json['password']

    


if __name__ == "__main__":
    app.run(debug=True)