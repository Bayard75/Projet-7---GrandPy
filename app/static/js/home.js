let submit = document.getElementById('form');
let bottomChat = document.getElementById('bottom-chat')
let chatbox = document.getElementById('chatbox');

class Bot
{
    constructor()
    {
      this.greeting = `Evidement que je peux te trouver ca ! 
                      Laisse moi quelques secondes pour me rappeller d'une bonne histoire.`
      this.wikiNotFound = `Malheuresement l'age a eu raison de moi !
                          Je n'arrive pas a me souvenir d'accedote sur cette endroit.`
      this.wikiFound =`Tiens j'en connais une bonne sur cette endroit, tu vas être epaté ?`
    }

    botAdressResponse(adresse)
    {
      console.log('adresse : '+adresse)
      if (adresse === undefined)
      {
        let adressState = {
          found : false,
          message : `Il semblerait que tu m'ais mal posé ta question
                    car je ne trouve aucune adresse pour ta recherche.
                    Reessaie, nous pouvons tous nous tromper.`
        };
        return adressState;

      }
      else
      {
        let adressState = {
          found : true,
          message : `Ah ! Je me disais que cela me rappelait quelque chose !
                    Ce que tu recherches se situe la : `+adresse+`.`
        };
        return adressState;
      };
    }
    
    botAnswer(answer)
    {
        let botDiv = document.createElement('div');
        botDiv.setAttribute('class','botMessage');

        let template = `
        <div class="media-body ml-3">
          <div class="bg-light rounded py-2 px-3 mb-2">
            <p class="text-small mb-0 text-muted">`+answer+`</p>
          </div>
        </div>
      </div>`

        botDiv.innerHTML = template;
        chatbox.appendChild(botDiv);
    }

    botAnswerWikiFound(summary,title)
    {
      let botDiv = document.createElement('div');
      botDiv.setAttribute('class','botMessage');
      console.log(title)
      let template = `
          <div class="media-body ml-3">
            <div class="bg-light rounded py-2 px-3 mb-2">
              <p class="text-small mb-0 text-muted">`+summary+`
              <a href="https://fr.wikipedia.org/wiki/`+title+`" target="_blank">
              En savoir plus sur Wikipedia !</a>
              </p>
            </div>
          </div>
        </div>`
      
        
      botDiv.innerHTML = template;
      chatbox.appendChild(botDiv);

    }
  }


let grandPy = new Bot;

function delay(ms) {
  return function(x) {
    return new Promise(resolve => setTimeout(() => resolve(x), ms));
  };
}

function scrollToBottom() 
{
  let chatbox = document.getElementById('chatbox')
  chatbox.scrollTop = chatbox.scrollHeight;
}

function showMap(longitude, latitude)
{
  console.log('showmap ')
  let location ={lat: parseFloat(latitude), lng: parseFloat(longitude)};
  let options_map = {
    zoom : 15,
    center : location
  };
  let createDivMap = document.createElement('div');
  createDivMap.setAttribute('class','map');
  chatbox.appendChild(createDivMap);
  let divMap = document.getElementsByClassName('map')
  size = divMap.length;
  let map = new google.maps.Map(divMap[size-1], options_map);
  let marker = new google.maps.Marker({position : location, map:map});
  //Add info on the marker
}


function showQuestion(question)
{
  let userDiv = document.createElement('div');
  userDiv.setAttribute('class','userMessage');
  
  let userMessageTemplate = `
    <div class="media w-50 ml-auto mb-3">
      <div class="media-body">
        <div class="bg-primary rounded py-2 px-3 mb-2">
          <p class="text-small mb-0 text-white">`+question+`</p>
        </div>
      </div>
    </div>`;

  userDiv.innerHTML = userMessageTemplate;
  chatbox.appendChild(userDiv);

}

function growingSpinnerAnimation()
{

      let botDivLoad = document.createElement('div');
      botDivLoad.setAttribute('id','loading')
      let loadingTemplate ='<div class="spinner-border text-primary"></div>'
      botDivLoad.innerHTML = loadingTemplate;
      chatbox.appendChild(botDivLoad);
};

function fetching()
{
      
      // I should set the animation here before the post request 
      let body = {question : document.getElementById("value").value};
      let myHeaders = new Headers();
      myHeaders.append("Content-Type","application/json"); //Important or request.get_json() returns None 

      fetch('/submit', {
              // Specify the method
              method: 'POST',
              // A JSON payload
              body: JSON.stringify(body),
              headers: myHeaders
            })
            .then(function (response) 
            { 
              // At this point, Flask dealted with the question
                let user_input = document.getElementById("value");
                showQuestion(user_input.value);
                scrollToBottom();
                user_input.value = '';
                growingSpinnerAnimation();

                return response.json();

            })
            .then(delay(1000))
            .then(function (data)
            {
                // I should remove the animation about here as we have our data 
                chatbox.removeChild(chatbox.lastChild);
                let adresseState = grandPy.botAdressResponse(data['adresse']);
                if (adresseState.found === false)
                {
                  grandPy.botAnswer(adresseState.message);
                }
                else
                {
                  grandPy.botAnswer(adresseState.message);
                  scrollToBottom();
                  return data;
                }
            })
            .then(delay(1000))
            .then(function(data)
            {
                showMap(data["longitude"],data["latitude"]);
                scrollToBottom();
                return data
            })
            .then(delay(1000))
            .then(function(data)
            {
                if (data["summary"] === undefined)
                {
                    grandPy.botAnswer(grandPy.wikiNotFound);
                    scrollToBottom();
                }
                else
                {
                    grandPy.botAnswer(grandPy.wikiFound);
                    scrollToBottom();
                    grandPy.botAnswerWikiFound(data["summary"],data["title"]);
                    scrollToBottom();
                };    
            })
            .catch(function(error)
            {
              showQuestion(error);
            })
  };

submit.addEventListener("submit",function(event)
{
    fetching();
    event.preventDefault();
})