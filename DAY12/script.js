let ageElement = document.getElementById("age");
let currentAge = parseInt(ageElement.innerText); 

function plus() {
    currentAge++;
    ageElement.innerText = currentAge;
    console.log("Age incremented to:", currentAge);
}

function minus() {
    if (currentAge > 0) { 
        currentAge--;
        ageElement.innerText = currentAge;
        console.log("Age decremented to:", currentAge); 
    } else {
        console.log("Age cannot be less than 0."); 
    }
}