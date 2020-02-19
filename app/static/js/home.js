
function showMap(longitude, latitude)
{
  let location ={lat: latitude, lng: longitude};
  let options_map = {
    zoom : 15,
    center : location
  };
  let divMap = document.getElementById("map");
  let map = new google.maps.Map(divMap, options_map);
  let marker = new google.maps.Marker({position : location, map:map});

}



function fetching(){
      let body = {question : document.getElementById("value").value};
      let myHeaders = new Headers();
      myHeaders.append("Content-Type","application/json"); //Important or request.get_json() return None 

      fetch('/submit', {
        // Specify the method
        method: 'POST',
        // A JSON payload
        body: JSON.stringify(body),
        headers: myHeaders
      })
      .then(function (response) { // At this point, Flask dealted with the question
        let question = document.getElementById("question")
        question.innerHTML = body["question"];
        return response.json();
      })
      .then(function (data) {

        let adresse = document.getElementById("adresse");
        adresse.innerHTML = data["adresse"];
        setTimeout(showMap(data["longitude"],data["latitude"]), 1000000);
      });
      }

      let submit = document.getElementById("form");
      submit.addEventListener("submit",function(event){
        console.log('apppel de la fonction send()');
        fetching();
        event.preventDefault();
      })
