let old_password = document.getElementById("id_old_password");
 let new_password1 = document.getElementById("id_new_password1");
 let new_password2 = document.getElementById("id_new_password2");


 let helptext = document.querySelectorAll(".helptext");
 for(i=0; i < helptext.length; i++){
    helptext[i].remove()
 }
 old_password.classList.add('old_password')
 new_password1.classList.add('Password')
 new_password2.classList.add('Confirm_Password')
 helptext.remove()
