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