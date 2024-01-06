
//function to get the price for the games
function getPrezzo(oggetto) {
  if (oggetto === 'A') {
      return 10.99;
  } else if (oggetto === 'B') {
      return 15.99;
  } else if(oggetto === 'Free') {
      return 0.00;
  }
}

 //function to use the paypal apy to create a button for payments t
function initPayPalButton(oggetto, containerId) {
  paypal.Buttons({
      createOrder: function(data, actions) {
          return actions.order.create({
              purchase_units: [{
                  amount: {
                      value: getPrezzo(oggetto) 
                  }
              }]
          });
      },
      onApprove: function(data, actions) {
          return actions.order.capture().then(function(details) {
              // payment successful
              alert('Pagamento completato per ' + oggetto + '. ID transazione: ' + details.id);
          });
      },
      onError: function(err) {
          console.error('Errore durante il pagamento:', err);
      }
  }).render('#' + containerId);
}


initPayPalButton('A', 'paypal-button-container-A');
initPayPalButton('B', 'paypal-button-container-B');
initPayPalButton('Free', 'paypal-button-container-Free');
