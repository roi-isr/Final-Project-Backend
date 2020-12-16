from flask import Flask
from flask import jsonify
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    conn = connect_to_db()
    create_table(conn)
    print("Successful connection and creation")
    return "hello"

@app.route('/roi')
def roi():
    return "Roi"

@app.route('/daniel')
def daniel():
    return "Daniel"

def connect_to_db():
    conn = psycopg2.connect("""
    dbname='d6sja18bu5d6qh'
    user='srmngikqacnqlj'
    password='c74259d2a98acc497a45815abd47dfd4cf0d29484019b547d1c1b8fe789f9fd2'
    host='ec2-54-170-100-209.eu-west-1.compute.amazonaws.com'
    port='5432'""")
    return conn

def create_table(conn):
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS diamonds (name TEXT, price INTEGER);")

if __name__=="__main__":
    app.run(port=5000,debug=True)

