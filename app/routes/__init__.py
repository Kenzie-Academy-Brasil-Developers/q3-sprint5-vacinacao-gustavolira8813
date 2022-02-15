from flask import Blueprint, Flask
from app.routes.vaccine_blueprint import bp_vaccine

bp_api = Blueprint("bp_api", __name__, url_prefix="/api")

def init_app(app: Flask):
    bp_api.register_blueprint(bp_vaccine)
    app.register_blueprint(bp_api)