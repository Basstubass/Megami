// $(function() {
    
//     });
    window.addEventListener('DOMContentLoaded', function(){
        /** jQueryの処理 */
        $( "#button" ).click(function() {
            $( "#button" ).addClass( "onclic", 250, validate);
          });
        
          function validate() {
            setTimeout(function() {
              $( "#button" ).removeClass( "onclic" );
              $( "#button" ).addClass( "validate", 450, callback );
            }, 2250 );
          }
            function callback() {
              setTimeout(function() {
                $( "#button" ).removeClass( "validate" );
              }, 1250 );
            }
      });

    let title = document.getElementById("id_title");
    title.classList.add('id_title')

    let content = document.getElementById("id_content");
    content.classList.add('id_content')