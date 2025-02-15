window.addEventListener('resize', function() {
    const main = document.querySelector('.main');
    if (window.innerWidth <= 500) {
        main.style.flexDirection = 'column'; 
    } else {
        main.style.flexDirection = 'row';
    }
});