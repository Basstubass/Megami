let account_icon = document.getElementById("account_icon");
let account = document.querySelector(".account");
let x_icon = document.getElementById("x_icon");
let x_icon1 = document.getElementById("x_icon1");
let action = document.querySelector(".action");
let stories = document.querySelector(".stories");
let following_data = document.querySelectorAll('.following_data');

const myuser = document.querySelector('.myuser');
my_username = myuser.textContent

account_icon.addEventListener('click', function(){
    account.classList.remove("show");
})
x_icon.addEventListener('click', function(){
    account.classList.add("show");
})
for (let i=0; i < following_data.length; i++){
    following_data[i].addEventListener('click', function(){
        stories.classList.remove("action");
    })
}

x_icon1.addEventListener('click', function(){
    stories.classList.add("action");
})

// 要素を削除



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



$('.LikesIcon-fa-heart').on('click', function(e) {
    article_id = $(this).attr("id");
    $.ajax({
        'url': 'change/',
        'type': 'POST',
        'data': {
            'id': article_id,
        },
        'dataType': 'json'

    })
});

$('.following_data').on('click', function(e){
    followuser_id = $(this).attr("id");
    $('.following_dat').append()
})


    

// $('.following_data').on('click', function(e) {
//     followuser_id = $(this).attr("id");
//     $.ajax({
//         'url': '',
//         'type': 'GET',
//         'data': {
//             'id': followuser_id,
//         },
//         'dataType': 'json'
//     })
// })





///////////////////////////////////
const g_elementDivJoinScreen = document.getElementById( "div_join_screen" );
const g_elementDivChatScreen = document.getElementById( "div_chat_screen" );
const g_elementInputUserName = document.getElementById( "input_username" );
const g_elementInputRoomName = document.getElementById( "input_roomname" );

const g_elementTextUserName = document.getElementById( "text_username" );
const g_elementTextRoomName = document.getElementById( "text_roomname" );

const g_elementInputMessage = document.getElementById( "input_message" );
const g_elementListMessage = document.getElementById( "list_message" );

const get_message_div = document.querySelector('.message_div');
const get_user_div = document.querySelector('.user_div');


// WebSocketオブジェクト
let ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
const g_socket = new WebSocket( ws_scheme + "://" + window.location.host + "/ws/chat/" );

// 「Join」ボタンを押すと呼ばれる関数
function onsubmitButton_JoinChat()
{
    // ユーザー名
    let strInputUserName = g_elementInputUserName.value;
    if( !strInputUserName )
    {
        return;
    }
    g_elementTextUserName.value = strInputUserName;

    // ルーム名
    let strInputRoomName = g_elementInputRoomName.value;
    g_elementTextRoomName.value = strInputRoomName;

    // サーバーに"join"を送信
    g_socket.send( JSON.stringify( { "data_type": "join", "username": strInputUserName, "roomname": strInputRoomName } ) );

    // 画面の切り替え
    g_elementDivJoinScreen.style.display = "none";  // 参加画面の非表示
    g_elementDivChatScreen.style.display = "block";  // チャット画面の表示
}

// 「Leave Chat.」ボタンを押すと呼ばれる関数
function onclickButton_LeaveChat()
{
    // メッセージリストのクリア
    while( g_elementListMessage.firstChild )
    {
        g_elementListMessage.removeChild( g_elementListMessage.firstChild );
    }

    // ユーザー名
    g_elementTextUserName.value = "";

    // サーバーに"leave"を送信
    g_socket.send( JSON.stringify( { "data_type": "leave" } ) );

    // 画面の切り替え
    g_elementDivChatScreen.style.display = "none";  // チャット画面の非表示
    g_elementDivJoinScreen.style.display = "flex";  // 参加画面の表示

    location.reload();
}

// 「Send」ボタンを押したときの処理
function onsubmitButton_Send()
{
    // 送信用テキストHTML要素からメッセージ文字列の取得
    let strMessage = g_elementInputMessage.value;
    if( !strMessage )
    {
        return;
    }

    // WebSocketを通したメッセージの送信
    g_socket.send( JSON.stringify( { "message": strMessage } ) );

    // 送信用テキストHTML要素の中身のクリア
    g_elementInputMessage.value = "";
}

