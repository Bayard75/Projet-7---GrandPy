from app.fonctions import parserKiller

def test_parserKiller():

    result = parserKiller("Salut GrandPY peux tu me donner l'adresse d'Openclassrooms ?")
    assert result == 'adresse openclassrooms'

