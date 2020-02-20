
function showMap(longitude, latitude)
{
  let location ={lat: parseFloat(latitude), lng: parseFloat(longitude)};
  let options_map = {
    zoom : 15,
    center : location
  };

  let divMap = document.getElementById("map");
  let map = new google.maps.Map(divMap, options_map);
  let marker = new google.maps.Marker({position : location, map:map});
  //Add info on the marker
}



function fetching(){
      
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
      .then(function (response) { // At this point, Flask dealted with the question
        let question = document.getElementById("question")
        question.innerHTML = body["question"];
        return response.json();
      })
      .then(function (data) {

        let adresse = document.getElementById("adresse");
        let histoire = document.getElementById("histoire");
        // I should remove the animation about here as we have our data 

        adresse.innerHTML = data["adresse"];
        let longitude = data["longitude"];
        let latitude = data["latitude"];
        console.log(data);

        showMap(longitude,latitude);
        histoire.innerHTML = data["summary"];

        //Add catch !
      });
      }

      let submit = document.getElementById("form");
      submit.addEventListener("submit",function(event){
        fetching();
        event.preventDefault();
      })
