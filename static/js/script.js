//Makes the bottom bar follow the screen when scrolling
window.addEventListener('scroll', function() {
    var footer = document.querySelector('.footer');
    footer.style.transition = 'bottom 0.5s';
  
    if (window.scrollY + window.innerHeight >= document.body.offsetHeight) {
      footer.style.bottom = '0';
    } else {
      footer.style.bottom = '-' + footer.offsetHeight + 'px';
    }
  });
  
/*
paypal.Buttons({
   createOrder: function(data, actions) {
     // Personalizza e restituisci un oggetto di ordine
     return actions.order.create({
       purchase_units: [{
         amount: {
           value: '10.00' // Importo del pagamento
         }
       }]
     });
   },
   onApprove: function(data, actions) {
     // Esegui il pagamento quando l'utente approva
     return actions.order.capture().then(function(details) {
       // Esegui azioni dopo il pagamento completato
       showSuccessMessage();
     });
   }
 }).render('#paypal-button-container');

 function showSuccessModal() {
   var successModal = document.getElementById('successModal');
   if (successModal) {
       successModal.style.display = 'block';
   } else {
       var successMessage = document.createElement('div');
       successMessage.id = 'successModal';
       successMessage.innerHTML = '<p>Payment successful!</p><button onclick="hideSuccessModal()">Close</button>';
       document.body.appendChild(successMessage);
   }
} */

/*function hideSuccessModal() {
   var successModal = document.getElementById('successModal');
   if (successModal) {
       successModal.style.display = 'none';
   }
} */



 function addToFavorites(gameId) {
  // Qui dovresti implementare la logica per aggiungere il gioco ai preferiti
  // Potresti utilizzare localStorage, un database, o qualsiasi altro metodo di persistenza dei dati.
  // In questo esempio, mostro un messaggio di alert.
  alert(`Il gioco con ID ${gameId} è stato aggiunto ai preferiti.`);
}


function getPrezzo(oggetto) {
  if (oggetto === 'A') {
      return 10.99;
  } else if (oggetto === 'B') {
      return 15.99;
  } else {
      return 0.00;
  }
}


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
              // Logica da eseguire dopo il pagamento avvenuto con successo
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
