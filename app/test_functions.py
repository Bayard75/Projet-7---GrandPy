import pytest
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

def test_google_api():


    assert Maps.google_api('openclassrooms') =={'formatted_address': '7 Cité Paradis, 75010 Paris, France', 'geometry': {'location': {'lat': 48.8748465, 'lng': 2.3504873}}}


def test_get_page_id():

    wiki = Wiki_API('openclassrooms',48.8748465,2.3504873)
    assert wiki.get_page_id() == 5091748

def test_get_summary():
    
    wiki = Wiki_API('openclassrooms',48.8748465,2.3504873)
    assert wiki.get_summary(5091748) =="L'Hôtel Bourrienne (appelé aussi Hôtel de Bourrienne et Petit Hôtel Bourrienne) est un hôtel particulier du XVIIIe siècle situé au 58 rue d'Hauteville dans le 10e arrondissement de Paris. Propriété privée, il est classé au titre des monuments historiques depuis le 20 juin 1927. En juillet 2015, il est acheté par l'entrepreneur Charles Beigbeder pour en faire l"
