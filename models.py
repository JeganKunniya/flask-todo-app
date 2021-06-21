# Schema

import sqlite3


class Schema(object):
    def __init__(self):
        """
        Constructor to create the database schema using Sqlite database for the ToDo application.
        This creates the necessary tables if not already exists
        """
        self.connection = sqlite3.connect('todo.db')
        self.create_user_table()
        self.create_todo_table()

    def create_user_table(self):
        """
        Creates the table in the Sqlite database for the user.

        :return: None
        """
        create_user_schema_query = """
        CREATE TABLE IF NOT EXISTS "User" (
            Id INTEGER PRIMARY KEY,
            Name TEXT,
            Email TEXT
        )
        """
        self.connection.execute(create_user_schema_query)

    def create_todo_table(self):
        """
        Creates the table in the Sqlite database for the ToDo item.

        :return: None
        """
        create_todo_schema_query = """
        CREATE TABLE IF NOT EXISTS "ToDo" (
            Id INTEGER PRIMARY KEY,
            Title TEXT,
            Description TEXT,
            CreatedOn DATE DEFAULT CURRENT_DATE,
            DueDate Date,
            IsDeleted BOOLEAN,
            IsCompleted BOOLEAN,
            CreatedBy INTEGER FOREIGNKEY REFERENCES USER(Id)
        )
        """
        self.connection.execute(create_todo_schema_query)


# ToDoModel

class ToDoModel(object):
    """
    This class handles all the CRUD operations of ToDo data store.
    """
    TABLENAME = "TODO"

    def __init__(self):
        self.connection = sqlite3.connect("todo.db")
        self.connection.row_factory = sqlite3.Row

    def __del__(self):
        self.connection.commit()
        self.connection.close()

    def create_todo_item(self, title, description, created_by):
        query = f"Insert into {self.TABLENAME}(Title, Description, CreatedBy) values ('{title}', '{description}', " \
                f"{created_by})"
        self.connection.execute(query)

        return self.get_all_todo_items()

    def get_todo_item(self, id):
        query = f'Select * from {self.TABLENAME} where Id={id}'
        self.connection.execute(query)
        return self.get_all_todo_items()

    def get_all_todo_items(self, id=None):
        query = f'Select * from {self.TABLENAME}'
        if id is not None:
            query += f' where Id = {id}'
        result = self.connection.execute(query).fetchall()

        response = [{column: row[i]
                     for i, column in enumerate(result[0].keys())}
                    for row in result]
        return response

    def update_todo_item(self, id, title, description):
        query = f"Update {self.TABLENAME} Set Title='{title}', Description='{description}' where Id = {id}"

        self.connection.execute(query)
        return self.get_all_todo_items()

    def delete_todo_item(self, id):
        query = f"Update {self.TABLENAME} set IsDeleted=1 where Id = {id}"

        self.connection.execute(query)
        return self.get_all_todo_items()


# UserModel

class UserModel(object):
    """
    This class handles all the CRUD operations of the user
    """
    TABLENAME = 'USER'

    def __init__(self):
        self.connection = sqlite3.connect("todo.db")
        self.connection.row_factory = sqlite3.Row

    def __del__(self):
        self.connection.commit()
        self.connection.close()

    def create_user(self, name, email):
        query = f"Insert into {self.TABLENAME}(Name, Email) values ('{name}', '{email}')"

        user_id = self.connection.execute(query).lastrowid

        return f'User [Id={user_id}] created successfully'

    def update_user(self, id, name, email):
        query = f"Update {self.TABLENAME} set "
        if name is not None:
            query += f" name='{name}'"
        if email is not None:
            query += f", email='{email}' "
        query += f"where id = {id}"

        total_rows_updated = self.connection.execute(query).rowcount

        return f'Update impacted {total_rows_updated} row(s)'

    def delete_user(self, id):
        query = f"Delete from {self.TABLENAME} where Id={id}"

        no_of_rows_deleted = self.connection.execute(query).rowcount

        return f"Deleted {no_of_rows_deleted} row(s) matching to user identifier {id}"
