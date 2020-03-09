from flask import render_template,request, jsonify, make_response, request
from app.functions import *
from app import app

@app.route('/') #Decorator which binds the url given ('/') to the function home.
@app.route('/home') #When a browser request this URL, FLASK give the return value as RESPONSE.
def home():
    return render_template('home.html', title = 'Grandpy The Bot')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        question = request.get_json()["question"]
        # Once we have our question stored we can parse it !
        sentence_listed = sentence_to_list(question)
        sentence_parsed = parserKiller(sentence_listed)
        # Our question has been parsed time to send it to the google API

        location_maps = Maps.google_api(sentence_parsed)
        if location_maps == False:
            return make_response(jsonify(location_maps))
        location_wiki = Wiki_API(sentence_parsed,
                                location_maps["geometry"]["location"]["lat"],
                                location_maps["geometry"]["location"]["lng"])

        location_wiki_page_id = location_wiki.get_page_id()
        if location_wiki_page_id == False:
            return make_response(jsonify(location_wiki_page_id))

        location_wiki_summary = location_wiki.get_summary(location_wiki_page_id)
        if location_wiki_summary == False:
            return make_response(jsonify(location_wiki_summary))

        info_jsonified = jsonify(adresse = location_maps["formatted_address"],
                                latitude = (location_maps["geometry"]["location"]["lat"]),
                                longitude = (location_maps["geometry"]["location"]["lng"]),
                                summary = location_wiki_summary)
                                
        return make_response(info_jsonified)