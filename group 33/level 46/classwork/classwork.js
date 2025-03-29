const buttons = ['btn1', 'btn2', 'btn3'];

buttons.forEach((id) => {
    const button = document.getElementById(id);
    button.addEventListener('click', function() {
        
        button.style.backgroundColor = 'pink';
        
        button.textContent = 'nice';
    });
});