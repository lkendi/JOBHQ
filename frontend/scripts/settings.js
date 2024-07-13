document.addEventListener("DOMContentLoaded", function () {
    const sidebar = document.getElementById("sidebar");
    const hamburger = document.getElementById("hamburger");

    hamburger.addEventListener("click", function () {
        sidebar.classList.toggle("active");
    });
});
