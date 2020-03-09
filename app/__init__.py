from flask import Flask

app = Flask(__name__) 
app.config.from_object("config.DevelopmentConfig")
from app import routes

if __name__ =='__main__':
    app.run()