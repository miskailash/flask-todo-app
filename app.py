from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for the app

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = [
        {"id": 1, "task": "Buy groceries"},
        {"id": 2, "task": "Read a book"}
    ]
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(debug=True)
