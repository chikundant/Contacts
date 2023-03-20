window.onload = function(){
    let contact_button = document.getElementsByClassName('contact')[0]
    let contact_menu = document.getElementsByClassName('contacs_menu')[0]

     contact_button.addEventListener('click', function(){
        contact_menu.classList.toggle('hidden')
     })
}