from flask import Flask

app = Flask(__name__) 

from app import routes

@app.route("/")
def home():
    return "Hello world"

