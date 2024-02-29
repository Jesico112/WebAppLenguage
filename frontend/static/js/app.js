// frontend/static/js/app.js
document.getElementById("botonEnviar").addEventListener("click", function() {
    fetch("/texto/")
        .then(response => response.json())
        .then(data => {
            alert("Texto recibido: " + data.contenido);
        })
        .catch(error => {
            console.error("Error al recuperar el texto:", error);
            alert("Error al recuperar el texto.");
        });
});
