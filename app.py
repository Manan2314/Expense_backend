from flask import Flask, request, jsonify
from flask_cors import CORS
import csv

app = Flask(__name__)
CORS(app)

@app.route('/add-expense', methods=['POST'])
def add_expense():
    data = request.get_json()
    with open("expenses.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([data["date"], data["email"], data["amount"], data["category"]])
    return jsonify({"status": "success", "message": "Expense saved!"})

@app.route('/')
def home():
    return "Backend Running"
