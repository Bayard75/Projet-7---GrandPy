function send(){
    let body = {value : document.getElementById("value").value}
    let request = new XMLHttpRequest();
    
    request.onreadystatechange = function(){
      if(this.readyState == XMLHttpRequest.DONE){
        let response = JSON.parse(this.responseText);
        console.log(response);
        document.getElementById("result").innerHTML = response;
      }    
    }
    request.open("POST","http://127.0.0.1:5000/submit");
    request.setRequestHeader("Content-Type","application/json");
    request.send();
    
  }
  
  let submit = document.getElementById("button");
  submit.addEventListener("click",function(event){
    send();
})