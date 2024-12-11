let AC = document.querySelector(".AC");
let plusMinus = document.querySelector(".plusMinus");
let percentage = document.querySelector(".percentage");
let division = document.querySelector(".division");
let multiply = document.querySelector(".multiply");
let minus = document.querySelector(".minus");
let plus = document.querySelector(".plus");
let equal = document.querySelector(".equal");
let zero = document.querySelector(".zero");
let one = document.querySelector(".one");
let two = document.querySelector(".two");
let three = document.querySelector(".three");
let four = document.querySelector(".four");
let five = document.querySelector(".five");
let six = document.querySelector(".six");
let seven = document.querySelector(".seven");
let eight = document.querySelector(".eight");
let nine = document.querySelector(".nine");
let dot = document.querySelector(".dot");

let screenText = document.querySelector(".screenText");
let expression = "";

function updateScreen() {
  screenText.textContent = expression;
}

function handleNumberClick(number) {
  expression += number;
  updateScreen();
}

zero.addEventListener("click", () => handleNumberClick(0));
one.addEventListener("click", () => handleNumberClick(1));
two.addEventListener("click", () => handleNumberClick(2));
three.addEventListener("click", () => handleNumberClick(3));
four.addEventListener("click", () => handleNumberClick(4));
five.addEventListener("click", () => handleNumberClick(5));
six.addEventListener("click", () => handleNumberClick(6));
seven.addEventListener("click", () => handleNumberClick(7));
eight.addEventListener("click", () => handleNumberClick(8));
nine.addEventListener("click", () => handleNumberClick(9));

dot.addEventListener("click", () => {
  if (!expression.includes(".")) {
    expression += ".";
    updateScreen();
  }
});

function handleOperationClick(operator) {
  const lastChar = expression.slice(-1);
  if (!isOperator(lastChar)) {
    expression += ` ${operator} `;
    updateScreen();
  }
}

function isOperator(char) {
  return char === "+" || char === "-" || char === "*" || char === "/";
}

division.addEventListener("click", () => handleOperationClick("/"));
multiply.addEventListener("click", () => handleOperationClick("*"));
minus.addEventListener("click", () => handleOperationClick("-"));
plus.addEventListener("click", () => handleOperationClick("+"));

equal.addEventListener("click", () => {
  try {
    expression = eval(expression).toString();
    updateScreen();
  } catch (error) {
    expression = "Error";
    updateScreen();
  }
});

AC.addEventListener("click", () => {
  expression = "";
  updateScreen();
});

plusMinus.addEventListener("click", () => {
  expression = eval(`-1 * (${expression})`).toString();
  updateScreen();
});

percentage.addEventListener("click", () => {
  expression = eval(`0.01 * (${expression})`).toString();
  updateScreen();
});
