const trafficCtx = document.getElementById('trafficChart').getContext('2d');
const threatCtx = document.getElementById('threatChart').getContext('2d');

let labels = [];
let normalData = [];
let attackData = [];

const trafficChart = new Chart(trafficCtx, {
    type: 'line',
    data: {
        labels: labels,
        datasets: [
            {
                label: 'Normal',
                data: normalData,
                borderColor: 'green',
                fill: false
            },
            {
                label: 'Attack',
                data: attackData,
                borderColor: 'red',
                fill: false
            }
        ]
    }
});

const threatChart = new Chart(threatCtx, {
    type: 'pie',
    data: {
        labels: ['Normal', 'Attack'],
        datasets: [{
            data: [0, 0],
            backgroundColor: ['blue', 'pink']
        }]
    }
});

function loadData() {
    fetch('/api/live_data')
        .then(response => response.json())
        .then(data => {

            if (!data) return;

            const time = new Date().toLocaleTimeString();

            labels.push(time);
            normalData.push(data.normal || 0);
            attackData.push(data.attack || 0);

            if (labels.length > 10) {
                labels.shift();
                normalData.shift();
                attackData.shift();
            }

            trafficChart.update();

            threatChart.data.datasets[0].data = [
                data.normal || 0,
                data.attack || 0
            ];
            threatChart.update();

            // Update Logs
            const tableBody = document.getElementById("logTableBody");
            tableBody.innerHTML = "";

            if (data.logs && Array.isArray(data.logs)) {
                data.logs.forEach(log => {
                    tableBody.innerHTML += `
                        <tr>
                            <td>${log.time}</td>
                            <td>${log.ip}</td>
                            <td>${log.status}</td>
                            <td>${log.confidence}%</td>
                        </tr>
                    `;
                });
            }

        })
        .catch(error => console.log(error));
}

setInterval(loadData, 2000);