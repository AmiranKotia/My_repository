let input = document.querySelector("#input");
let button = document.querySelector("#add");
let taskContainer = document.querySelector("#task-container");
let trash = document.querySelector("#trash");
let timerInterval;

function addItem() {
  if (input.value == "") {
    alert("Please write a task");
  } else {
    let parentDiv = document.createElement("div");
    let childDiv = document.createElement("div");
    let inProgress = document.createElement("i");
    let done = document.createElement("i");
    let trashIcon = document.createElement("i");

    parentDiv.className = "task";
    parentDiv.textContent = input.value;

    childDiv.appendChild(inProgress);
    inProgress.className = "fa-solid fa-clock-rotate-left doing";
    inProgress.style.color = "grey";
    inProgress.addEventListener("click", () => {
      if (inProgress.style.color == "grey") {
        inProgress.style.color = "rgb(255, 110, 57)";
        done.style.color = "grey";
        parentDiv.classList.remove("checked");

        let existingTimerInput = childDiv.querySelector(".timer-input");
        if (existingTimerInput) {
          existingTimerInput.style.display = "block";
          existingTimerInput.focus();
        } else {
          let timerInput = document.createElement("input");
          timerInput.className = "timer-input";
          timerInput.type = "number";
          timerInput.placeholder = "Set timer (minutes)";
          timerInput.addEventListener("keydown", (event) => {
            if (event.key == "Enter") {
              stopTimer(parentDiv);
              startTimer(timerInput.value, parentDiv);
              timerInput.style.display = "none";
            }
          });

          childDiv.appendChild(timerInput);
          timerInput.focus();
        }
      } else {
        inProgress.style.color = "grey";
        pauseTimer();
      }
    });

    childDiv.appendChild(done);
    done.className = "fa-solid fa-check check";
    done.style.color = "grey";
    done.addEventListener("click", () => {
      if (parentDiv.classList.contains("checked")) {
        parentDiv.classList.remove("checked");
        done.style.color = "grey";
        stopTimer(parentDiv);
        removeTimerDisplay(parentDiv);
      } else {
        parentDiv.classList.add("checked");
        done.style.color = "rgb(0, 163, 101)";
        inProgress.style.color = "grey";
        pauseTimer();
        removeTimerDisplay(parentDiv);
      }
    });

    childDiv.appendChild(trashIcon);
    trashIcon.className = "fa-solid fa-trash trash";
    trashIcon.style.color = "grey";
    trashIcon.addEventListener("click", () => {
      parentDiv.remove();
      emptyContainer();
      stopTimer(parentDiv);
    });

    childDiv.appendChild(trashIcon);
    parentDiv.appendChild(childDiv);
    taskContainer.appendChild(parentDiv);
    input.value = "";
    document.querySelector("#removeAll").style.display = "block";
  }
}

input.addEventListener("keydown", (event) => {
  if (event.key == "Enter") {
    addItem();
  }
});

function removeAll() {
  let tasks = document.querySelectorAll(".task");
  tasks.forEach((task) => {
    task.remove();
  });
  emptyContainer();
}

function emptyContainer() {
  let remainingTasks = document.querySelectorAll(".task");
  if (remainingTasks.length == 0) {
    document.getElementById("removeAll").style.display = "none";
  }
}

function startTimer(minutes, taskElement) {
  let seconds = minutes * 60;
  let timerDisplay = document.createElement("div");
  timerDisplay.className = "timer-display";
  timerDisplay.textContent = `Time remaining: ${formatTime(seconds)}`;
  taskElement.appendChild(timerDisplay);

  timerInterval = setInterval(() => {
    seconds--;
    timerDisplay.textContent = `Time remaining: ${formatTime(seconds)}`;

    if (seconds <= 0) {
      clearInterval(timerInterval);
      timerDisplay.textContent = "Time's up!";
      taskElement.style.backgroundColor = "rgb(252, 150, 150)";
    }
  }, 1000);
}

function stopTimer(taskElement) {
  let timerDisplay = taskElement.querySelector(".timer-display");
  if (timerDisplay) {
    clearInterval(timerInterval);
  }
}

function pauseTimer() {
  if (timerInterval) {
    clearInterval(timerInterval);
  }
}

function modifyTimer(taskElement) {
  let existingTimerInput = taskElement.querySelector(".timer-input");
  let timerDisplay = taskElement.querySelector(".timer-display");

  if (timerDisplay) {
    timerDisplay.remove();
  }

  if (!existingTimerInput) {
    let timerInput = document.createElement("input");
    timerInput.className = "timer-input";
    timerInput.type = "number";
    timerInput.placeholder = "Set timer (minutes)";
    timerInput.addEventListener("keydown", (event) => {
      if (event.key == "Enter") {
        removeTimerDisplay(taskElement);

        stopTimer(taskElement);
        startTimer(timerInput.value, taskElement);
        timerInput.style.display = "none";
      }
    });

    taskElement.appendChild(timerInput);
    timerInput.focus();
  }
}

function removeTimerDisplay(taskElement) {
  let timerDisplay = taskElement.querySelector(".timer-display");
  if (timerDisplay) {
    timerDisplay.remove();
  }
}

function formatTime(seconds) {
  let minutes = Math.floor(seconds / 60);
  let remainingSeconds = seconds % 60;
  if (remainingSeconds < 10) {
    return `${minutes}:0${remainingSeconds}`;
  } else {
    return `${minutes}:${remainingSeconds}`;
  }
}
