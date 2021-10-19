from flask import Blueprint

activities_blueprint = Blueprint('activities_blueprint', __name__)

@activities_blueprint.get("/activities")
def activities():
    print()
    return "tutti gli activities"