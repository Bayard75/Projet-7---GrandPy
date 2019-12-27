#This file will host all of our python functions
import os, json

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
    
    for words in sentence_listed:
        if words in parser_json:
            sentence_listed.remove(words)
        else:
            pass
    
    sentence_parsed = ' '.join(sentence_listed)
    return sentence_parsed


if __name__=='__main__':
    pass

