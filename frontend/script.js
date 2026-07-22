function detect() {
    const features = document.getElementById("features").value;

    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ features: features })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("output").innerText =
            JSON.stringify(data, null, 4);

        loadLogs();
    })
    .catch(err => {
        alert("Backend not connected");
        console.error(err);
    });
}

function loadLogs() {
    fetch("http://127.0.0.1:5000/logs")
    .then(res => res.json())
    .then(data => {
        const table = document.getElementById("logTable");
        table.innerHTML = "";

        data.forEach(log => {
            table.innerHTML += `
                <tr>
                    <td>${log.id}</td>
                    <td>${log.features}</td>
                    <td>${log.rf_result}</td>
                    <td>-</td>
                </tr>
            `;
        });
    });
}
