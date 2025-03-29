
function changeButtonContent(buttonId) {
    const button = document.getElementById(buttonId);

    button.innerHTML = "button 2 ";
    button.style.fontSize = "20px"; 

}


////////////////////////////////////////////////////////////////////

let fruits = ['lemon', 'apple', ];

fruits.add('orange');

console.log(fruits);

////////////////////////////////////////////////////////////////////

let cars = ['BMW', 'opel', 'audi', ];

cars[cars.length - 1] = 'Mercedes';

console.log(cars);

/////////////////////////////////////////////////////////////////////