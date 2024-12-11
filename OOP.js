class User {
  firstName;
  lastName;
  age;
  id;
  constructor(fn, ln, age, id) {
    this.firstName = fn;
    this.lastName = ln;
    this.age = age;
    this.id = id;
  }
}

let user = new User("Lado", "Xurcilava", 36, 1);
console.log(user);
