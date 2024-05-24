import re
from src import logger
from src.model import User
from src.service.blacklist import blacklist_token
from src.service.user import save_new_user

UUID_PATTERN = re.compile(r"^[\da-f]{8}-([\da-f]{4}-){3}[\da-f]{12}$", re.IGNORECASE)


def register_user(data):
    try:
        response, status_code = save_new_user(data=data)
        if status_code == 201:
            # automatically login a user once the registration is successful
            user = User.query.filter_by(email=data.get("email")).first()
            auth_token = user.encode_auth_token(user.public_id)
            logger.info("Authentication token is generated.")
            response["auth_token"] = auth_token
        return response, status_code
    except Exception as e:
        logger.error(e)
        response_object = {"status": "fail", "message": "Try again"}
        return response_object, 500


def login_user(data):
    try:
        # fetch the user data
        user = User.query.filter_by(email=data.get("email")).first()
        if user and user.check_password(data.get("password")):
            auth_token = user.encode_auth_token(user.public_id)
            if auth_token:
                response_object = {
                    "status": "success",
                    "message": "Successfully logged in.",
                    "auth_token": auth_token,
                }
                return response_object, 200
        else:
            response_object = {
                "status": "fail",
                "message": "email or password does not match.",
            }
            return response_object, 401

    except Exception as e:
        logger.error(e)
        response_object = {"status": "fail", "message": "Try again"}
        return response_object, 500


def logout_user(data):
    if data:
        auth_token = data.split(" ")[1]
    else:
        auth_token = ""

    if auth_token:
        response = User.decode_auth_token(auth_token)
        if bool(UUID_PATTERN.match(response)):
            # mark the token as blacklisted
            return blacklist_token(token=auth_token)
        else:
            response_object = {"status": "fail", "message": response}
            return response_object, 401
    else:
        response_object = {"status": "fail", "message": "Provide a valid auth token."}
        return response_object, 403
