This application is developped for the 7th project in the developper path for Openclassrooms.

The app will be using the following stack :
- Python
- Flask
- HTML/CSS
- Javascript
- Bootstrap

This application goal is to take in a user input as a question for example : "Hi GrandPy can you give me the adress of the Louvres ?".
Python will then parse the question for keywords, get the coordinates (Google maps API) of the louvres, send them to JS et post a map of the adress.
Then the bot will call on the wikipedia API to give us some information on the location.

api_url_format = f'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={sentence_parsed}&inputtype=textquery&fields=formatted_address,geometry/location&key={GOOGLE_API_KEY}'
