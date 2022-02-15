from flask import Blueprint
from app.controllers import vaccine_controller

bp_vaccine = Blueprint("bp_vaccine", __name__, url_prefix="/vaccinations")

bp_vaccine.post("")(vaccine_controller.insert_vaccine)
bp_vaccine.get("")(vaccine_controller.show_list_vaccinations)