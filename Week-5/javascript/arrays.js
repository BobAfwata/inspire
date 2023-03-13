//declare arrays
const cars = ["Saab", "Volvo", "BMW"];

// access array using [id]
const cars = ["Saab", "Volvo", "BMW"];
let car = cars[0];


// last element
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let fruit = fruits[fruits.length - 1];



//using for loops
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let fLen = fruits.length;

let text = "<ul>";
for (let i = 0; i < fLen; i++) {
  text += "<li>" + fruits[i] + "</li>";
}
text += "</ul>";