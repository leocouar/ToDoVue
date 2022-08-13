from flask import Flask, request , jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from datetime import datetime


app=Flask(__name__)
app.config.from_object('config.MainConfig')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    nacimiento = db.Column(db.DateTime)

    def __init__(self,username ,email, firstname, lastname, password, nacimiento):
        self.username = username
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.nacimiento = nacimiento
    
    def __repr__(self) -> str:
        return self.username

    def serialize(self):
        return {
            "id": f"{self.id}",
            "username": f"{self.username}",
            "email": f"{self.email}",
            "firstname": f"{self.firstname}",
            "lastname": f"{self.lastname}",
            "nacimiento": f"{self.nacimiento}"
        }
        
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    text = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(80), nullable=False)
    create = db.Column(db.DateTime, nullable=False)
    delete = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer)
    
    def __init__(self, title, text, status, create, delete):
        self.title = title
        self.text = text
        self.status = status
        self.create = create
        self.delete = delete

db.create_all()

#USUARIOS
#POST
@app.route('/user', methods=['POST'])
def saveUser():
    if request.method == 'POST':
        try:
            username = str(request.json['username'])
            email = str(request.json['email'])
            firstname = str(request.json['firstname'])
            lastname = str(request.json['lastname'])
            password = generate_password_hash(request.json['password'])
            day = int(request.json['day'])
            month = int(request.json['month'])
            year = int(request.json['year'])
            nacdate = datetime(year=year,month=month, day=day)
            validacion = User.query.filter_by(username=username).first()
            if validacion == None:
                try:
                    be = User(username=username , email=email, firstname=firstname, lastname=lastname, password=password, nacimiento=nacdate)
                    db.session.add(be)
                    db.session.commit()
                    return jsonify({"msg":"El usuario se creo coerrectamente"})
                except:
                    return jsonify({"msg":"error al generar el usuario"})
            else:
                return jsonify({"msg":"usuario ya existente"})
        except:
            return jsonify({"msg": "error"})

@app.route('/user', methods=['GET'])
def getUsers():
    us= User.query.all()
    userList = [user.serialize() for user in us]
    return jsonify(userList)

@app.route('/user/<id>', methods=['GET'])
def getUser(id):
    usuario = User.query.filter_by(id=id).first()
    user = usuario.serialize()
    return jsonify(user)

@app.route('/user/<id>', methods=['POST','GET'])
def updateUser(id):
    usuario = User.query.get(id)
    if request.method == 'POST':
        usuario.username = str(request.json['username'])
        usuario.email = str(request.json['email'])
        usuario.firstname = str(request.json['firstname'])
        usuario.lastname = str(request.json['lastname'])
        usuario.password = generate_password_hash(request.json['password'])
        db.session.commit()
        return jsonify({"msg":"ok"})


#TASK
if __name__ == "__main__":
    app.run(debug=True)
