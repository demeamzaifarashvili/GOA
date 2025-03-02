//const submit = document.getElementById("submit");

//submit.addEventListener('click', function(){
     //const name = document.getElementById("name")
     //const email = document.getElementById("email")
    //const pass = document.getElementById("pass")
//})


const submit = document.getElementById("submit");
const form = document.getElementById("form");

submit.addEventListener('click', function(event){
    event.preventDefault();

    const name = form.nextElementSibling.name
    const email = form.nextElementSibling.email
    const pass = form.nextElementSibling.name.pass

    console.log(name.value)
    console.log(email.value)
    console.log(pass.value)
    
})



