
let chatbox = document.getElementById('chatbox');



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
  console.log(size)
  let map = new google.maps.Map(divMap[size-1], options_map);
  let marker = new google.maps.Marker({position : location, map:map});
  //Add info on the marker
}



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
      .then(function (response) { // At this point, Flask dealted with the question
        let user_input = document.getElementById("value");
        let question = document.createElement('p')
        
        question.setAttribute('class','user');
        console.log(user_input.value)
        chatbox.appendChild(question);
        question.innerHTML = user_input.value;
        user_input.value='';
        console.log(response.status)
        return response.json();
      })
      .then(function (data) {
        // I should remove the animation about here as we have our data 
        let returned_adress = document.createElement('p');
        let history = document.createElement('p');
        returned_adress.setAttribute('class','bot');
        history.setAttribute('class','bot');
        console.log(data);

        chatbox.appendChild(returned_adress);
        returned_adress.innerHTML = data['adresse'];
        showMap(data["longitude"],data["latitude"]);
        chatbox.appendChild(history)
        history.innerHTML = data["summary"];
      
        //Add catch !
      })
}

let submit = document.getElementById("form");
submit.addEventListener("submit",function(event)
{
    fetching();
    event.preventDefault();
})
