# service.py
from models import ToDoModel, UserModel


class ToDoService(object):

    def __init__(self):
        self.model = ToDoModel()

    def create(self, params):
        return self.model.create_todo_item(params['Title'], params['Description'], params['CreatedBy'])

    def get_all_todo_items(self):
        return self.model.get_all_todo_items()

    def get_todo_item(self, id):
        return self.model.get_all_todo_items(id)

    def delete(self, id):
        return self.model.delete_todo_item(id)

    def update(self, params):
        return self.model.update_todo_item(params['Id'], params['Title'], params['Description'])


class UserService(object):

    def __init__(self):
        self.model = UserModel()

    def create(self, params):
        return self.model.create_user(params['Name'], params['Email'])