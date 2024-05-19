// Ожидание загрузки DOM
document.addEventListener('DOMContentLoaded', function() {
    // Поиск кнопки регистрации по ее идентификатору
    var registrationButton = document.getElementById('registrationButton');

    // Добавление обработчика события click для кнопки регистрации
    registrationButton.addEventListener('click', function() {
        // Перенаправление на страницу регистрации
        window.location.href = 'http://127.0.0.1:8000/registration/';
    });
});
