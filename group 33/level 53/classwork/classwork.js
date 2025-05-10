const img = document.getElementById("img")
const next = document.getElementById("next")
const prev = document.getElementById("prev")
let i = 0;
const images = ["./image1.png", "./image2.png",  "./image3.png", "./image4.png", "./image5.png", ]

next.addEventListener("click", function(){
    i++;
    if ( i >= images.length){
        i = 0;
    }
    img.src = images[i]
})

next.addEventListener("click", function(){
    i--;
    if ( i <= -1){
        i = img.length -1;
    }
    img.src = images[i]
})
