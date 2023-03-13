for (let i = 0; i < 5; i++) {
    text += "The number is " + i + "<br>";
  }


  // for loop in
const person = {fname:"Bob", lname:"Afwata", age:30};

let text = "";
for (let x in person) {
  text += person[x];
}

//numbers
const numbers = [45, 4, 9, 16, 25];

let txt = "";
for (let x in numbers) {
  txt += numbers[x];
}



//break
for (let i = 0; i < 10; i++) {
  if (i === 3) { break; }
  text += "The number is " + i + "<br>";
}


//continue

for (let i = 0; i < 10; i++) {
  if (i === 3) { continue; }
  text += "The number is " + i + "<br>";
}