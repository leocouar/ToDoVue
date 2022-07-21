from flask import Flask,jsonify

app = Flask(__name__)

user = {
    'user':{
        'id':1,
        'name': 'leonardo',
        'lastName':'Couñago Arballo',
    }
}

@app.route('/')
def index():
    return jsonify(user)

if __name__ == "__main__":
    app.run(debug=True)