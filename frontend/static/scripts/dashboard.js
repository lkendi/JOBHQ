document.addEventListener("DOMContentLoaded", function () {
    // Initialize charts
    const applicationsChartCtx = document.getElementById('applicationsChart').getContext('2d');
    const interviewsChartCtx = document.getElementById('interviewsChart').getContext('2d');
    const offersChartCtx = document.getElementById('offersChart').getContext('2d');
    const jobsChartCtx = document.getElementById('jobsChart').getContext('2d');

    const applicationsChart = new Chart(applicationsChartCtx, {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'Applications',
                data: [],
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
            labels: [], // to be populated dynamically
            datasets: [{
                label: 'Interviews',
                data: [],
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
            labels: [], // to be populated dynamically
            datasets: [{
                label: 'Offers',
                data: [],
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
        type: 'bar',
        data: {
            labels: [], // to be populated dynamically
            datasets: [{
                label: 'Roles Applied',
                data: [],
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

    // Fetch data and populate charts and metrics
    function fetchDashboardData() {
        fetch('/get_dashboard_data')
            .then(response => response.json())
            .then(data => {
                // Update key metrics
                document.getElementById('applications-submitted').textContent = data.applications_submitted;
                document.getElementById('interviews-scheduled').textContent = data.interviews_scheduled;
                document.getElementById('offers-received').textContent = data.offers_received;
                document.getElementById('jobs-accepted').textContent = data.jobs_accepted;

                // Update charts
                applicationsChart.data.labels = data.applications_overview.labels;
                applicationsChart.data.datasets[0].data = data.applications_overview.data;
                applicationsChart.update();

                interviewsChart.data.labels = data.interviews_overview.labels;
                interviewsChart.data.datasets[0].data = data.interviews_overview.data;
                interviewsChart.update();

                offersChart.data.labels = data.offers_overview.labels;
                offersChart.data.datasets[0].data = data.offers_overview.data;
                offersChart.update();

                jobsChart.data.labels = data.roles_applied.labels;
                jobsChart.data.datasets[0].data = data.roles_applied.data;
                jobsChart.update();

                // Update recent activity
                const recentActivityList = document.getElementById('recent-activity-list');
                recentActivityList.innerHTML = '';
                data.recent_activity.forEach(activity => {
                    const listItem = document.createElement('li');
                    listItem.textContent = activity;
                    recentActivityList.appendChild(listItem);
                });
            });
    }

    // Apply date filters and fetch filtered data
    document.getElementById('apply-filters').addEventListener('click', function () {
        const fromDate = document.getElementById('filter-date-from').value;
        const toDate = document.getElementById('filter-date-to').value;

        fetch(`/get_dashboard_data?from=${fromDate}&to=${toDate}`)
            .then(response => response.json())
            .then(data => {
                // Update key metrics
                document.getElementById('applications-submitted').textContent = data.applications_submitted;
                document.getElementById('interviews-scheduled').textContent = data.interviews_scheduled;
                document.getElementById('offers-received').textContent = data.offers_received;
                document.getElementById('jobs-accepted').textContent = data.jobs_accepted;

                // Update charts
                applicationsChart.data.labels = data.applications_overview.labels;
                applicationsChart.data.datasets[0].data = data.applications_overview.data;
                applicationsChart.update();

                interviewsChart.data.labels = data.interviews_overview.labels;
                interviewsChart.data.datasets[0].data = data.interviews_overview.data;
                interviewsChart.update();

                offersChart.data.labels = data.offers_overview.labels;
                offersChart.data.datasets[0].data = data.offers_overview.data;
                offersChart.update();

                jobsChart.data.labels = data.roles_applied.labels;
                jobsChart.data.datasets[0].data = data.roles_applied.data;
                jobsChart.update();

                // Update recent activity
                const recentActivityList = document.getElementById('recent-activity-list');
                recentActivityList.innerHTML = '';
                data.recent_activity.forEach(activity => {
                    const listItem = document.createElement('li');
                    listItem.textContent = activity;
                    recentActivityList.appendChild(listItem);
                });
            });
    });

    // Initialize FullCalendar
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        events: '/get_calendar_events'
    });
    calendar.render();

    // Initial fetch of dashboard data
    fetchDashboardData();
});
