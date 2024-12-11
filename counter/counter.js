let count = 0;
const h1 = document.querySelector(".h1");
const btns = document.querySelectorAll(".btn");

btns.forEach(function (btn) {
  btn.addEventListener("click", function (e) {
    const styles = e.currentTarget.classList;
    if (styles.contains("decrease")) {
      count--;
    } else if (styles.contains("increase")) {
      count++;
    } else {
      count = 0;
    }
    if (count > 0) {
      h1.style.color = "darkgreen";
      document.body.style.backgroundColor = "lightgreen";
    }
    if (count < 0) {
      h1.style.color = "darkred";
      document.body.style.backgroundColor = "lightcoral";
    }
    if (count == 0) {
      h1.style.color = "black";
      document.body.style.backgroundColor = "grey";
    }
    h1.textContent = count;
  });
});
