from flask import Blueprint, jsonify
from ..service.user import save_new_user, get_all_users, get_a_user

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["POST"])
def register():
    return jsonify({"message": ""}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    return jsonify({"message": ""}), 201
