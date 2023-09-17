const menuBtn = document.querySelector('.menu__btn');
const menuTablet = document.querySelector('.tablet');
const containers = document.querySelectorAll('.container');
const menuBtnClose = document.querySelector('.menu__close__btn');


menuBtn.addEventListener('click', ()=>{
    menuTablet.classList.toggle('menu--open');
    containers.forEach(container => {
        container.classList.toggle('menu--open--container')
    });
    
});

menuBtnClose.addEventListener('click', ()=>{
    menuTablet.classList.remove('menu--open')
    containers.forEach(container => {
        container.classList.remove('menu--open--container')
    });

});


const closeButtons = document.querySelectorAll('.close_messages');

  // Додаємо обробник подій до кожної кнопки
closeButtons.forEach((button) => {
    button.addEventListener('click', () => {
      // Знаходимо батьківський елемент, тобто <div class="messages">
      const messageDiv = button.closest('.messages');

      // Приховуємо повідомлення, змінюючи його стиль
      messageDiv.style.display = 'none';
    });
});