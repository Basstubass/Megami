
let user_name = document.getElementById("id_username");
user_name.classList.add('un')

let password = document.getElementById('id_password');
password.classList.add('pass')



const textbox = document.getElementById("message")
textbox.addEventListener('click', function(){
    const value = textbox.value
    console.log(value)
})

// const formElements = document.forms.contactForm;
// formElements.text.id = 'id_username';
