let reviews = [
  {
    id: 1,
    name: "Anna Maria Davitashvili",
    job: "Lease Analyst",
    img: "https://community.mis.temple.edu/files/avatars/14661/5ac7ca2e4f95d-bpfull.jpg",
    text: "Davita Consulting Group is a U.S.-based technology consulting firm with a team of expert consultants that partner with companies around the world to help successfully implement new business and technology. At Davita Consulting Group, our consultants will help your business keep    pace with the changing consumer market. Our Cloud, Big Data, and BIAnalytics specialists will identify the tools necessary for the growth",
  },
  {
    id: 2,
    name: "Hermione Granger",
    job: "Witch",
    img: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKPEoroIKaM9U492WaWeTfJhVJveQt6BVDaMab6ARzMA&s",
    text: "She is an overachiever who excels academically and is described by Rowling as a 'very logical, upright and good' character. Rowling adds that Hermione's parents, two Muggle dentists, are a bit bemused by their odd daughter but 'quite proud of her all the same'.",
  },
  {
    id: 3,
    name: "Nicolas Cage",
    job: "Actor",
    img: "https://images.fineartamerica.com/images/artworkimages/mediumlarge/3/nicolas-cage-osama-kh.jpg",
    text: "Cage is known for his edgy, intense personality and for his passion for method acting. He is said to have had two teeth pulled for his role in Birdy, slashed his arm for Racing With the Moon (1984) and swallowed a live cockroach for Vampire's Kiss (1992).",
  },
  {
    id: 4,
    name: "Valiko Mizandari a.k.a. Mimino",
    job: "Pilot",
    img: "https://www.peoples.ru/art/cinema/characters/mimino/mimino_4.jpg",
    text: "Pilot Mimino works at small local airlines in Telavi, Georgia, flying helicopters between small villages. He dreams of piloting large planes for major international airlines, so he goes to Moscow for refresher courses. There in a hotel he meets truck driver Rubik from Dilijan, Armenia who is given a place in that hotel by mistake. Together they have many adventures in Moscow. However, both are homesick and long for their family, friends, and hometowns in the Caucasus.",
  },
];

let img = document.querySelector(".img");
let author = document.querySelector(".name");
let job = document.querySelector(".job");
let info = document.querySelector(".info");

let leftArrow = document.querySelector(".leftArrow");
let rightArrow = document.querySelector(".rightArrow");
let random = document.querySelector(".random");

let currentItem = 0;

window.addEventListener("DOMContentLoaded", function () {
  showPerson();
});

function showPerson() {
  let item = reviews[currentItem];
  img.src = item.img;
  author.textContent = item.name;
  job.textContent = item.job;
  info.textContent = item.text;
}

rightArrow.addEventListener("click", () => {
  currentItem++;
  if (currentItem > reviews.length - 1) {
    currentItem = 0;
  }
  showPerson();
});

leftArrow.addEventListener("click", () => {
  currentItem--;
  if (currentItem < 0) {
    currentItem = reviews.length - 1;
  }
  showPerson();
});

random.addEventListener("click", () => {
  let randomNumber;
  do {
    randomNumber = Math.floor(Math.random() * reviews.length);
  } while (randomNumber == currentItem);
  currentItem = randomNumber;
  showPerson();
});
