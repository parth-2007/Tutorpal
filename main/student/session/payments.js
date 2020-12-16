var price = '{{price}}'
var id = '{{session_id}}'
var url = '127.0.0.1:8000/process_payment/'

/*
var data = {
  'price':price,
  'id':id,
}

function submitData(){
  console.log('Clicked button')
  var data = {
    'price':price,
    'id':id,
  }

  fetch(url,{
    method:"POST",
    headers:{
      'Content-Type':'application/json',
      'X-CSRFToken':'{{csrf_token}}',
    },
    body:JSON.stringify({'data':data}
    )
  })
  .then((response) => response.json())
  .then((data) => {
    console.log('Success:', data);
    alert('Transaction Completed');
    window.location.href = "/requests/"

  })
}
*/


function submitData(){
  $.ajax({
      type: "POST",
      url: "127.0.0.1:8000/process_payment/",
      headers: {
          "Content-Type": "application/json",
          "HTTP_GROUP_NAME": "groups_name",
          "X-CSRFToken": "{{csrf_token}}",
      },
      data: {
          'price':price,
          'id':id,
          //"csrfmiddlewaretoken": "{{csrf_token}}",
      },
      success: function(data){
          console.log("success");
          //console.log(data);
      },
      failure: function(data){
          console.log("failure");
          //console.log(data);
      },
  });
  console.log('Sent POST Request')


paypal.Buttons({

  style: {
        color:  'blue',
        shape:  'pill',
        label:  'pay',
        height: 40
    },

  createOrder: function(data, actions) {
    return actions.order.create({
      purchase_units: [{
        amount: {
          value: parseFloat(price).toFixed(2)
        }
      }]
    });
  },
  onApprove: function(data, actions) {
    return actions.order.capture().then(function(details) {
      //alert('Transaction completed by ' + details.payer.name.given_name);
      submitData();
    });
  }
}).render('#paypal-button-container')};