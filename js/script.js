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
  
