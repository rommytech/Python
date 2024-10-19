document.addEventListener("DOMContentLoaded", function() {
    const button = document.querySelector("button");

    if (button) {
        button.addEventListener("click", function() {
            alert("Sabes que quieres pedirte todos los pasteles!");
            button.style.backgroundColor = button.style.backgroundColor === 'red' ? '#3498db' : 'red';
        });
    } else {
        console.error("Button not found in the DOM!");
    }
});
