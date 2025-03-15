class Car {
    main( brand, color, year) {
        this.brand = brand;
        this.color = color;
        this.year = year;
    }
}
const car1 = new Car("bmw", "black", 2024);
const car2 = new Car("audi", "rs6", 2022);
const car3 = new Car("lamborgini", "aventador", 2023);


class Car1 {
    constructor( brand, horsePower) {
        this.brand = brand;
        this.horsePower = horsePower;
    }
}

increaseHorsePower() 
    this.horsePower += 50;
  
const car5 = new Car("mercedes", 500);



//3
let array = [1, 2, 3, 4, 5];

//4
let array1 = new Array(17 ,18, 55, 12, 9);

//5
let array2 = [13, 32, 3, 4, 7];

for (let i = 0; i < array2.length; i++) {
    console.log(array2[i]);
}

//6
let array3 = [0, 5, 7, 4, 5];

console.log(array3[1]); 
console.log(array3[0]); 
console.log(array3[3]);