const questions = [
  {
    question:
      "YOU NEED TO USE EXTRA CAUTION WHEN DRIVING NEAR A PEDESTRIAN USING A WHITE CANE BECAUSE:",
    answers: [
      { text: "They are deaf", correct: false },
      { text: "They have a mental disability", correct: false },
      { text: "They are blind", correct: true },
      { text: "They have a walking problem", correct: false },
    ],
  },
  {
    question:
      "WHEN DRIVING NEAR A BLIND PEDESTRIAN WHO IS CARRYING A WHITE CANE OR USING A GUIDE DOG, YOU SHOULD:",
    answers: [
      { text: "Slow down and be prepared to stop", correct: true },
      { text: "Take the right-of-way", correct: false },
      { text: "Proceed normally", correct: false },
      { text: "Drive away quickly", correct: false },
    ],
  },
  {
    question: "YOU MAY DRIVE AROUND THE GATES AT A RAILROAD CROSSING:",
    answers: [
      { text: "When the train has passed", correct: false },
      { text: "Never", correct: true },
      { text: "When the lights have stopped flashing", correct: false },
      { text: "When other drivers drive around the gates", correct: false },
    ],
  },
  {
    question: "HIGHWAY AND EXPRESSWAY GUIDE SIGNS ARE:",
    answers: [
      { text: "Orange with black letters", correct: false },
      { text: "Green with white letters", correct: true },
      { text: "Yellow with black letters", correct: false },
      { text: "Red with white letters", correct: false },
    ],
  },
  {
    question:
      "FROM TOP TO BOTTOM, THE FOLLOWING IS THE PROPER ORDER FOR TRAFFIC LIGHTS:",
    answers: [
      { text: "Red, yellow, green", correct: true },
      { text: "Red, green, yellow", correct: false },
      { text: "Green, red, yellow", correct: false },
      { text: "Green, yellow, red", correct: false },
    ],
  },
  {
    question: "IF A GREEN ARROW TURNS INTO A GREEN LIGHT, YOU:",
    answers: [
      {
        text: "May still turn but you must yield to oncoming traffic",
        correct: true,
      },
      { text: "May no longer turn and must proceed straight", correct: false },
      { text: "Still have the right of way to turn", correct: false },
      {
        text: "No longer have to turn the way the arrow indicates",
        correct: false,
      },
    ],
  },
  {
    question: "A STEADY YELLOW LIGHT AT AN INTERSECTION MEANS:",
    answers: [
      { text: "Go", correct: false },
      { text: "Yield to other cars", correct: false },
      { text: "Slow down and prepare to stop", correct: true },
      { text: "Stop", correct: false },
    ],
  },
  {
    question: "A FLASHING YELLOW ARROW MEANS THAT YOU:",
    answers: [
      {
        text: "Should stop and proceed with the turn when a green arrow appears",
        correct: false,
      },
      { text: "Should slow down and prepare to stop", correct: false },
      {
        text: "May turn, but must first yield to oncoming traffic and pedestrians",
        correct: true,
      },
      { text: "Have the right of way to turn", correct: false },
    ],
  },
  {
    question: "A FLASHING YELLOW LIGHT MEANS THAT YOU SHOULD:",
    answers: [
      { text: "Slow down and proceed with care", correct: true },
      { text: "Continue through if the way is clear", correct: false },
      { text: "Stop and proceed when a green light appears", correct: false },
      { text: "Stop and proceed when the way is clear", correct: false },
    ],
  },
  {
    question: "YOU MUST STOP WHEN YOU SEE A:",
    answers: [
      { text: "Flashing red light", correct: true },
      { text: "Steady yellow light", correct: false },
      { text: "Yellow arrow", correct: false },
      { text: "Flashing yellow light", correct: false },
    ],
  },
  {
    question: "A STEADY GREEN LIGHT AT AN INTERSECTION MEANS THAT YOU:",
    answers: [
      { text: "Must slow down and prepare to stop", correct: false },
      {
        text: "Must stop and check for oncoming traffic before proceeding",
        correct: false,
      },
      {
        text: "May drive through the intersection if the road is clear",
        correct: true,
      },
      { text: "May not turn right", correct: false },
    ],
  },
  {
    question:
      "A STEADY YELLOW LIGHT MEANS THAT A _______ LIGHT WILL SOON APPEAR.",
    answers: [
      { text: "Flashing yellow", correct: false },
      { text: "Flashing red", correct: false },
      { text: "Steady green", correct: false },
      { text: "Steady red", correct: true },
    ],
  },
  {
    question: "YOU MAY CONTINUE CAREFULLY THROUGH A YELLOW LIGHT IF:",
    answers: [
      {
        text: "There is an emergency vehicle crossing your lane",
        correct: false,
      },
      { text: "There are no pedestrians crossing", correct: false },
      { text: "You are turning right", correct: false },
      { text: "You are within the intersection", correct: true },
    ],
  },
  {
    question: "YOU MAY TURN LEFT AT A RED LIGHT IF:",
    answers: [
      {
        text: "There is no traffic coming in the opposite direction",
        correct: false,
      },
      {
        text: "You are turning from a one-way street onto another one-way street",
        correct: true,
      },
      {
        text: "You are turning from a two-way street onto a one-way street",
        correct: false,
      },
      { text: "The car in front of you turns left", correct: false },
    ],
  },
  {
    question: "IF A TRAFFIC LIGHT IS BROKEN OR NOT FUNCTIONING YOU SHOULD:",
    answers: [
      { text: "Continue as if it were a four-way stop sign", correct: true },
      { text: "Stop and wait for it to be repaired", correct: false },
      { text: "Stop and wait for a police officer to arrive", correct: false },
      { text: "Continue as you normally would", correct: false },
    ],
  },
  {
    question: "YOU MAY TURN RIGHT ON RED IF YOU:",
    answers: [
      {
        text: "Stop first and check for traffic and pedestrians",
        correct: true,
      },
      { text: "Have a right turn red arrow", correct: false },
      { text: "Are in the left lane", correct: false },
      { text: "Slow down first", correct: false },
    ],
  },
  {
    question: "WHEN MAKING A RIGHT TURN ON A GREEN LIGHT, YOU MUST:",
    answers: [
      { text: "Maintain normal driving speed", correct: false },
      { text: "Yield to pedestrians", correct: true },
      { text: "Stop and look for oncoming traffic", correct: false },
      { text: "Increase your normal driving speed", correct: false },
    ],
  },
  {
    question:
      "THE SPEED LIMIT IS _______ MILES PER HOUR WHEN THE YELLOW LIGHTS ARE FLASHING ON THE SCHOOL ZONE SPEED SIGN.",
    answers: [
      { text: "25", correct: false },
      { text: "30", correct: false },
      { text: "15", correct: true },
      { text: "20", correct: false },
    ],
  },
  {
    question: "A FLASHING RED LIGHT AT A RAILROAD CROSSING MEANS:",
    answers: [
      {
        text: "Stop, do not proceed until signals are completed",
        correct: true,
      },
      { text: "Slow down and proceed if clear", correct: false },
      { text: "Proceed with caution", correct: false },
      { text: "You have the right-of-way", correct: false },
    ],
  },
  {
    question:
      "YOU MAY PASS IF THE LINE DIVIDING TWO LANES IS A ___________ LINE.",
    answers: [
      { text: "Solid white", correct: false },
      { text: "Broken white", correct: true },
      { text: "Double solid yellow", correct: false },
      { text: "Solid yellow", correct: false },
    ],
  },
  {
    question:
      "LANES OF TRAFFIC MOVING IN THE SAME DIRECTION ARE DIVIDED BY ____ LINES.",
    answers: [
      { text: "Yellow", correct: false },
      { text: "White", correct: true },
      { text: "Red", correct: false },
      { text: "Black", correct: false },
    ],
  },
  {
    question:
      "YOU MAY NOT PASS ANOTHER CAR ON EITHER SIDE OF A _______ CENTERLINE.",
    answers: [
      { text: "Combination solid and broken yellow", correct: false },
      { text: "Single broken yellow", correct: false },
      { text: "Double solid yellow", correct: true },
      { text: "Single broken white", correct: false },
    ],
  },
  {
    question: "YOU MAY CROSS SOLID YELLOW LINES:",
    answers: [
      { text: "To pass traffic moving in the same direction", correct: false },
      { text: "During daylight hours only", correct: false },
      { text: "At any time", correct: false },
      { text: "When making turns", correct: true },
    ],
  },
  {
    question:
      "THE ROAD EDGE ON THE RIGHT SIDE IS MARKED BY A ___________ LINE.",
    answers: [
      { text: "Broken white", correct: false },
      { text: "Solid yellow", correct: false },
      { text: "Solid white", correct: true },
      { text: "Broken yellow", correct: false },
    ],
  },
  {
    question:
      "LANES OF TRAFFIC MOVING IN THE OPPOSITE DIRECTION ARE DIVIDED BY ____ LINES.",
    answers: [
      { text: "Yellow", correct: true },
      { text: "White", correct: false },
      { text: "Red", correct: false },
      { text: "Black", correct: false },
    ],
  },
  {
    question: "THE MINIMUM DRINKING AGE IN THIS STATE IS ____ YEARS.",
    answers: [
      { text: "9", correct: false },
      { text: "20", correct: false },
      { text: "21", correct: true },
      { text: "18", correct: false },
    ],
  },
  {
    question:
      "PEOPLE UNDER 16 YEARS OF AGE WHO USE A FALSE IDENTIFICATION CARD TO BUY ALCOHOL WILL:",
    answers: [
      {
        text: "Receive a driving suspension that starts on their 16th birthday",
        correct: true,
      },
      {
        text: "Not be able to take the driver’s exam until their 21st birthday",
        correct: false,
      },
      {
        text: "Receive a driving suspension that starts on their 21st birthday",
        correct: false,
      },
      { text: "Be sent to an alcohol safety education class", correct: false },
    ],
  },
  {
    question:
      "IF A PERSON UNDER 21 YEARS OLD CONSUMES ALCOHOL, BUT IS NOT DRIVING A MOTORVEHICLE, THE PENALTY FOR A FIRST OFFENSE IS:",
    answers: [
      {
        text: "A 90-day driver license suspension and up to a $500 fine",
        correct: true,
      },
      { text: "A 6-month probation", correct: false },
      { text: "Sentence to a corrections institution", correct: false },
      { text: "Points on the driving record", correct: false },
    ],
  },
  {
    question: "PARENTAL CONSENT TO CONDUCT BREATH, BLOOD, AND URINE TESTS IS:",
    answers: [
      { text: "Not required", correct: true },
      { text: "Required from only one parent", correct: false },
      { text: "Required for people under 16 years old", correct: false },
      { text: "Required from both parents", correct: false },
    ],
  },
  {
    question:
      "IT IS AGAINST THE LAW FOR ANYONE UNDER THE AGE OF 21 TO ______ ALCOHOL.",
    answers: [
      { text: "Wear clothing advertising", correct: false },
      { text: "Be in the presence of", correct: false },
      { text: "Consume", correct: true },
      { text: "Serve", correct: false },
    ],
  },
  {
    question:
      "IT IS AGAINST THE LAW FOR ANYONE UNDER THE AGE OF 21 TO ______ ALCOHOL.",
    answers: [
      { text: "Wear clothing advertising", correct: false },
      { text: "Possess", correct: true },
      { text: "Serve", correct: false },
      { text: "Be in the presence of", correct: false },
    ],
  },
  {
    question:
      "IT IS AGAINST THE LAW FOR ANYONE UNDER THE AGE OF 21 TO ______ ALCOHOL.",
    answers: [
      { text: "Serve", correct: false },
      { text: "Wear clothing advertising", correct: false },
      { text: "Be in the presence of", correct: false },
      { text: "Transport", correct: true },
    ],
  },
  {
    question:
      "ONE OF THE PENALTIES FOR DRIVING UNDER THE INFLUENCE OF ALCOHOL IS A(N):",
    answers: [
      { text: "5 – year driver’s license suspension", correct: false },
      { text: "$100.00 fine", correct: false },
      { text: "Attendance to Alcohol Highway Safety School", correct: true },
      { text: "12 – hour sentence in jail", correct: false },
    ],
  },
  {
    question:
      "IF YOU ARE ARRESTED FOR DRIVING UNDER THE INFLUENCE OF ALCOHOL AND YOU REFUSE TO TAKE THE BLOOD TEST, YOU WILL RECIEVE A:",
    answers: [
      { text: "Drug counseling treatment", correct: false },
      { text: "Sentence of one day in jail", correct: false },
      { text: "Driver’s License Suspension", correct: true },
      { text: "$300.00 fine", correct: false },
    ],
  },
  {
    question:
      "IF A POLICE OFFICER REQUIRES YOU TO TAKE A BLOOD, BREATH, OR URINE TEST, YOU:",
    answers: [
      { text: "May choose the test you prefer", correct: false },
      { text: "Must sign a consent form", correct: false },
      { text: "May refuse if underage", correct: false },
      {
        text: "Must take the test, or your license will be suspended",
        correct: true,
      },
    ],
  },
  {
    question:
      "FOR A FIRST CONVICTION FOR DRIVING UNDER THE INFLUENCE AT ANY BLOOD ALCOHOL CONCENTRATION LEVEL, YOU COULD:",
    answers: [
      { text: "Lose your license for up to 5 years", correct: false },
      {
        text: "Be required to conduct a public education class on the dangers of drunk driving",
        correct: false,
      },
      {
        text: "Be required to drive with a restricted occupational license",
        correct: false,
      },
      { text: "Pay a fine of at least $300", correct: true },
    ],
  },
  {
    question:
      "IF UNDER 21 YEARS OF AGE YOU ARE CONSIDERED TO BE DRIVING WHILE UNDER THE INFLUENCE IF YOUR BLOOD ALCOHOL LEVEL IS:",
    answers: [
      { text: ".08% or higher", correct: false },
      { text: ".10% or higher", correct: false },
      { text: ".02% or higher", correct: true },
      { text: ".05% or higher", correct: false },
    ],
  },
  {
    question:
      "IF YOU ARE UNDER AGE 21 AND ARE CONVICTED OF DRIVING UNDER THE INFLUENCE OF ALCOHOL, YOU WILL RECEIVE A ____ LICENSE SUSPENSION FOR A FIRST OFFENSE.",
    answers: [
      { text: "60-Day", correct: false },
      { text: "30-Day", correct: false },
      { text: "6-Month", correct: false },
      { text: "1-Year", correct: true },
    ],
  },
  {
    question:
      "IF YOU ARE UNDER AGE 21, AND ARE CONVICTED OF CARRYING A FALSE ID CARD, YOU WILL BE REQUIRED TO PAY A $500 FINE AND YOUR LICENSE WILL BE SUSPENDED FOR 90 DAYS.",
    answers: [
      {
        text: "Only if your blood alcohol content (BAC) is .02% or higher",
        correct: false,
      },
      { text: "Even if you were not driving", correct: true },
      {
        text: "Only if you were driving at the time of arrest",
        correct: false,
      },
      {
        text: "Only if your blood alcohol content (BAC) is .02% or higher and you were driving at the time of arrest",
        correct: false,
      },
    ],
  },
  {
    question:
      "THE ZERO TOLERANCE LAW REDUCED THE BLOOD ALCOHOL CONTENT (BAC) FROM .08% TO ____ FOR DRIVERS UNDER 21 TO BE CHARGED WITH DRIVING UNDER THE INFLUENCE.",
    answers: [
      { text: ".02%", correct: true },
      { text: ".05%", correct: false },
      { text: ".07%", correct: false },
      { text: ".08%", correct: false },
    ],
  },
  {
    question: "IF YOU ARE STOPPED BY A POLICE OFFICER, YOU SHOULD:",
    answers: [
      { text: "Unbuckle your seat belt and lower your window", correct: false },
      {
        text: "Get your paperwork ready before the officer reaches your car",
        correct: false,
      },
      {
        text: "Stay in your vehicle with your hands on the steering wheel, and wait for the officer to approach you",
        correct: true,
      },
      {
        text: "Get out of your car and walk toward the patrol car",
        correct: false,
      },
    ],
  },
  {
    question:
      "AT AN INTERSECTION CONTROLLED BY A STOP SIGN, IF YOU CAN’T GET A GOOD VIEW OF CROSS-STREET TRAFFIC WHEN YOU STOP BEHIND THE WHITE TOP BAR PAINTED ON THE PAVEMENT, YOU SHOULD:",
    answers: [
      { text: "Wait 5 seconds, then proceed", correct: false },
      { text: "Sound your horn before proceeding", correct: false },
      {
        text: "Put down your windows, listen for traffic, and then proceed",
        correct: false,
      },
      {
        text: "Pull forward slowly, check for traffic and pedestrians, and proceed when clear",
        correct: true,
      },
    ],
  },
];

