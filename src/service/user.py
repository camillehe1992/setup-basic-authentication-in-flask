import uuid
from datetime import datetime, UTC

from src import db, logger
from src.model.user import User


def login_user(data):
    pass


def logout_user(data):
    pass


def save_new_user(data):
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
        response_object = {"message": "Successfully registered."}
        return response_object, 201
    else:
        response_object = {
            "message": "User already exists. Please Log in.",
        }
        return response_object, 409


def get_all_users():
    users = User.query.all()
    logger.info(f"Retrieve all users. length={len(users)}")
    return [user.to_dict() for user in users]


def get_a_user(id):
    user = User.query.filter_by(public_id=id).first().to_dict()

    if not user:
        logger.error(f"User {id} not found!")
        return {"message": f"User {id} not found!"}, 404
    else:
        logger.info(f"Retrieve a user by public_id(id) = {user.id}")
        return {"message": f"Get user {user.id}", "data": user}, 200


def save_changes(data):
    db.session.add(data)
    db.session.commit()
