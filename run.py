from app import app #From the package app we import the variable app
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEY_DATABSE_URI'] = 'sqlite:///site'
if __name__== "__main__":
    app.run(debug=False)