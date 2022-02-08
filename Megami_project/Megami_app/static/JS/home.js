let account_icon = document.getElementById("account_icon");
let account = document.querySelector(".account");
let x_icon = document.getElementById("x_icon");
account_icon.addEventListener('click', function(){
    account.classList.remove("show");
})
x_icon.addEventListener('click', function(){
    account.classList.add("show");
})



// テスト

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

    /** jQueryの処理 */
    $('.LikesIcon').on('click', function() {
        let $btn = $(this);
        // Likeボタンがonクラス持っていたら
        if ($btn.hasClass('on')) {
          $btn.removeClass('on');
          $btn.children("i").attr('class', 'far fa-heart LikesIcon-fa-heart');  
        } else {
      
          $btn.addClass('on');
      
          // ポイントは2つ！！
          // ①アイコンを変更する
          // far fa-heart（白抜きアイコン）
          // ⇒ fas fa-heart（背景色つきアイコン）
          // ②アニメーション+アイコン色変更用のheartクラスを付与する
      
          $btn.children("i").attr('class', 'fas fa-heart LikesIcon-fa-heart heart');
      
        }
  });



$('.add_good').on('click', function(e) {
    article_id = $(this).attr("id");
    $.ajax({
        'url': 'change/',
        'type': 'POST',
        'data': {
            'id': article_id,
        },
        'dataType': 'json'

    }).done( response => {
        const response_id = response.id;
        const good_count = response.good_count;
        const element = '#good-count-' + response_id;
        $(element).text(good_count);
    });

});


