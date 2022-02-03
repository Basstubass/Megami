function CheckPassword(confirm){
    // 入力値取得
    var input1 = password.value;
    var input2 = confirm.value;
    // パスワード比較
    if(input1 != input2){
        confirm.setCustomValidity("入力値が一致しません。");
    }else{
        confirm.setCustomValidity('');
    }
}

// クラス付与
 let user_name = document.getElementById("id_username");
 let email = document.getElementById("id_email");
 let password1 = document.getElementById("id_password1");
 let password2 = document.getElementById("id_password2");


 let helptext = document.querySelectorAll(".helptext");
 for(i=0; i < helptext.length; i++){
    helptext[i].remove()
 }
 user_name.classList.add('un')
 email.classList.add('Mail_Adress')
 password1.classList.add('Password')
 password2.classList.add('Confirm_Password')
 helptext.remove()
