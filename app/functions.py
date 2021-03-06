#This file will host all of our python functions
import os, json, requests
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

try : 
    with open('app/parser.json','r') as file:
        parser_json = json.load(file)
except:
    print('Le fichier parser.json est introuvable dans le working directory')


def sentence_to_list(sentence_to_clean):
    '''This function will take in a sentence to clean
        and will return a list of words '''
    print(sentence_to_clean)
    sentence_to_clean = sentence_to_clean.lower()
    sentence_to_clean = sentence_to_clean.replace("'"," ")
    sentence_cleaned = sentence_to_clean.replace('"',' ')
    
    sentence_listed = sentence_cleaned.split()
    return sentence_listed

def parserKiller(sentence_listed):
    '''This function will take in a list of words
        put it through our parser and return a string with fewer words'''
    print(sentence_listed)
    sentence_parsed =[] #empty list where we store all the approved words

    for word in sentence_listed:
        if word not in parser_json:
            sentence_parsed.append(word)

    sentence_parsed = ' '.join(sentence_parsed)
    return sentence_parsed

class Maps():
    '''This class will regroup all the functions
    associeted to the google api calls from python side'''

    @staticmethod
    def google_api(sentence_parsed):
        '''This method will take in a sentence parsed and
            return a json file with a formatted adresse 
            latitude and longitude.'''
        print(sentence_parsed)
        maps_url_format = f'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={sentence_parsed}&inputtype=textquery&fields=formatted_address,geometry/location&key={GOOGLE_API_KEY}'
        location_infos = requests.get(maps_url_format).json()
        print(location_infos)
        if location_infos['status'] == 'OK':
            location_infos = (location_infos['candidates'][0]) #We only take the first match and the adress
            return location_infos
        else:
            return False

class Wiki_API():
    '''This class will handle all interactions
        with the wikipedia API
        This class should be able to :
        -Find a page given a location
        -Find and send back a summary of the '''
    
    def __init__(self,location_name, latitude,longitude):
        
        self.lat = str(latitude)
        self.lng = str(longitude)
        self.url = 'https://fr.wikipedia.org/w/api.php'

    def get_page_id(self):
        """This function will use the API to retrieve the page id
            of a given location"""
        
        PARAMS = {
            "action": "query",
            "format": "json",
            "list": "geosearch",
            "gscoord":self.lat + "|" + self.lng
        }

        response = requests.get(self.url,params=PARAMS)
        data = response.json()
        try :
            first_page_id = data["query"]["geosearch"][0]["pageid"]
            return first_page_id

        except KeyError:
            return False
    
    def get_summary(self,page_id):
        """This function will return the summary of a article
            thanks to a page_id"""
        
        PARAMS = {
            'action': 'query',
            'format': 'json',
            'prop': 'extracts',
            'exintro': '',
            'explaintext': '',
            'exsentences':'1', # We return only the first sentence of the summary
            'pageids': page_id
        }

        try :
            response = requests.get(self.url, params=PARAMS)
            data = response.json()
            title = (data["query"]["pages"][str(page_id)]['title'])
            summary = data["query"]["pages"][str(page_id)]['extract']
            return (title,summary)
        except:
            return False

if __name__=="__main__":
    pass

a= sentence_to_list("Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel?")
b = parserKiller(a)
print(a)
print(b)
print(Maps.google_api(b))
