#This file will host all of our python functions
import os, json

GOOGLE_API_KEY = 'AIzaSyCQQOAFsvFsdCHFRMCg8RFlZbV8COmZwVE'

try : 
    with open('app/parser.json','r') as file:
        parser_json = json.load(file)
except:
    print('Le fichier parser.json est introuvable dans le working directory')

def sentence_to_list(sentence_to_clean):
    '''This function will take in a sentence to clean
        and will return a list of words '''

    sentence_to_clean = sentence_to_clean.lower()
    sentence_to_clean = sentence_to_clean.replace("'"," ")
    sentence_cleaned = sentence_to_clean.replace('"',' ')
    
    sentence_listed = sentence_cleaned.split()
    return sentence_listed

def parserKiller(sentence_listed):
    '''This function will take in a list of words
        put it through our parser and return a string with fewer words'''
    
    sentence_parsed =[] #empty list that we store all the approved words

    for words in sentence_listed:
        if words not in parser_json:
            sentence_parsed.append(words)
        else:
            pass

    sentence_parsed = ' '.join(sentence_parsed)
    return sentence_parsed

api_url_format = f'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={sentence_parsed}&inputtype=textquery&fields=formatted_address,geometry/location&key={GOOGLE_API_KEY}'

if __name__=='__main__':
    pass

