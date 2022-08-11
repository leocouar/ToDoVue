from flask import Flask, Response, request, jsonify
from models import db,User,Task
from logging import exception
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config.from_object('config.MainConfig')
db.init_app(app)

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
    try:
        userList = User.query.all()
        toReturn = [User.serialize() for user in userList]
        return jsonify(toReturn), 200
    except:
        exception("[SERVER]: Error al retornar lista de usuarios.")
        return jsonify({"msg":"Error al retornar usuarios"})

@app.route("/user/<id>", methods=['GET'])
def getUser(id):
    user= User.query.filter_by(id=id)
    
    if not user:
        return jsonify({"msg":"este usuario no existe"})
    else:
        return jsonify(user)

@app.route('/user', methods=['POST'])
def createUser():
    if request.method == 'POST':
        username = request.json['username']
        firstname = request.json['firstname']
        lastname = request.json['lastname']
        password = request.json['password']

        user_name = User.query.filter_by(username=username).first()
        
        if user_name == None:
            user = User(username=username, password=generate_password_hash(password)) #Crear usuario
            db.session.add(user)
            db.session.commit()

@app.route("/user/<id>", methods=['PUT'])
def updateUser(id):
    pass

    


if __name__ == "__main__":
    app.run(debug=True)