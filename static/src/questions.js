// For testing
let correctAns = "1";

function markCorrectIncorrect(element, allOptions) {
  // Highlight red if wrong answer
  if (element.dataset.value != correctAns) {
    console.log(element.classList);
    element.classList.add("bg-red-400");
  }

  for (let opt of allOptions) {
    opt.classList.remove("hover:bg-gray-100");
    if (opt.dataset.value == correctAns) {
      opt.classList.add("bg-green-400");
    }
  }

  // document.getElementById("solutions-button").classList.remove("hidden");
}

const options = document.getElementsByClassName("question-option");
for (let opt of options) {
  opt.addEventListener("click", () => markCorrectIncorrect(opt, options));
}

// Fill in the boxes at the bottom depending on question difficulty
for (i = 1; i < 11; i++) {
  document.getElementById(`footer-box-${i}`).style.background =
    "rgb(96 165 250)";
  document.getElementById(`footer-box-${i}`).classList.add("border-2");
}
