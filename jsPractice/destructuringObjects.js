const person = {
  firstName: "Chris",
  lastName: "Lam",
  age: 47,
  occupation: "firefighter"
};

const { age, occupation: occ } = person;
console.log(`${age}, ${occ}`);
