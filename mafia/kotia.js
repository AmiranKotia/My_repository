let left = document.querySelector(".leftArrow");
let right = document.querySelector(".rightArrow");
let slider = document.querySelector(".slider");
let images = document.querySelectorAll(".img");
let bottom = document.querySelector(".bottom-carousel");

let slideNumber = 1;
let length = images.length;

for (let i = 0; i < length; i++) {
  let div = document.createElement("div");
  div.className = "button";
  bottom.appendChild(div);
}

let buttons = document.querySelectorAll(".button");
buttons[0].style.backgroundColor = "rgba(255, 255, 255, 0.7)";

let resetBg = () => {
  buttons.forEach((button) => {
    button.style.backgroundColor = "transparent";
  });
};

buttons.forEach((button, i) => {
  button.addEventListener("click", () => {
    resetBg();
    slider.style.transform = `translateX(-${i * 1500}px)`;
    slideNumber = i + 1;
    button.style.backgroundColor = "rgba(255, 255, 255, 0.7)";
  });
});

let nextSlide = () => {
  slider.style.transform = `translateX(-${slideNumber * 1500}px)`;
  slideNumber++;
};
let previousSlide = () => {
  slider.style.transform = `translateX(-${(slideNumber - 2) * 1500}px)`;
  slideNumber--;
};
let firstSlide = () => {
  slider.style.transform = `translateX(0px)`;
  slideNumber = 1;
};
let lastSlide = () => {
  slider.style.transform = `translateX(-${(length - 1) * 1500}px)`;
  slideNumber = length;
};
let changeColor = () => {
  resetBg();
  buttons[slideNumber - 1].style.backgroundColor = "rgba(255, 255, 255, 0.7)";
};

right.addEventListener("click", () => {
  slideNumber < images.length ? nextSlide() : firstSlide();
  changeColor();
});

left.addEventListener("click", () => {
  slideNumber > 1 ? previousSlide() : lastSlide();
  changeColor();
});
