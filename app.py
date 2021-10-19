from flask import Flask
from markupsafe import escape
from flask import request
from users.routes import users_blueprint
from company.routes import company_blueprint
from activities.routes import activities_blueprint

app = Flask(__name__)
app.register_blueprint(users_blueprint)
app.register_blueprint(company_blueprint)
app.register_blueprint(activities_blueprint)

@app.get("/")
def hello_world():
    print()
    return "index"

@app.get('/hello')
def hello():
    return 'Hello, World'

@app.get('/user/<string:username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User: {escape(username)}'

#user routes
