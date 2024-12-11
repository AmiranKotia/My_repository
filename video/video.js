let btn = document.querySelector(".button");
let video = document.querySelector(".videoContainer");

btn.addEventListener("click", function () {
  if (!btn.classList.contains("slide")) {
    btn.classList.add("slide");
    video.pause();
  } else {
    btn.classList.remove("slide");
    video.play();
  }
});

let loader = document.querySelector(".loader");

loader.style.visibility = "visible";

window.addEventListener("load", function () {
  loader.style.visibility = "visible";
  loader.classList.add("hide-loader");
});
