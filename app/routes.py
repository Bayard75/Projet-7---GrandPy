from flask import render_template,request, jsonify, make_response
from app.functions import *
from app import app

@app.route('/') #Decorator which binds the url given ('/') to the function home.
@app.route('/home') #When a browser request this URL, FLASK give the return value as RESPONSE.
def home():
    return render_template('home.html', title = 'Grandpy The Bot')

@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method =='POST':
        user_input = request.form.get("user_input") #The type of this will be NoneType 
        user_input = str(user_input) #We change it to str to avoid Attribute error with the following function
        listed = sentence_to_list(user_input)
        parsed = parserKiller(listed)
        locations_infos = Maps.google_api(parsed)
        info_jsonified = jsonify(adresse = locations_infos["formatted_address"],
                                latitude = locations_infos["geometry"]["location"]["lat"],
                                longitude= locations_infos["geometry"]["location"]["lng"])
        return info_jsonified