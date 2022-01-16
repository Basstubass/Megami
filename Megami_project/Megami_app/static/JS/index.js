const conceptElement = document.querySelector(".concept");
const AbilityElement = document.querySelector(".Ability");

window.addEventListener("load", function() {
    // 実行したい処理
    conceptElement.classList.add("view")
 });

 document.addEventListener("scroll", function(){
    const getElementDistance = AbilityElement.getBoundingClientRect().top + AbilityElement.clientHeight * .6;
    if (window.innerHeight > getElementDistance) {
        AbilityElement.classList.add("view")
    } 
})