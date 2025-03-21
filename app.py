import os
from flask import Flask, jsonify
from flask_cors import CORS  

app = Flask(__name__)
CORS(app)  

# ✅ Root Route (Fix for 404 Error)
@app.route('/')
def home():
    return "Flask Todo App is Running!"

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = [
        {"id": 1, "task": "Buy groceries"},
        {"id": 2, "task": "Read a book"}
    ]
    return jsonify(tasks)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render ke liye correct port setup
    app.run(host="0.0.0.0", port=port, debug=True)
