// Add event listeners
let leftButtonIndex = 0;
let rightButtonIndex = 1;
const buttonTexts = ["Sign Up", "Enter"];
const placeholderText = ["User ID", "Name"];
const inputTypes = ["user_id", "name"];
const leftButton = document.getElementById("left-button");
const rightButton = document.getElementById("right-button");
rightButton.addEventListener("click", () => {
  rightButtonIndex ^= 1; // ^= is the toggle operator
  leftButtonIndex ^= 1;
  rightButton.value = buttonTexts[rightButtonIndex];
  leftButton.value = buttonTexts[leftButtonIndex];
  document.getElementById("input-box").placeholder =
    placeholderText[rightButtonIndex];
  document
    .getElementById("input-box")
    .setAttribute("name", inputTypes[rightButtonIndex]);
});
