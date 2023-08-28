from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Task 1"},
    {"id": 2, "title": "Task 2"}
]

@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tasks": tasks})

if __name__ == "__main__":
    app.run(debug=True)