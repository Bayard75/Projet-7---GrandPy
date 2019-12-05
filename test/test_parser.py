import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

path = r'C:\Users\mbaya\OneDrive\Documents\grandpy\app\resources\parser.json'
try:
    with open(path,"r") as file:
        parser = file.read()
except:
    pass


def mock_parser(phrase):
    '''This mock fonction will take one sentence as an argument
    pass it through our parser, and then will return an location
    name'''
    decoupe = []
    phrase = phrase.lower()
    phrase = phrase.replace("'",' ')
    phrase = phrase.replace('"',' ')
    phrase = phrase.split(' ')

    for mot in phrase:
        print(mot)
        if mot not in parser:
            decoupe.append(mot)
    print(decoupe)
    phrase_decoupe = " ".join(decoupe)
    return phrase_decoupe
b ="Salut ! Peux tu me dire ou se trouve le louvres ?"
a = mock_parser(b)
print(a)

def test_parserKiller(monkeypatch):
    monkeypatch.setattr('app.fonctions.parserKiller', mock_parser)
    result = mock_parser("Salut GrandPY peux tu me donner l'adresse d'Openclassrooms ?")
    assert result == 'adresse openclassrooms'
