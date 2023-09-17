const passwordField = document.getElementById('password');
const togglePassword = document.getElementById('togglePassword');

togglePassword.addEventListener('click', () => {
  if (passwordField.type === 'password') {
    passwordField.type = 'text'; // Показати пароль
  } else {
    passwordField.type = 'password'; // Приховати пароль
  }
});
