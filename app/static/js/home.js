function fetching(){
      let body = {question : document.getElementById("value").value};
      let myHeaders = new Headers();
      myHeaders.append("COntent-Type","application/json"); //Important or request.get_json() return None 

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
      });
      }

      let submit = document.getElementById("form");
      submit.addEventListener("submit",function(event){
        console.log('apppel de la fonction send()');
        fetching();
        event.preventDefault();
      })
