from flask import Flask, jsonify

app = Flask(__name__)

# Mock data for employees
employees = [
    {"id": 1, "name": "John Doe", "department": "HR", "joining_date": "2020-01-15", "email": "john@example.com"},
    {"id": 2, "name": "Jane Smith", "department": "IT", "joining_date": "2019-03-22", "email": "jane@example.com"},
    {"id": 2, "name": "Jane Smith", "department": "IT", "joining_date": "2019-03-22", "email": "jane@example.com"},
    {"id": 2, "name": "Jane Smith", "department": "IT", "joining_date": "2019-03-22", "email": "jane@example.com"},
    {"id": 10, "name": "Jane Smith", "department": "IT", "joining_date": "2019-03-22", "email": "jane@example.com"},
    {"id": 11, "name": "Jane Smith", "department": "IT", "joining_date": "2019-03-22", "email": "jane@example.com"}
]

# Define an endpoint to get employee data
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

if __name__ == '__main__':
    app.run(debug=True)

