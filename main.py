from flask import Flask
from flask import jsonify

import json
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"msg": "Hello"})

@app.route('/roi')
def roi():
    return "Roi"

@app.route('/daniel')
def daniel():
    return "Daniel"

app.run(debug=True)

