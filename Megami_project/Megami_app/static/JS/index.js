const conceptElement = document.querySelector(".concept");
const salon_com = document.querySelector(".salon-con");
const user_com = document.querySelector(".user-con");
const stylist_con = document.querySelector(".stylist-con");
const conceptmessage = document.querySelector(".concept-message");
const conect_img = document.querySelector(".conect-img");
const AbilityElement = document.querySelector(".Ability");
const connect_message = document.querySelector(".connect-message");
const using_message = document.querySelector(".using-message");
const Ability_message = document.querySelector(".Ability-message");
const stylist_user = document.querySelector(".stylist-user")
const salon_user = document.querySelector(".salon-user")
const stylist_salon = document.querySelector(".stylist-salon")


window.addEventListener("load", function() {
    // 実行したい処理
    conceptElement.classList.add("show")
    conceptmessage.classList.add("show")
    salon_com.classList.add("show")
    user_com.classList.add("show")
    stylist_con.classList.add("show")
    conect_img.classList.add("show")
    connect_message.classList.add("show")
    using_message.classList.add("show")
 });

 document.addEventListener("scroll", function(){
    const getElementDistance = AbilityElement.getBoundingClientRect().top + AbilityElement.clientHeight * .5;
    if (window.innerHeight > getElementDistance) {
        AbilityElement.classList.add("view")
        Ability_message.classList.add("view")
        stylist_user.classList.add("view")
        salon_user.classList.add("view")
        stylist_salon.classList.add("view")
    } 
});


