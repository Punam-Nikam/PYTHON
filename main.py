# # // This code is a simple Flask application that defines a REST API for managing tasks. It includes two endpoints: one for retrieving all tasks and another for retrieving a specific task by its ID. The tasks are stored in a list of dictionaries, and the API returns JSON responses. The application runs in debug mode when executed directly.

# from flask import Flask, jsonify

# app = Flask(__name__)

# tasks = [
#     {'id': 1, 'title': 'Learn python framework', 'done': False},
#     {'id': 2, 'title': 'Build a REST API', 'done': True}
# ]

# @app.route('/')
# def home():
#     return "Welcome to Flask API"

# @app.route('/tasks')
# def get_all_tasks():
#     return jsonify({'tasks': tasks})

# @app.route('/tasks/<int:task_id>')
# def get_task(task_id):

#     task = next((task for task in tasks if task['id'] == task_id), None)

#     if task is None:
#         return jsonify({'message': 'Task not found'}), 404

#     return jsonify(task)

# if __name__ == "__main__":
#     app.run(debug=True)