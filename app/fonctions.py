from flask_wtf import FlaskForm
import os,json

working_dir = os.getcwd()
resources_dir = os.path.join(working_dir,'resources')
parser_emplacement = os.path.join(resources_dir,'parser.json')
print(parser_emplacement)
with open(r'C:\Users\mbaya\OneDrive\Documents\grandpy\app\resources\parser.json') as file:
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

