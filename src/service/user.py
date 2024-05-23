import uuid
from datetime import datetime, UTC

from .. import db
from ..model.user import User


def save_new_user(data):
    user = User.query.filter_by(email=data["email"]).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data["email"],
            username=data["email"],
            password=data["password"],
            is_confirmed=True,
            is_admin=data.get("is_admin", True),
            registered_on=datetime.now(UTC),
        )
        save_changes(new_user)
        response_object = {"status": "success", "message": "Successfully registered."}
        return response_object, 201
    else:
        response_object = {
            "status": "fail",
            "message": "User already exists. Please Log in.",
        }
        return response_object, 409


def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
