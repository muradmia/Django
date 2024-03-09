// alert("hello World")
// console.log('Hello');


// console.log(document.getElementBytagName("h1"));
var h = document.getElementsByTagName("h1");
// console.log(h);
var i = document.getElementById("num3").style.color = "blue";
document.getElementById("num3").style.removeProperty = ("color");
console.log(num3.innerText);
// document.getElementById("i"
// console.log(i);
var c = document.getElementsByClassName("title");
// console.log(c);

document.getElementById("img")

img.setAttribute("alt","picture")
// console.log(img.getAttribute("alt"));

var hero = document.getElementById("hero")
console.log(hero.innerText);
var input = document.getElementById("input")
// console.log(typeof input);


var parent = document.getElementById("parent").innerHTML;
// console.log(parent)
// console.log(object);
var test = document.getElementsByClassName("right")
// console.log(test[0].childNodes[1].parentNode.parentNode.parentNode.childNodes[1]);
var newdiv = document.getElementById("newdiv")


function createEl(){
    var p = document.createElement("p");
    p.innerText = "Noton ami";
    newdiv.appendChild(p);
}
// createEl();

document.getElementById("btn").addEventListener( "click", function (e){
    // createEl();
    var input = document.getElementById("input").value;
    console.log(input);
});

// document.getElementById("input").addEventListener("blur", function (e){
//     console.log(e.target.value);
// })

function nter(e){
    console.log("Hello");
}

function enter(e){
    createEl();
}


function clickhandle(e){
    var input = document.getElementById("input").value;
    console.log(input);
}





