from flask import Blueprint, request
from src import logger
from src.service.user import get_all_users, save_new_user, get_a_user

user_bp = Blueprint("user", __name__, url_prefix="/users")


@user_bp.route("/", methods=["GET"])
def list_all_users():
    return get_all_users()


@user_bp.route("/", methods=["POST"])
def create_user():
    payload = request.json
    logger.debug("Create new user with payload", {"payload": payload})
    return save_new_user(data=payload)


@user_bp.route("/<id>", methods=["GET"])
def get_user(id):
    return get_a_user(id=id)
