function getConditionValue() {
    var uiCondition = document.getElementsByName("uiCondition");
    for(var i in uiCondition) {
      if(uiCondition[i].checked) {
          return uiCondition[i];
      }
    }
    return -1; // Invalid Value
  }
  
  
  function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var cars = document.getElementById("uiCar");
    var condition = document.getElementById("uiCondtion");
    var body = document.getElementById("uiBody");
    var transmission = document.getElementById("uiTrans");
    var fuel = document.getElementById("uiFuel");
    var year = document.getElementById("uiYear");
    var capacity = document.getElementById("uiCapacity");
    var mileage = document.getElementById("uiMileage");
    var estPrice = document.getElementById("uiEstimatedPrice");
    var url = "http://127.0.0.1:5000/predict_car_price";
  
    $.post(url, {
        cars: cars.value,
        condition: condition.value,
        body: body.value,
        transmission: transmission.value,
        fuel: fuel.value,
        year: parseInt(year.value),
        capacity: parseFloat(capacity.value),
        mileage: parseFloat(mileage.value),     
    },function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Laks</h2>";
        console.log(status);
    });
  }

function onPageLoad(){
    console.log("Document loaded");
    var url1 = "http://127.0.0.1:5000/get_car_names";
    var url2 = "http://127.0.0.1:5000/get_car_body";
    var url3 = "http://127.0.0.1:5000/get_car_transmission";
    var url4 = "http://127.0.0.1:5000/get_car_fuel";
    var url5 = "http://127.0.0.1:5000/get_car_condition";
    $.get(url1, function(data, status) {
        console.log("got response get_car_names_request");
        if(data){
            var cars = data.cars;
            var uiCar = document.getElementById("uiCar");
            $('#uiCar').empty();
            for(var i in cars) {
                var opt = new Option(cars[i]);
                $('#uiCar').append(opt);
            }
        }
    });
    $.get(url2, function(data, status) {
      console.log("got response get_car_body_request");
      if(data){
          var body = data.body;
          var uiBody = document.getElementById("uiBody");
          $('#uiBody').empty();
          for(var i in body) {
              var opt = new Option(body[i]);
              $('#uiBody').append(opt);
          }
      }
    });
    $.get(url3, function(data, status) {
      console.log("got response get_car_trans_request");
      if(data){
          var trans = data.transmission;
          var uiTrans = document.getElementById("uiTrans");
          $('#uiTrans').empty();
          for(var i in trans) {
              var opt = new Option(trans[i]);
              $('#uiTrans').append(opt);
          }
      }
    });
    $.get(url4, function(data, status) {
      console.log("got response get_car_fuel_request");
      if(data){
          var fuel = data.fuel;
          var uiFuel = document.getElementById("uiFuel");
          $('#uiFuel').empty();
          for(var i in fuel) {
              var opt = new Option(fuel[i]);
              $('#uiFuel').append(opt);
          }
      }
    });
    $.get(url5, function(data, status) {
      console.log("got response get_car_Condition_request");
      if(data){
          var condition = data.condition;
          var uiCondtion = document.getElementById("uiCondtion");
          $('#uiCondtion').empty();
          for(var i in condition) {
              var opt = new Option(condition[i]);
              $('#uiCondtion').append(opt);
          }
      }
    });
}

window.onload = onPageLoad;