import pkg_resources
from flask import Blueprint, jsonify, current_app as app
from datetime import datetime

system_bp = Blueprint("system", __name__, url_prefix="/system")


@system_bp.route("/health", methods=["GET"])
def health():
    return "SERVER IS UP!"


@system_bp.route("/info", methods=["GET"])
def sysinfo():
    return jsonify(
        {
            "build_platform": pkg_resources.get_build_platform(),
            "debug": app.config["DEBUG"],
            "environment": app.config["ENVIRONMENT"],
            "flask": pkg_resources.get_distribution("flask").version,
            "python": "3.11.9",
            "sqlalchemy": pkg_resources.get_distribution("sqlalchemy").version,
            "timestamp": datetime.now().strftime(format="%d/%m/%Y, %H:%M:%S"),
            "version": "0.0.1",
        }
    )
