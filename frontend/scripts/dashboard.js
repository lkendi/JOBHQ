document.addEventListener("DOMContentLoaded", function () {
    const sidebar = document.getElementById("sidebar");
    const hamburger = document.getElementById("hamburger");

    hamburger.addEventListener("click", function () {
        sidebar.classList.toggle("active");
    });

    // Initialize charts
    const applicationsChartCtx = document.getElementById('applicationsChart').getContext('2d');
    const interviewsChartCtx = document.getElementById('interviewsChart').getContext('2d');
    const offersChartCtx = document.getElementById('offersChart').getContext('2d');
    const jobsChartCtx = document.getElementById('jobsChart').getContext('2d');

    const applicationsChart = new Chart(applicationsChartCtx, {
        type: 'line',
        data: {
            labels: ['January', 'February', 'March', 'April', 'May'],
            datasets: [{
                label: 'Applications',
                data: [12, 19, 3, 5, 2],
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    const interviewsChart = new Chart(interviewsChartCtx, {
        type: 'line',
        data: {
            labels: ['January', 'February', 'March', 'April', 'May'],
            datasets: [{
                label: 'Interviews',
                data: [2, 3, 1, 4, 2],
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    const offersChart = new Chart(offersChartCtx, {
        type: 'line',
        data: {
            labels: ['January', 'February', 'March', 'April', 'May'],
            datasets: [{
                label: 'Offers',
                data: [1, 2, 1, 1, 0],
                backgroundColor: 'rgba(255, 206, 86, 0.2)',
                borderColor: 'rgba(255, 206, 86, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    const jobsChart = new Chart(jobsChartCtx, {
        type: 'horizontalBar',
        data: {
            labels: ['Software Engineer', 'Data Scientist', 'Product Manager', 'Designer'],
            datasets: [{
                label: 'Roles Applied',
                data: [5, 3, 2, 1],
                backgroundColor: 'rgba(153, 102, 255, 0.2)',
                borderColor: 'rgba(153, 102, 255, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                x: {
                    beginAtZero: true
                }
            }
        }
    });

    // Initialize calendar
    const calendarEl = document.getElementById('calendar');
    const calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        events: [
            { title: 'Interview with Google', date: '2023-07-01' },
            { title: 'Apply to Facebook', date: '2023-07-02' }
        ]
    });
    calendar.render();

    // Filters
    document.getElementById('apply-filters').addEventListener('click', function () {
        const fromDate = document.getElementById('filter-date-from').value;
        const toDate = document.getElementById('filter-date-to').value;
        console.log('Filters applied from', fromDate, 'to', toDate);
        // Update charts data based on filters
        // Add your filtering logic here
    });
});
