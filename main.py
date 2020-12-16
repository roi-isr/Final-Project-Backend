from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello"

@app.route('/roi')
def roi():
    return "Roi"

@app.route('/daniel')
def daniel():
    return "Daniel"

app.run(port=5000, debug=True)

