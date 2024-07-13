document.addEventListener("DOMContentLoaded", function () {
    const sidebar = document.getElementById("sidebar");
    const hamburger = document.getElementById("hamburger");
    const gridViewBtn = document.getElementById("grid-view-btn");
    const kanbanViewBtn = document.getElementById("kanban-view-btn");
    const gridView = document.getElementById("grid-view");
    const kanbanView = document.getElementById("kanban-view");
    const popup = document.getElementById("popup");
    const jobDetails = document.getElementById("job-details");
    const closePopup = document.querySelector(".popup .close");

    hamburger.addEventListener("click", function () {
        sidebar.classList.toggle("active");
    });

    gridViewBtn.addEventListener("click", function () {
        gridView.classList.add("active");
        kanbanView.classList.remove("active");
    });

    kanbanViewBtn.addEventListener("click", function () {
        kanbanView.classList.add("active");
        gridView.classList.remove("active");
    });

    document.querySelectorAll(".kanban-card").forEach(card => {
        card.addEventListener("click", function () {
            jobDetails.textContent = this.getAttribute("data-details");
            popup.style.display = "flex";
        });
    });

    closePopup.addEventListener("click", function () {
        popup.style.display = "none";
    });

    window.addEventListener("click", function (event) {
        if (event.target === popup) {
            popup.style.display = "none";
        }
    });
});
