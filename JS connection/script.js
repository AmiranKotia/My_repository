// let fileToUpload = document.querySelector("#fileToUpload");
// let userInfo = document.querySelector("#userInfo");
// let typeOption = document.querySelector("#typeOption");
// let addBtn = document.querySelector(".addBtn");
// let toDoArray = [];
// let tempImgSrc = "";

// function clickUploadImage() {
//   fileToUpload.click();
// }
// addBtn.addEventListener("click", () => {
//   let toDoObject = {
//     userInformation: userInfo.value,
//     type: typeOption.value,
//     image: "",
//   };
// });

// function uploadImage() {}

let playerSymbol = "X";
let button = document.querySelector(".btn");

document.querySelectorAll("td").forEach((cell) => {
  cell.addEventListener("click", () => {
    if (cell.textContent == "") {
      cell.textContent = playerSymbol;
      if (checkWinner()) {
        alert(`Player ${playerSymbol} wins!`);
        resetGame();
      } else if (checkTie()) {
        alert("It's a tie!");
        resetGame();
      } else {
        togglePlayer();
      }
    }
  });
});

button.addEventListener("click", () => {
  resetGame();
});

function togglePlayer() {
  if (playerSymbol == "X") {
    playerSymbol = "O";
  } else {
    playerSymbol = "X";
  }
}

function checkWinner() {
  let cells = document.querySelectorAll("td");
  let winningCombinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];

  for (let combo of winningCombinations) {
    let [a, b, c] = combo;
    if (
      cells[a].textContent &&
      cells[a].textContent == cells[b].textContent &&
      cells[b].textContent == cells[c].textContent
    ) {
      return true;
    }
  }
  return false;
}

function checkTie() {
  let cells = document.querySelectorAll("td");
  for (let cell of cells) {
    if (cell.textContent == "") {
      return false;
    }
  }
  return true;
}

function resetGame() {
  document.querySelectorAll("td").forEach((cell) => {
    cell.textContent = "";
  });
  playerSymbol = "X";
}

// let increment = document.querySelector(".increment");
// let decrement = document.querySelector(".decrement");
// let count = document.querySelector(".count");
// let H2 = document.querySelector(".H2");
// let countJS = 0;
// let count10 = 0;
// decrement.disabled = true;
// let checkFor0 = () => {
//   if (countJS == 0) {
//     decrement.disabled = true;
//   } else {
//     decrement.disabled = false;
//   }
// };

// increment.addEventListener("click", () => {
//   countJS++;
//   count.textContent = countJS;
//   if (countJS % 10 == 0) {
//     count10++;
//     H2.textContent = count10;
//   }
//   checkFor0();
// });
// decrement.addEventListener("click", () => {
//   countJS--;
//   count.textContent = countJS;
//   if (count10 !== 0) {
//     if (countJS % 10 == 0) {
//       count10--;
//       H2.textContent = count10;
//     }
//   }
//   checkFor0();
// });

// let reset = document.querySelector(".resCount");

// reset.addEventListener("click", () => {
//   countJS = 0;
//   count10 = 0;
//   count.textContent = countJS;
//   H2.textContent = count10;
//   decrement.disabled = true;
// });

// let boxs = document.querySelectorAll(".box");
// let booleanTypeForTicTacToe = true;
// boxs.forEach((box) => {
//   box.addEventListener("click", () => {
//     if (box.innerHTML == "") {
//       if (booleanTypeForTicTacToe) {
//         box.innerHTML = "x";
//         booleanTypeForTicTacToe = false;
//       } else {
//         box.innerHTML = "o";
//         booleanTypeForTicTacToe = true;
//       }
//       whoIsWinner();
//     }
//   });
// });

// let count = 0;

// let winnerPostion = [
//   [0, 1, 2],
//   [2, 5, 8],
//   [1, 4, 7],
//   [0, 3, 6],
//   [3, 4, 5],
//   [6, 7, 8],
//   [0, 4, 8],
//   [2, 4, 6],
// ];

// function whoIsWinner() {
//   let allIndexArray = Array.from(boxs).map((x) => x.innerHTML);
//   for (let winner of winnerPostion) {
//     if (
//       allIndexArray[winner[0]] == allIndexArray[winner[1]] &&
//       allIndexArray[winner[1]] == allIndexArray[winner[2]] &&
//       allIndexArray[winner[0]] != ""
//     ) {
//       alert(`winner is ${allIndexArray[winner[0]]}`);
//       resetValues();
//     }
//   }
//   count++;
//   if (count == 9) {
//     alert("It's a tie");
//     resetValues();
//   }
// }

// function resetValues() {
//   booleanTypeForTicTacToe = true;
//   boxs.forEach((x) => {
//     x.innerHTML = "";
//   });
// }
