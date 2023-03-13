const Student = {
    firstName: "Mercy",
    lastName: "Jill",
    age: 21,
    eyeColor: "brown"
  };

  Student.firstName
  Student["lastName"];

  // methords 
  const person = {
    firstName: "Bob",
    lastName : "Afwata",
    id       : 5566,
    fullName : function() {
      return this.firstName + " " + this.lastName;
    }
  };

  name = person.fullName();