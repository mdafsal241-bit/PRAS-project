from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# create database and table
def init_db():
    conn = sqlite3.connect("bmi.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bmi_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            weight REAL,
            height REAL,
            bmi REAL,
            status TEXT
        )
    """)

    conn.commit()
    conn.close()

init_db()


@app.route('/calculate_bmi', methods=['POST'])
def calculate_bmi():

    data = request.get_json()

    weight = float(data['weight'])
    height = float(data['height']) / 100

    bmi = weight / (height * height)

    if bmi < 18.5:
        status = "Underweight"
    elif bmi < 25:
        status = "Normal Weight"
    elif bmi < 30:
        status = "Overweight"
    else:
        status = "Obese"

    bmi = round(bmi,1)

    # store in database
    conn = sqlite3.connect("bmi.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO bmi_records (weight, height, bmi, status) VALUES (?, ?, ?, ?)",
        (weight, height*100, bmi, status)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "bmi": bmi,
        "status": status
    })


if __name__ == "__main__":
    app.run(debug=True)