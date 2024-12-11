// // pirveli varianti---
// let button = document.querySelector(".button");
// let backgroundColor = localStorage.getItem("color");
// document.body.style.backgroundColor = backgroundColor;

// button.addEventListener("click", () => {
//   if (backgroundColor == "black") {
//     document.body.style.backgroundColor = "white";
//     localStorage.setItem("color", "white");
//   } else {
//     document.body.style.backgroundColor = "black";
//     localStorage.setItem("color", "black");
//   }
//   backgroundColor = localStorage.getItem("color");
// });

// // meore varianti---
// function setBackgroundColor() {
//   document.body.style.backgroundColor = backColor;
// }
// let backColor = localStorage.getItem("color") || "white";
// setBackgroundColor();
// function changeColor() {
//   if (backColor == "white") {
//     backColor = "black";
//     localStorage.setItem("color", "black");
//     setBackgroundColor();
//   } else {
//     backColor = "white";
//     localStorage.setItem("color", "white");
//     setBackgroundColor();
//   }
// }

let mainDiv = document.querySelector(".MainDiv");
let pages = document.querySelector(".pages");
let array = [];
let currentPage = 1;
let itemsPerPage = 10;
let url = `https://jsonplaceholder.typicode.com/posts`;
let http = new XMLHttpRequest();

function sendRequest(method, url, callBack) {
  http.open(method, url);
  http.send();
  http.onload = () => {
    callBack(http.response);
  };
}

sendRequest("GET", url, (res) => {
  let result = JSON.parse(res);
  array = result;
  generateVisual();
  generatePages();
  clickEventFunction();
});

function generateVisual() {
  let startIndex = (currentPage - 1) * itemsPerPage;
  let endIndex = startIndex + itemsPerPage;
  let empty = ``;
  for (let i = startIndex; i < endIndex; i++) {
    empty += `
      <div style="border:1px solid white; background-color:black;color:white;">
        <h1>${array[i].id}</h1>
        <h1 id="title_${array[i].id}">${array[i].title}</h1>
        <p>${array[i].body}</p>
        <button onclick="deleteOneCard(${array[i].id})">delete</button>
        <button onclick="openUpdateModal(${array[i].id}, '${array[i].title}')">update</button>
      </div>
    `;
  }
  mainDiv.innerHTML = empty;
}

function generatePages() {
  let totalPage = Math.ceil(array.length / itemsPerPage);
  let empty = ``;
  for (let i = 1; i <= totalPage; i++) {
    empty += `<button class="button">${i}</button>`;
  }
  pages.innerHTML = empty;
}

function clickEventFunction() {
  let buttons = document.querySelectorAll(".button");
  buttons[0].classList.add("red");
  buttons.forEach((btn) => {
    btn.addEventListener("click", () => {
      currentPage = parseInt(btn.textContent);
      buttons.forEach((bt) => {
        bt.classList.remove("red");
      });
      btn.classList.add("red");
      generateVisual();
    });
  });
}

function deleteOneCard(id) {
  http.open("delete", `${url}/${id}`);
  http.send();
  http.onload = () => {
    let findIndex = array.findIndex((card) => card.id == id);
    if (findIndex != -1) {
      array.splice(findIndex, 1);
      alert("deleted");
      generateVisual();
    }
  };
}

function openUpdateModal(id, currentTitle) {
  let modalDiv = createModal();
  modalDiv.querySelector(".myInputForUpdate").value = currentTitle;
  document.body.appendChild(createModalBackground(modalDiv));

  let updateButton = modalDiv.querySelector(".modalUpdateButton");
  updateButton.addEventListener("click", () => {
    let updatedTitle = modalDiv.querySelector(".myInputForUpdate").value;
    updateCard(id, updatedTitle);
    document.body.removeChild(document.querySelector(".modalBackground"));
  });
}

function updateCard(id, updatedTitle) {
  let http = new XMLHttpRequest();
  http.open("PUT", `${url}/${id}`);

  let updateValueObject = {
    title: updatedTitle,
  };

  http.setRequestHeader("Content-Type", "application/json");

  http.send(JSON.stringify(updateValueObject));

  http.onload = () => {
    if (http.status == 200) {
      let findIndex = array.findIndex((card) => card.id == id);
      if (findIndex != -1) {
        array[findIndex].title = updatedTitle;
        alert("updated");
        generateVisual();
      }
    }
  };
}

function createInput() {
  let input = document.createElement("input");
  input.classList.add("myInputForUpdate");
  return input;
}

function createButton() {
  let button = document.createElement("button");
  button.classList.add("modalUpdateButton");
  button.textContent = "updateNow";
  return button;
}

function createModal() {
  let modalDiv = document.createElement("div");
  modalDiv.classList.add("modal");
  modalDiv.appendChild(createInput());
  modalDiv.appendChild(createButton());
  return modalDiv;
}

function createModalBackground(modalDiv) {
  let backgroundDiv = document.createElement("div");
  backgroundDiv.classList.add("modalBackground");
  backgroundDiv.appendChild(modalDiv);
  return backgroundDiv;
}

// fetch("https://jsonplaceholder.typicode.com/todos/1", {
//   method: "GET",
// })
//   .then((resolve) => {
//     return resolve.json();
//   })
//   .then((response) => {
//     console.log(response);
//   })
//   .catch((error) => {
//     console.error(error);
//   });

// async function getData() {
//   let fetchData = await fetch("https://jsonplaceholder.typicode.com/todos/1");

//   if (!fetchData.ok) {
//     console.error("error");
//   }

//   let result = await fetchData.json();
//   console.log(result);
// }
// getData();
