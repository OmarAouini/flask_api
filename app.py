from flask import Flask
from markupsafe import escape
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    print()
    return "index"

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<string:username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User: {escape(username)}'