// WebSocketからメッセージ受信時の処理
g_socket.onmessage = ( event ) =>
{
    // 自身がまだ参加していないときは、無視。
    if( !g_elementTextUserName.value )
    {
        return;
    }

    // テキストデータをJSONデータにデコード
    let data = JSON.parse( event.data );

    // メッセージの整形
    //let strMessage = data["message"];
    let strUser = data["username"];
    let strMessage = data["datetime"] + " : " + " " +data["message"];

    // 拡散されたメッセージをメッセージリストに追加
    let element_parson = document.createElement( "div" );
    let elementLi_user = document.createElement( "div" );
    let elementLi_message = document.createElement( "div" );


    elementLi_message.textContent = strMessage;
    elementLi_user.textContent = strUser;

    elementLi_user.className = 'username_div';
    elementLi_user.id='user_message';
    elementLi_message.className = 'message_div';
    elementLi_message.id = 'user_message';

    element_parson.id ='pearents';

    get_user_div.prepend( element_parson );

    const pearents = document.getElementById("pearents");
    pearents.prepend( elementLi_message );
    pearents.prepend(elementLi_user);

};

// WebSocketクローズ時の処理
g_socket.onclose = ( event ) =>
{
    // ウェブページを閉じたとき以外のWebSocketクローズは想定外
    console.error( "Unexpected : Chat socket closed." );
};

///////////////////////////////////
let message_send = document.querySelector('.message_send');
let chat_user_name = document.querySelectorAll('.chat_user_name');
// let chat_room_name = document.querySelectorAll('.chat_room_name');
chat_user_name[1].remove();
// chat_room_name[1].remove();
let user_div_li = document.querySelector('.message_send');




///////////////////////////////////
const Peer = window.Peer;

function OnButtonClick(){
    const local_stream = document.querySelector('.local-stream');
    local_stream.classList.remove("show");

    (async function main(){
        const localVideo = document.getElementById('js-local-stream');
        const joinTrigger = document.getElementById('js-join-trigger');
        const leaveTrigger = document.getElementById('js-leave-trigger');
        const remoteVideos = document.getElementById('js-remote-streams');
        const roomId = document.getElementById('js-room-id');
        const localText = document.getElementById('js-local-text');
        const sendTrigger = document.getElementById('js-send-trigger');
        const messages = document.getElementById('js-messages');
    
        const video_on = document.querySelector('.video_on'); 
        const video_off = document.querySelector('.video_off')
        video_on.classList.add("show");
        video_off.classList.remove("show");
        // video_on.addEventListener('click', ()=>{
        //     screen_on = true;
        // });
            const localStream = await navigator.mediaDevices
            .getUserMedia({
                audio: true,
                video: true,
            })
            .catch(console.error);
    
    
        localVideo.method = true;
        localVideo.srcObject = localStream;
        localVideo.playsInline = true;
        await localVideo.play().catch(console.error);
    
        const peer = (window.peer = new Peer({
            key: '05ba2d45-025e-4dd5-b22a-4e6bc3687491',
            debug: 3,
        }));
    
        joinTrigger.addEventListener('click', () =>{
            if (!peer.open){
                return;
            }
    
            const room = peer.joinRoom(roomId.value, {
                mode: "mesh",
                stream: localStream,
            });
    
            room.once('open', () => {
                messages.textContent += '=== You joined ===\n';
            });
    
            room.on('peerJoin', peerId => {
                messages.textContent += `=== ${peerId} joined ===\n`;
            });
    
            room.on('stream', async stream => {
                const newVideo = document.createElement('video');
                newVideo.srcObject = stream;
                newVideo.playsInline = true;
                newVideo.setAttribute('data-peer-id', stream.peerId);
                remoteVideos.append(newVideo);
                await newVideo.play().catch(console.error);
            });
    
            room.on('data', ({data, src}) => {
                messages.textContent += `${src}: ${data}\n`;
            });
    
            room.on('peerLeave', peerId => {
                const remoteVideo = remoteVideos.querySelector(
                    `[data-peer-id="${peerId}]`
                );
                remoteVideo.srcObject.getTracks().forEach(track => track.stop());
                remoteVideo.srcObject = null;
                remoteVideo.remove();
    
                messages.textContent += ` ${peerId} left \n`;
            });
    
            room.once('close', () => {
                sendTrigger.removeEventListener('click', onClickSend);
                messages.textContent += ' You left \n';
                Array.form(remoteVideos.children).forEach(remoteVideo => {
                    remoteVideo.srcObject.getTracks().forEach(track => track.stop());
                    remoteVideo.srcObject = null;
                    remoteVideo.remove();
                });
            });
    
            sendTrigger.addEventListener('click', onClickSend);
            leaveTrigger.addEventListener('click', ()=> room.close(), { once: true});
    
            function onClickSend() {
                room.send(localText.value);
    
                messages.textContent += `${peer.id}: ${localText.value}\n`;
                localText.value = '';
            }
        });
        peer.on('error', console.error);
    })();
}

function OffButtonClick(){
    setTimeout("location.reload()",2000);
}
    

   

//////////////////////////////////