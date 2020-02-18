from flask import render_template,request, jsonify, make_response, request
from app.functions import *
from app import app

@app.route('/') #Decorator which binds the url given ('/') to the function home.
@app.route('/home') #When a browser request this URL, FLASK give the return value as RESPONSE.
def home():
    return render_template('home.html', title = 'Grandpy The Bot')

@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        question = request.get_json()["question"]
        # Once we have our question stored we can parse it !
        sentence_listed = sentence_to_list(question)
        sentence_parsed = parserKiller(sentence_listed)
        # Our question has been parsed time to send it to the google API
        location = Maps.google_api(sentence_parsed)
        info_jsonified = jsonify(adresse = location["formatted_address"],
                                latitude = location["geometry"]["location"]["lat"],
                                longitude= location["geometry"]["location"]["lng"])
        return info_jsonified