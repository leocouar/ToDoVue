from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

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
    
    def serialize(self):
        return {
            "username" : self.username,
            "firstname" : self.firstname,
            "lastname" : self.lastname,
            "nacdate" : self.nacdate,
            "deleted" : self.deleted
        }

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


