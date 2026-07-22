from flask import Flask, render_template, jsonify
import random
from datetime import datetime

app = Flask(__name__)

# -----------------------------------
# SECURITY DASHBOARD (SEPARATE PAGE)
# -----------------------------------

@app.route("/security_dashboard")
def security_dashboard():
    return render_template("security_dashboard.html")


@app.route("/api/dashboard_data")
def dashboard_data():

    supervised = []
    unsupervised = []
    attack_count = 0

    for i in range(10):
        prediction = random.choice(["Normal", "Attack"])
        confidence = random.randint(60, 100)

        if prediction == "Attack":
            attack_count += 1

        supervised.append({
            "id": i+1,
            "time": datetime.now().strftime("%H:%M:%S"),
            "features": f"{random.randint(10,100)}, {random.randint(10,100)}",
            "prediction": prediction,
            "confidence": confidence
        })

    for i in range(10):
        unsupervised.append({
            "id": i+1,
            "time": datetime.now().strftime("%H:%M:%S"),
            "features": f"{random.randint(10,100)}, {random.randint(10,100)}",
            "cluster": random.randint(0, 2)
        })

    return jsonify({
        "supervised": supervised,
        "unsupervised": unsupervised,
        "active_threats": attack_count,
        "ml_confidence": random.randint(40, 95),
        "uptime": random.randint(80, 100)
    })


# -----------------------------------
# REALTIME MONITORING (SEPARATE PAGE)
# -----------------------------------

@app.route("/realtime")
def realtime():
    return render_template("realtime.html")


@app.route("/api/realtime_data")
def realtime_data():

    normal = random.randint(50, 100)
    attack = random.randint(0, 30)

    logs = []

    for i in range(6):
        status = random.choice(["Normal", "Attack"])

        logs.append({
            "time": datetime.now().strftime("%H:%M:%S"),
            "ip": f"192.168.1.{random.randint(1,255)}",
            "status": status,
            "confidence": random.randint(60, 100)
        })

    return jsonify({
        "normal": normal,
        "attack": attack,
        "logs": logs
    })


if __name__ == "__main__":
    app.run(debug=True)