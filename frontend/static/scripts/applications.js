document.addEventListener("DOMContentLoaded", function () {
    // View toggle buttons
    const gridViewBtn = document.getElementById("grid-view-btn");
    const kanbanViewBtn = document.getElementById("kanban-view-btn");
    const gridView = document.getElementById("grid-view");
    const kanbanView = document.getElementById("kanban-view");
    gridViewBtn.addEventListener("click", function () {
        gridView.classList.add("active");
        kanbanView.classList.remove("active");
    });
    kanbanViewBtn.addEventListener("click", function () {
        kanbanView.classList.add("active");
        gridView.classList.remove("active");
    });

    // Popup elements
    const popup = document.getElementById("popup");
    const closePopupButtons = document.querySelectorAll('.popup .close');
    closePopupButtons.forEach(button => {
        button.addEventListener('click', function () {
            button.closest('.popup').style.display = 'none';
        });
    });
    window.addEventListener('click', function (event) {
        if (event.target.classList.contains('popup')) {
            event.target.style.display = 'none';
        }
    });

    // New application popup
    const addApplicationBtn = document.getElementById('add-application-btn');
    const addApplicationPopup = document.getElementById('add-application-popup');
    const addApplicationCloseBtn = document.getElementById('add-application-close');
    addApplicationBtn.addEventListener('click', function () {
        addApplicationPopup.style.display = 'flex';
    });
    addApplicationCloseBtn.addEventListener('click', function () {
        addApplicationPopup.style.display = 'none';
    });

    // Edit application popup
    const editIcons = document.querySelectorAll('.edit-icon');
    const kanbanCards = document.querySelectorAll('.kanban-card');
    const showPopup = (applicationId) => {
        fetch(`/get_application/${applicationId}`)
            .then(response => response.json())
            .then(data => {
                document.getElementById('edit-application-id').value = data.id;
                document.getElementById('edit-job-title').value = data.job_title;
                document.getElementById('edit-company-name').value = data.company_name;
                document.getElementById('edit-application-date').value = data.application_date;
                document.getElementById('edit-status').value = data.status;
                popup.style.display = 'flex';
            });
    };
    editIcons.forEach(icon => {
        icon.addEventListener('click', function() {
            const applicationId = this.getAttribute('data-id');
            showPopup(applicationId);
        });
    });
    kanbanCards.forEach(card => {
        card.addEventListener('click', function() {
            const applicationId = this.getAttribute('data-id');
            showPopup(applicationId);
        });
    });

    // Save application
    const saveBtn = document.getElementById('save-button');
    saveBtn.addEventListener('click', function() {
        const form = document.getElementById('edit-application-form');
        const formData = new FormData(form);
        fetch('/update_application', {
            method: 'POST',
            body: formData
        }).then(response => response.json())
          .then(data => {
              if (data.status === 'success') {
                  location.reload();
              } else {
                  alert('Failed to update application');
              }
          });
    });

    // Drag and drop functionality for Kanban cards
    const columns = document.querySelectorAll('.kanban-column');
    columns.forEach(column => {
        column.addEventListener('dragover', function(e) {
            e.preventDefault();
            const afterElement = getDragAfterElement(column, e.clientY);
            const draggable = document.querySelector('.dragging');
            if (afterElement == null) {
                column.appendChild(draggable);
            } else {
                column.insertBefore(draggable, afterElement);
            }
        });
        column.addEventListener('drop', function() {
            const applicationId = document.querySelector('.dragging').getAttribute('data-id');
            const newStatus = column.getAttribute('data-status');
            const formData = new FormData();
            formData.append('application_id', applicationId);
            formData.append('status', newStatus);
            fetch('/update_status', {
                method: 'POST',
                body: formData
            }).then(response => response.json())
              .then(data => {
                  if (data.status !== 'success') {
                      alert('Failed to update status');
                  } else {
                      location.reload();
                  }
              });
        });
    });

    function getDragAfterElement(container, y) {
        const draggableElements = [...container.querySelectorAll('.kanban-card:not(.dragging)')];
        return draggableElements.reduce((closest, child) => {
            const box = child.getBoundingClientRect();
            const offset = y - box.top - box.height / 2;
            if (offset < 0 && offset > closest.offset) {
                return { offset: offset, element: child };
            } else {
                return closest;
            }
        }, { offset: Number.NEGATIVE_INFINITY }).element;
    }

    kanbanCards.forEach(card => {
        card.addEventListener('dragstart', () => {
            card.classList.add('dragging');
        });
        card.addEventListener('dragend', () => {
            card.classList.remove('dragging');
        });
    });

});

    $(document).ready(function() {
        var isKanbanView = false;

        $('#applications-table').DataTable();

        $('#add-application-btn').on('click', function() {
            $('#application-modal').show();
        });

        $('.close').on('click', function() {
            $('#application-modal').hide();
        });

        $('#status').on('change', function() {
            var status = $(this).val();
            if (status === 'Interview' || status === 'Offer') {
                $('#additional-info').show();
            } else {
                $('#additional-info').hide();
            }
        });

        $('#application-form').on('submit', function(event) {
            event.preventDefault();

            var formData = $(this).serializeArray();
            var application = {};
            formData.forEach(function(item) {
                application[item.name] = item.value;
            });

            application.status = application.status.replace(/\b\w/g, l => l.toUpperCase());
            application.applicationDate = new Date(application.applicationDate);

            if (application.applicationDate > new Date()) {
                alert("Application date cannot be after the current date.");
                return;
            }

            if (isKanbanView) {
                addApplicationToKanban(application);
            } else {
                addApplicationToTable(application);
            }

            $('#application-modal').hide();
            $('#application-form')[0].reset();
            $('#additional-info').hide();
        });

        function addApplicationToTable(application) {
            var table = $('#applications-table').DataTable();
            table.row.add([
                application.company,
                application.position,
                application.status,
                application.applicationDate.toDateString(),
                application.notes
            ]).draw(false);
        }

        function addApplicationToKanban(application) {
            // Implement Kanban addition logic here
        }

        // Kanban view toggling logic
        $('#toggle-kanban-view').on('click', function() {
            isKanbanView = !isKanbanView;
            $('#kanban-view').toggle();
            $('#applications-view').toggle();
        });
});
