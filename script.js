let count = 1;
let computer = [];
let user = [];
let started = false;
let red = new Audio("sounds/red.mp3");
let blue = new Audio("sounds/blue.mp3");
let green = new Audio("sounds/green.mp3");
let yellow = new Audio("sounds/yellow.mp3");
let wrong = new Audio("sounds/wrong.mp3");

let colors = ["red", "blue", "yellow", "green"];
$(document).on("keypress", function () {
  if (!started) {
    nextSequence();
    started = true;
  }
});
function nextSequence() {
  user = [];
  let t = "Level " + count;
  $("h1").text(t);
  count++;
  let x = Math.floor(Math.random() * 4);
  $("#" + colors[x]).addClass("pressed");
  computer.push(colors[x]);
  setTimeout(() => {
    $("#" + colors[x]).removeClass("pressed");
  }, 200);
}
$(".cell").on("click", function () {
  if (!started) return;
  let x = $(this).attr("id");
  user.push(x);

  $("#" + x).addClass("pressed");
  setTimeout(() => {
    $("#" + x).removeClass("pressed");
  }, 200);
  switch (x) {
    case "red":
      red.play();
      break;
    case "blue":
      blue.play();
      break;
    case "green":
      green.play();
      break;
    case "yellow":
      yellow.play();
      break;
  }
  matchWinner(user.length - 1);
});
function matchWinner(x) {
  if (user[x] === computer[x]) {
    if (user.length === computer.length) {
      setTimeout(() => {
        nextSequence();
      }, 300);
    }
  } else {
    user = [];
    computer = [];
    count = 1;
    $("h1").text("You lose, Press any key to restart");
    started = false;
    wrong.play();
    $(".container").addClass("showError");
    setTimeout(() => {
      $(".container").removeClass("showError");
    }, 300);
  }
}
