from flask import Blueprint, request
from src import logger
from src.service.user import get_all_users, save_new_user, get_a_user

user_bp = Blueprint("user", __name__, url_prefix="/users")


@user_bp.route("/", methods=["GET"])
def list_all_users():
    return get_all_users()


@user_bp.route("/", methods=["POST", "OPTIONS"])
def create_user():
    data = request.json
    return save_new_user(data=data)


@user_bp.route("/<public_id>", methods=["GET"])
def get_user(public_id):
    return get_a_user(public_id=public_id)
