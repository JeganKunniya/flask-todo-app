# This is the main program to run the flask web application

from controller import app
from models import Schema

if __name__ == '__main__':
    Schema()
    app.run(debug=True)  # live mode enabled with debug=True
