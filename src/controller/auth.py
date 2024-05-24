from flask import Blueprint, request

from src.service.auth import register_user, login_user, logout_user

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["POST"])
def register():
    return register_user(data=request.json)


@auth_bp.route("/login", methods=["POST"])
def login():
    return login_user(data=request.json)


@auth_bp.route("/logout", methods=["GET"])
def logout():
    auth_token = request.headers["Authorization"]
    return logout_user(data=auth_token)
