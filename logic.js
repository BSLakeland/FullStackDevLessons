function showText(){
    document.getElementById("hiddenText").style.display = "block";
}
function showImage(){
    document.getElementById("hiddenImage").style.display = "block";
}

function sayHello() {
    let name = document.getElementById("nameInput").value;
    if (name == "Tom"){
        greeting = "Fuck off, Tom."
    }
    else {
        greeting = "Hello, " + name + "!"
    }
    alert(greeting);
    console.log("Hey ho!")
}