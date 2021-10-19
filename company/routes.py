from flask import Blueprint

company_blueprint = Blueprint('company_blueprint', __name__)

@company_blueprint.get("/company")
def company():
    print()
    return "tutti gli company"