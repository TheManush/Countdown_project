from flask import Flask, render_template, jsonify
from zoneinfo import ZoneInfo
from datetime import datetime

app = Flask(__name__)

timezone = ZoneInfo("Asia/Dhaka")

target_date = datetime(2030, 5, 29, 23, 59, 59, tzinfo=timezone)
#year, month, day, hour, minute, second

@app.route('/')
def home():
    current_time = datetime.now(tz=timezone)
    difference = target_date - current_time
    total_seconds =max(0, int(difference.total_seconds()))
    days = total_seconds // (24 * 3600)
    hours = (total_seconds % (24 * 3600)) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    return render_template(
        "index.html", days=days, hours=hours, minutes=minutes, seconds=seconds       
    )


@app.route('/cntdown-data')
def cntdown_data():
    current_time = datetime.now(tz=timezone)
    difference = target_date - current_time
    total_seconds =max(0, int(difference.total_seconds()))
    days = total_seconds // (24 * 3600)
    hours = (total_seconds % (24 * 3600)) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    return jsonify({
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds
    })

if __name__ == "__main__":
    app.run(debug=True)