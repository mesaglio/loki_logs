from flask import Blueprint
from utils.decorators import log_enpoint_information

ping_blueprint = Blueprint("ping", __name__)


@ping_blueprint.route("/ping", methods=["GET"])
@log_enpoint_information
def ping():
    return "Pong", 200