const questionElement = document.getElementById("question");
const answerButtons = document.getElementById("answers");
const nextButton = document.getElementById("next");

let currentQuestionIndex = 0;
let score = 0;

function shuffle(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
}

function startQuiz() {
  currentQuestionIndex = 0;
  score = 0;
  shuffle(questions);
  nextButton.innerHTML = "Next";
  showQuestion();
}

function showQuestion() {
  resetState();
  let currentQuestion = questions[currentQuestionIndex];
  let questionNo = currentQuestionIndex + 1;
  questionElement.innerHTML = questionNo + ". " + currentQuestion.question;

  currentQuestion.answers.forEach((answer) => {
    const button = document.createElement("button");
    button.innerHTML = answer.text;
    button.classList.add("btn");
    answerButtons.appendChild(button);
    if (answer.correct) {
      button.dataset.correct = answer.correct;
    }
    button.addEventListener("click", selectAnswer);
  });
}

function resetState() {
  nextButton.style.display = "none";
  while (answerButtons.firstChild) {
    answerButtons.removeChild(answerButtons.firstChild);
  }
}

function selectAnswer(e) {
  const selectedBtn = e.target;
  const isCorrect = selectedBtn.dataset.correct === "true";
  if (isCorrect) {
    selectedBtn.classList.add("correct");
    score++;
  } else {
    selectedBtn.classList.add("incorrect");
  }
  Array.from(answerButtons.children).forEach((button) => {
    if (button.dataset.correct === "true") {
      button.classList.add("correct");
    }
    button.disabled = true;
  });
  nextButton.style.display = "block";
}

function showScore() {
  resetState();
  questionElement.innerHTML = `You scored ${score} out of ${questions.length}!`;
  nextButton.innerHTML = "Restart Test";
  nextButton.style.display = "block";
}

function handleNextButton() {
  currentQuestionIndex++;
  if (currentQuestionIndex < questions.length) {
    showQuestion();
  } else {
    showScore();
  }
}

nextButton.addEventListener("click", () => {
  if (currentQuestionIndex < questions.length) {
    handleNextButton();
  } else {
    startQuiz();
  }
});

startQuiz();
