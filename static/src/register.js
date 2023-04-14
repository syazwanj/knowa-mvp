// Get input elements
emailInput = document.getElementById("email");
pwInput = document.getElementById("password");
pwCfmInput = document.getElementById("passwordcfm");
regButton = document.getElementById("register-button");

function emailValidator() {
  // Per the RFC5322 standard
  const validRegex =
    /(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])/;
  if (emailInput.value.match(validRegex)) {
    console.log("Match!");
    elementClassAlter(emailInput, true);
    return true;
  } else {
    console.log("Not a match");
    elementClassAlter(emailInput, false);
    return false;
  }
}

function pwValidator() {
  const lengthRegex = /^.{8,}$/;
  const numberRegex = /[0-9]/;
  const lowerRegex = /[a-z]/;
  const upperRegex = /[A-Z]/;

  let lengthValid = pwInput.value.match(lengthRegex);
  let numValid = pwInput.value.match(numberRegex);
  let lowUppValid =
    pwInput.value.match(lowerRegex) && pwInput.value.match(upperRegex);
  elementArr = ["#pw-min-char", "#pw-lower-upper", "#pw-special-number"];

  // Set all to red by default
  for (let elem of elementArr) {
    document.querySelector(elem).classList.remove("text-green-500");
    document.querySelector(elem).classList.add("text-red-500");
  }

  if (lengthValid) {
    document.querySelector("#pw-min-char").classList.add("text-green-500");
    document.querySelector("#pw-min-char").classList.remove("text-red-500");
  }
  if (numValid) {
    document
      .querySelector("#pw-special-number")
      .classList.add("text-green-500");
    document
      .querySelector("#pw-special-number")
      .classList.remove("text-red-500");
  }
  if (lowUppValid) {
    document.querySelector("#pw-lower-upper").classList.add("text-green-500");
    document.querySelector("#pw-lower-upper").classList.remove("text-red-500");
  }
  return lengthValid && numValid && lowUppValid;
}

function pwCfmValidator() {
  if (pwCfmInput.value != pwInput.value) {
    elementClassAlter(pwCfmInput, false);
  } else {
    elementClassAlter(pwCfmInput, true);
  }

  return pwCfmInput.value == pwInput.value;
}

function elementClassAlter(element, valid) {
  if (valid) {
    element.classList.add("bg-gray-50");
    element.classList.add("focus:ring-primary-600");
    element.classList.add("focus:border-primary-600");
    element.classList.remove("bg-red-200");
    element.classList.remove("focus:ring-red-600");
    element.classList.remove("focus:border-red-600");
  } else {
    element.classList.remove("bg-gray-50");
    element.classList.remove("focus:ring-primary-600");
    element.classList.remove("focus:border-primary-600");
    element.classList.add("bg-red-200");
    element.classList.add("focus:ring-red-600");
    element.classList.add("focus:border-red-600");
  }
}

function sendRegister() {
  let allOk = emailValidator() && pwValidator() && pwCfmValidator();
  if (!allOk) {
    console.log("email:" + emailValidator());
    console.log("pw:" + pwValidator());
    console.log("pwCfm:" + pwCfmValidator());
    alert("One or more fields invalid.");
  } else {
    document.querySelector("#registration-form").submit();
  }
}

emailInput.addEventListener("input", emailValidator);
pwInput.addEventListener("input", pwValidator);
pwCfmInput.addEventListener("input", pwCfmValidator);
regButton.addEventListener("click", sendRegister);
