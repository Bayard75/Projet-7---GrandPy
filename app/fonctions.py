from flask_wtf import FlaskForm
import os,json
import urllib.request


API_MAPS_KEY= 'AIzaSyCQQOAFsvFsdCHFRMCg8RFlZbV8COmZwVE'

with open(r'app\resources\parser.json') as file:
    parser = json.load(file)

def parserKiller(phrase_a_clean):
    decoupe = []
    phrase = phrase_a_clean.lower()
    phrase = phrase.replace("'",' ')
    phrase = phrase.replace('"',' ')
    phrase = phrase.split(' ')

    for mot in phrase:
        if mot not in parser:
            decoupe.append(mot)
    phrase_decoupe = " ".join(decoupe)
    return phrase_decoupe

def google_api(returned_response):
    # With our returned reponse search the adresse through the google API
    # Should return a json file
    pass
