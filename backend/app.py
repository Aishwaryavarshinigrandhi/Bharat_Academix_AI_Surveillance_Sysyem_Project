from flask import Flask, request, jsonify, render_template
from database import init_db, insert_alert, get_alerts
import os

app = Flask(__name__,
            template_folder="../templates",
            static_folder="../static")

init_db()

@app.route('/')
def dashboard():
    alerts = get_alerts()
    return render_template("dashboard.html", alerts=alerts)

@app.route('/alert', methods=['POST'])
def receive_alert():
    data = request.json
    insert_alert(data)
    return jsonify({"status": "Alert received"})

@app.route('/alerts')
def fetch_alerts():
    alerts = get_alerts()
    return jsonify(alerts)

if __name__ == "__main__":
    os.makedirs("../alerts", exist_ok=True)
    app.run(debug=True)