from flask import render_template,request, jsonify, make_response, request
from app.functions import *
from app import app
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
app.app_context().push()
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.String)
    latitude = db.Column(db.String)
db.create_all()
gp_1 = User(id=1, longitude=48.875640, latitude=2.359587)
gp_2 = User(id=2, longitude=48.863148, latitude=2.344904)
gp_3 = User(id=3, longitude=48.869892, latitude=2.352425)
gp_4 = User(id=4, longitude=48.867622, latitude=2.362921)
db.session.add(gp_1)
db.session.add(gp_2)
db.session.add(gp_3)
db.session.add(gp_4)
db.session.commit()
@app.route('/') #Decorator which binds the url given ('/') to the function home.
@app.route('/home') #When a browser request this URL, FLASK give the return value as RESPONSE.
def home():
    data = []
    data.append(["groupe1", User.query.filter_by(id=1).first().longitude, User.query.filter_by(id=1).first().latitude])
    data.append(["groupe1", User.query.filter_by(id=2).first().longitude, User.query.filter_by(id=2).first().latitude])
    data.append(["groupe1", User.query.filter_by(id=3).first().longitude, User.query.filter_by(id=3).first().latitude])
    data.append(["groupe1", User.query.filter_by(id=4).first().longitude, User.query.filter_by(id=4).first().latitude])
    return render_template('home.html', title = 'H24 Koltes', data_loc=data)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        loca = request.get_json()
        print(loca)
        q = User.query.filter_by(id=int(loca['group'])).first()
        q.longitude = loca['latitude']
        q.latitude = loca['longitude']
        db.session.commit()
        return make_response(loca)
    