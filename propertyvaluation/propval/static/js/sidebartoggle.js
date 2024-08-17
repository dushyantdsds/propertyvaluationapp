const hamburger = document.querySelector("#toggle-btn");
console.log("connected")
hamburger.addEventListener("click",function(){
    document.querySelector("#sidebar").classList.toggle("expand");
});