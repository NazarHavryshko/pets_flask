const passwordField1 = document.getElementById('password1');
const togglePassword1 = document.getElementById('togglePassword1');

togglePassword1.addEventListener('click', () => {
  if (passwordField1.type === 'password') {
    passwordField1.type = 'text'; // Показати пароль
  } else {
    passwordField1.type = 'password'; // Приховати пароль
  }
});


const passwordField2 = document.getElementById('password2');
const togglePassword2 = document.getElementById('togglePassword2');

togglePassword2.addEventListener('click', () => {
  if (passwordField2.type === 'password') {
    passwordField2.type = 'text'; // Показати пароль
  } else {
    passwordField2.type = 'password'; // Приховати пароль
  }
});