
const div = document.getElementById("div");

let x = 0;
let y = 0;
let direction = "right";

const interval = setInterval(() => {
  if (direction === "right") {
    x += 5;
    if (x >= 400) direction = "down";
  } else if (direction === "down") {
    y += 5;
    if (y >= 400) direction = "left";
  } else if (direction === "left") {
    x -= 5;
    if (x <= 0) direction = "up";
  } else if (direction === "up") {
    y -= 5;
    if (y <= 0) direction = "right"; 
  }

  div.style.left = `${x}px`;
  div.style.top = `${y}px`;
}, 20);