from flask import Flask
from flask_cors import CORS

app = Flask(__name__) 
app.config.from_object("config.Config")
CORS(app)

from app import routes
if __name__ =='__main__':
    app.run()