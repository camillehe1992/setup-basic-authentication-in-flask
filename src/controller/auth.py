from flask import Blueprint, jsonify, request
from src import bcrypt, logger
from src.service.user import login_user, logout_user, save_new_user, save_changes
from src.model.user import User


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["POST"])
def register(current_user):
    email = request.json["email"]
    password = request.json["password"]

    if current_user.is_authenticated:
        logger.info("You are already registered.")
        return {"message": "You are already registered."}, 201

    user = User(email=email, password=password)
    save_new_user(user)
    save_changes(user)
    login_user(user)
    logger.info("You registered and are now logged in. Welcome!")
    return {"message": "You registered and are now logged in. Welcome!"}, 201


@auth_bp.route("/login", methods=["POST"])
def login(current_user):
    email = request.json["email"]
    password = request.json["password"]

    if current_user.is_authenticated:
        logger.info("You are already logged in")
        return {"message": "You are already logged in"}, 201

    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password, password):
        login_user(user)
        return {"message": "User logged in"}, 200
    else:
        logger.error("Invalid email and/or password")
        return {"message": "Invalid email and/or password"}, 400


@auth_bp.route("/logout", methods=["POST"])
def logout(current_user):
    logout_user(current_user)
    return jsonify({"message": ""}), 201
