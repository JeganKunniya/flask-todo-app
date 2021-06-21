# controller.py

from flask import jsonify, request, Flask

from service import ToDoService, UserService

app = Flask(__name__)


class ToDoController(object):

    @app.route('/health')
    def health():
        return f'Hello there, I am healthy!'

    @app.route('/todo', methods=['POST'])
    def create_todo():
        return jsonify(ToDoService().create(request.get_json()))

    @app.route('/todo', methods=['GET'])
    def get_all_todo():
        return jsonify(ToDoService().get_all_todo_items())

    @app.route('/todo/<id>', methods=['GET'])
    def get_todo(id):
        return jsonify(ToDoService().get_todo_item(id))

    @app.route('/todo/<id>', methods=['DELETE'])
    def delete_todo(id):
        return jsonify(ToDoService().delete(id))

    @app.route('/todo', methods=['PUT'])
    def update_todo():
        return jsonify(ToDoService().update(request.get_json()))


class UserConoller(object):

    @app.route('/user', methods=['POST'])
    def create_user():
        return jsonify(UserService().create(request.get_json()))