document.querySelector('.login-form').addEventListener('submit', function(e) {
    e.preventDefault(); // Previene el envío del formulario
    document.querySelector('.fa-hourglass-start').style.display = 'inline-block'; // Muestra el icono de reloj de arena
    setTimeout(function() {
        e.target.submit(); // Envía el formulario después de 3 segundos
    }, 3000);
});
