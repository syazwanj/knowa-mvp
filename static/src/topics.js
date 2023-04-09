function gotoTopic(element) {
  console.log(element.dataset.topic);
}

const topicCards = document.getElementsByClassName("card");
for (let card of topicCards) {
  card.addEventListener("click", () => gotoTopic(card));
}
