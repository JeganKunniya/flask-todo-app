Hello there,

Welcome to my todo application built using Python and Flask.

This app has been built as part of the learning curriculum of 'Python to Projects' 
offered and taught virtually by **@bhavaniravi_** and **@TheLearningDev**.

## ToDo App Insights

### Core Requirements
The ToDo application provides the following basic functionalities,
1. Create a ToDo item
2. Read the available ToDo item(s)
3. Update a ToDo item
4. Delete a ToDo item

**Note:**
We will employ the soft-delete mechanism for deleting a ToDo item in this app.

### Store information

Let's use a relation database for the app, that has the following database elements 
to perform CRUD operations. 

Table Name: ToDo_Item
- Id: unique number of the ToDo item [Primary Key]
- Title: the short description of the todo [Text]
- Description: the addition information about the todo [Text]
- CreatedOn: the date in which the todo is created [Date]
- DueDate: the date by when the todo has to be completed [Date]
- IsDeleted: the flag that indicates if the todo is deleted [Boolean]
- IsCompleted: the flag that indicates if the todo is completed [Boolean]
- CreatedBy: unique number of the user created the ToDo item [Foreign Key]

Let's add a user who is creating these ToDo items and link the user with the ToDo

Table Name: User
- Id: unique number that identifies the user [Primary Key]
- Name: the name of the user [Text]
- Email: the email id of the user [Text]

Wish me luck!