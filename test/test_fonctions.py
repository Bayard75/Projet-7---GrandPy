from app.fonctions import parserKiller, Maps
import json

def test_parserKiller():

    result = parserKiller("Salut GrandPY peux tu me donner l'adresse d'Openclassrooms ?")
    assert result == 'openclassrooms'

def test_google_api():
    expeted_result = {'candidates': [{'formatted_address': '7 Cité Paradis, 75010 Paris, France', 'geometry': {'location': {'lat': 48.8748465, 'lng': 2.3504873}}}], 'status': 'OK'}
    print(expeted_result)
    result = Maps.google_api('adresse openclassrooms')
    print(result)
    assert result == expeted_result

