import pytest,requests
from app.functions import *

def test_sentence_to_list():
    
    assert sentence_to_list("""Salut GrandPy !
                            Est-ce que tu connais 
                            l'adresse d'OpenClassrooms ?""") == ['salut', 
                            'grandpy', '!', 'est-ce', 'que', 'tu', 'connais',
                             'l', 'adresse', 'd', 'openclassrooms', '?']

                        
def test_parserKiller():

    assert parserKiller(['salut', 'grandpy', '!', 
    'est-ce', 'que', 'tu', 'connais', 'l', 'adresse',
     'd', 'openclassrooms', '?']) == "openclassrooms"


def test_get_page_id():

    wiki = Wiki_API('openclassrooms',48.8748465,2.3504873)
    assert wiki.get_page_id() == 5091748

def test_get_summary():
    
    wiki = Wiki_API('openclassrooms',48.8748465,2.3504873)
    assert wiki.get_summary(5091748) == ('Hôtel Bourrienne', "L'Hôtel Bourrienne (appelé aussi Hôtel de Bourrienne et Petit Hôtel Bourrienne) est un hôtel particulier du XVIIIe siècle situé au 58 rue d'Hauteville dans le 10e arrondissement de Paris.")

class Mock_Response:
    '''This class will be used to mock the behavoir of requests.get'''
    def __init__(self, result):
        self.result = result

    def json(self):
        return self.result

class Test_Google_Api():


    def test_adress_found(self, monkeypatch):
        sentence ='openclassrooms'
        def mocked(url):
            return Mock_Response({
                    "candidates":
                    [{
                        "formatted_address":
                            "7 Cité Paradis, 75010 Paris, France"
                    }],
                    "status": "OK"
                })
        monkeypatch.setattr("requests.get", mocked)
        assert Maps.google_api(sentence) != False

        
