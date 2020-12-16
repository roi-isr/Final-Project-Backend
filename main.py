from flask import Flask
import json
app = Flask(__name__)

@app.route('/')
def home():
    return json.dumps({"msg": "Hello"})

@app.route('/roi')
def roi():
    return "Roi"

@app.route('/daniel')
def daniel():
    return "Daniel"

app.run(debug=True)

