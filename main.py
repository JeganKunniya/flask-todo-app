# This is the main program to run the flask web application

from flask import Flask

app = Flask(__name__)


@app.route('/<name>')
def echo(name):
    return f'Hello, {name}!'


if __name__ == '__main__':
    app.run(debug=True)  # live mode enabled with debug=True
