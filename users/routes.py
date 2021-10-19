from flask import Blueprint

users_blueprint = Blueprint('users_blueprint', __name__)

@users_blueprint.get("/users")
def users():
    print()
    return "tutti gli users"
