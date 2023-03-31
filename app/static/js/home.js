function localte_all(){
    data = document.getElementById('data_loc').innerHTML
    console.log(data.replaceAll("'", '"'))
    var locations = JSON.parse(data.replaceAll("'", '"'));
    
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 13.75,
      center: new google.maps.LatLng(48.868599, 2.358921),
      mapTypeId: google.maps.MapTypeId.ROADMAP
    });
    
    var infowindow = new google.maps.InfoWindow();
  
    var marker, i;
    
    for (i = 0; i < locations.length; i++) {  
      console.log(Number(locations[i][1]))
      marker = new google.maps.Marker({
        position: new google.maps.LatLng(+locations[i][1], +locations[i][2]),
        map: map
      });
      
      google.maps.event.addListener(marker, 'click', (function(marker, i) {
        return function() {
          infowindow.setContent(locations[i][0]);
          infowindow.open(map, marker);
        }
      })(marker, i));
      }}

localte_all();