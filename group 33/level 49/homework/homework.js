const container = document.getElementById('container');

let paragraph = document.createElement('p');
let TextNode1 = document.createTextNodea("hello world")

p.appendChild(TextNode1);
div.appendChild(p);

let button = document.createElement("button");
let TextNode2 = document.createTextNode("click me")
container.removeChild(button);

container.replaceChild(newParagraph, button);