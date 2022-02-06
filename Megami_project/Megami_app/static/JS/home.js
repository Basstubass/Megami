let account_icon = document.getElementById("account_icon");
let account = document.querySelector(".account");
let x_icon = document.getElementById("x_icon");
account_icon.addEventListener('click', function(){
    account.classList.remove("show");
})
x_icon.addEventListener('click', function(){
    account.classList.add("show");
})