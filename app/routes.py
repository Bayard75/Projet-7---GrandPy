from flask import render_template
from app import app

@app.route('/') #Decorator which binds the url given ('/') to the function home.
@app.route('/home') #When a browser request this URL, FLASK give the return value as RESPONSE.
def home():
    return render_template('home.html', title = 'Grandpy The Bot')