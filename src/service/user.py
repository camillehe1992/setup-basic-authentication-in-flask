import uuid
from datetime import datetime, UTC

from src import db, logger
from src.model import User


def save_new_user(data):
    email = data["email"]
    logger.debug(f"Create new user with email {email}")
    user = User.query.filter_by(email=data["email"]).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data["email"],
            username=data["username"],
            password=data["password"],
            is_confirmed=data.get("is_confirmed", False),
            is_admin=data.get("is_admin", False),
            registered_on=datetime.now(UTC),
        )
        save_changes(new_user)
        logger.info("Successfully registered.")
        response_object = {"status": "success", "message": "Successfully registered."}
        return response_object, 201
    else:
        logger.error("User already exists. Please Log in.")
        response_object = {
            "status": "fail",
            "message": "User already exists. Please Log in.",
        }
        return response_object, 409


def get_all_users():
    response = User.query.all()
    users = [user.to_dict() for user in response]
    logger.info(f"Retrieve all users. length={len(users)}")
    return {"message": "List all users", "data": users}, 200


def get_a_user(public_id):
    logger.info(f"Retrieve a user by public_id {public_id}")
    user = User.query.filter_by(public_id=public_id).first().to_dict()
    if not user:
        logger.error(f"User {public_id} not found!")
        return {"message": f"User {public_id} not found!"}, 404
    else:
        logger.info(f"Retrieved a user by public_id = {public_id} successfully")
        return {"message": f"Retrieve user successfully", "data": user}, 200


def save_changes(data):
    db.session.add(data)
    db.session.commit()
